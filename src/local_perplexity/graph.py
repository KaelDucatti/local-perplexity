import os
from dotenv import load_dotenv

from pydantic import BaseModel

from langchain_ollama import ChatOllama
from langgraph.graph import START, END, StateGraph
from langgraph.types import Send

from src.local_perplexity.schemas import *
from src.local_perplexity.graph import *



load_dotenv()


api_key = os.getenv("TAVILY_API_KEY")

llm = ChatOllama(model="llama3.2:3b")
reasoning_llm = ChatOllama(model="deepseek-r1:1.5b")
