import os
from typing import Dict, List, cast

import streamlit as st
from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from langgraph.graph import END, START, StateGraph
from tavily import TavilyClient

from .prompts import build_final_response, build_queries, resume_research
from .schemas import QueryList, QueryResult, ReportState

load_dotenv()

api_key = os.getenv("TAVILY_API_KEY")

reasoning_llm = ChatOllama(model="llama3.2:3b")
llm = ChatOllama(model="deepseek-r1:1.5b")


def build_first_query(state: ReportState) -> Dict:
    user_input = state.user_input

    prompt = build_queries.format(user_input=user_input)
    query_llm = llm.with_structured_output(QueryList)
    result = cast(QueryList, query_llm.invoke(prompt))

    return {"queries": result.queries}


def execute_all_searches(state: ReportState) -> Dict:
    """Executa todas as pesquisas sequencialmente"""
    queries = state.queries
    user_input = state.user_input
    all_results = []
    
    tavily_client = TavilyClient(api_key=api_key)
    
    for query in queries:
        try:
            st.write(f"🔍 Searching: {query}")
            
            result = tavily_client.search(
                query=query,
                max_results=1,
                include_raw_content=False
            )
            
            if not result["results"]:
                st.write(f"❌ No results found for: {query}")
                continue
            
            url = result["results"][0]["url"]
            st.write(f"📄 Extracting content from: {url}")
            
            url_extraction = tavily_client.extract(url)

            if (url_extraction.get("results") and 
                len(url_extraction["results"]) > 0 and 
                url_extraction["results"][0].get("raw_content")):
                
                raw_content = url_extraction["results"][0]["raw_content"]
                prompt = resume_research.format(
                    user_input=user_input,
                    search_results=raw_content
                )
                llm_result = llm.invoke(prompt)
                query_result = QueryResult(
                    title=result["results"][0]["title"],
                    url=url,
                    resume=cast(str, llm_result.content)
                )
            else:
                query_result = QueryResult(
                    title=result["results"][0]["title"],
                    url=url,
                    resume=result["results"][0].get("content", "No detailed content available")
                )
            
            all_results.append(query_result)
            st.write(f"✅ Processed: {query_result.title}")
            
        except Exception as e:
            st.write(f"❌ Error searching for '{query}': {e}")
            continue
    
    return {"queries_results": all_results}


def final_writer(state: ReportState) -> Dict:
    st.write("📝 Generating final report...")
    
    search_results = ""
    references = ""
    
    for i, result in enumerate(state.queries_results):
        search_results += f"[{i + 1}]\n\n"
        search_results += f"Title: {result.title}\n"
        search_results += f"URL: {result.url}\n"
        search_results += f"Content: {result.resume}\n"
        search_results += "=================\n\n"

        references += f"[{i + 1}] - [{result.title}]({result.url})\n"

    prompt = build_final_response.format(
        user_input=state.user_input,
        search_results=search_results
    )

    llm_result = reasoning_llm.invoke(prompt)
    final_response = str(llm_result.content) + "\n\n## References:\n" + references
    return {"final_response": final_response}


# Construindo o grafo simplificado
builder = StateGraph(ReportState)

builder.add_node("build_first_query", build_first_query)
builder.add_node("execute_all_searches", execute_all_searches)
builder.add_node("final_writer", final_writer)

builder.add_edge(START, "build_first_query")
builder.add_edge("build_first_query", "execute_all_searches")
builder.add_edge("execute_all_searches", "final_writer")
builder.add_edge("final_writer", END)

graph = builder.compile()


def main():
    st.title("🔬 Local Perplexity Research Planner")
    st.markdown("*Powered by LangGraph + Tavily + Local LLMs*")
    
    user_input = st.text_area(
        "Enter your research question:",
        height=150,
        value="What is the impact of climate change on global food security?",
        help="Ask any research question and I'll search the web and provide a comprehensive report."
    )

    if st.button("🚀 Start Research", type="primary"):
        if not user_input.strip():
            st.error("Please enter a research question.")
            return
            
        if not api_key:
            st.error("Please set your TAVILY_API_KEY in the environment variables.")
            return

        with st.status("🔍 Researching your question...", expanded=True) as status:
            try:
                # Executa o grafo
                final_state = graph.invoke({"user_input": user_input})
                status.update(label="✅ Research completed!", state="complete")
                
            except Exception as e:
                st.error(f"Error during research: {e}")
                return
            
        # Obtém a resposta final
        final_response = final_state.final_response
        
        if final_response:
            st.markdown("## 📊 Research Report")
            
            # Verifica se tem tags de pensamento para separar
            if "</think>" in final_response:
                think_str = final_response.split("</think>")[0].replace("<think>", "")
                final_response_clean = final_response.split("</think>")[1]
                
                with st.expander("🧠 AI Reasoning Process", expanded=False):
                    st.markdown(think_str)
                    
                st.markdown(final_response_clean)
            else:
                st.markdown(final_response)
                
            # Mostrar informações sobre os resultados
            num_sources = len(final_state.queries_results)
            st.success(f"✅ Report generated successfully using {num_sources} sources")
            
        else:
            st.error("❌ Could not generate the final report.")


if __name__ == "__main__":
    main()