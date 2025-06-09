### Local Perplexity





## 📝 Sobre o Projeto

O **Local Perplexity** é uma aplicação de pesquisa avançada que combina modelos de linguagem locais (LLMs) com pesquisa web em tempo real para responder perguntas dos usuários de maneira detalhada e fundamentada. Inspirado no serviço Perplexity.ai, este projeto permite executar pesquisas robustas usando modelos executados localmente, proporcionando respostas técnicas precisas com citações adequadas.

## 🏗️ Arquitetura

O Local Perplexity utiliza uma arquitetura baseada em grafos de estados para orquestrar o fluxo de trabalho de pesquisa e síntese de informações:

```mermaid
Arquitetura do Local Perplexity.download-icon {
            cursor: pointer;
            transform-origin: center;
        }
        .download-icon .arrow-part {
            transition: transform 0.35s cubic-bezier(0.35, 0.2, 0.14, 0.95);
             transform-origin: center;
        }
        button:has(.download-icon):hover .download-icon .arrow-part, button:has(.download-icon):focus-visible .download-icon .arrow-part {
          transform: translateY(-1.5px);
        }
        #mermaid-diagram-r107{font-family:var(--font-geist-sans);font-size:12px;fill:#000000;}#mermaid-diagram-r107 .error-icon{fill:#552222;}#mermaid-diagram-r107 .error-text{fill:#552222;stroke:#552222;}#mermaid-diagram-r107 .edge-thickness-normal{stroke-width:1px;}#mermaid-diagram-r107 .edge-thickness-thick{stroke-width:3.5px;}#mermaid-diagram-r107 .edge-pattern-solid{stroke-dasharray:0;}#mermaid-diagram-r107 .edge-thickness-invisible{stroke-width:0;fill:none;}#mermaid-diagram-r107 .edge-pattern-dashed{stroke-dasharray:3;}#mermaid-diagram-r107 .edge-pattern-dotted{stroke-dasharray:2;}#mermaid-diagram-r107 .marker{fill:#666;stroke:#666;}#mermaid-diagram-r107 .marker.cross{stroke:#666;}#mermaid-diagram-r107 svg{font-family:var(--font-geist-sans);font-size:12px;}#mermaid-diagram-r107 p{margin:0;}#mermaid-diagram-r107 .label{font-family:var(--font-geist-sans);color:#000000;}#mermaid-diagram-r107 .cluster-label text{fill:#333;}#mermaid-diagram-r107 .cluster-label span{color:#333;}#mermaid-diagram-r107 .cluster-label span p{background-color:transparent;}#mermaid-diagram-r107 .label text,#mermaid-diagram-r107 span{fill:#000000;color:#000000;}#mermaid-diagram-r107 .node rect,#mermaid-diagram-r107 .node circle,#mermaid-diagram-r107 .node ellipse,#mermaid-diagram-r107 .node polygon,#mermaid-diagram-r107 .node path{fill:#eee;stroke:#999;stroke-width:1px;}#mermaid-diagram-r107 .rough-node .label text,#mermaid-diagram-r107 .node .label text{text-anchor:middle;}#mermaid-diagram-r107 .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#mermaid-diagram-r107 .node .label{text-align:center;}#mermaid-diagram-r107 .node.clickable{cursor:pointer;}#mermaid-diagram-r107 .arrowheadPath{fill:#333333;}#mermaid-diagram-r107 .edgePath .path{stroke:#666;stroke-width:2.0px;}#mermaid-diagram-r107 .flowchart-link{stroke:#666;fill:none;}#mermaid-diagram-r107 .edgeLabel{background-color:white;text-align:center;}#mermaid-diagram-r107 .edgeLabel p{background-color:white;}#mermaid-diagram-r107 .edgeLabel rect{opacity:0.5;background-color:white;fill:white;}#mermaid-diagram-r107 .labelBkg{background-color:rgba(255, 255, 255, 0.5);}#mermaid-diagram-r107 .cluster rect{fill:hsl(0, 0%, 98.9215686275%);stroke:#707070;stroke-width:1px;}#mermaid-diagram-r107 .cluster text{fill:#333;}#mermaid-diagram-r107 .cluster span{color:#333;}#mermaid-diagram-r107 div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:var(--font-geist-sans);font-size:12px;background:hsl(-160, 0%, 93.3333333333%);border:1px solid #707070;border-radius:2px;pointer-events:none;z-index:100;}#mermaid-diagram-r107 .flowchartTitleText{text-anchor:middle;font-size:18px;fill:#000000;}#mermaid-diagram-r107 .flowchart-link{stroke:hsl(var(--gray-400));stroke-width:1px;}#mermaid-diagram-r107 .marker,#mermaid-diagram-r107 marker,#mermaid-diagram-r107 marker *{fill:hsl(var(--gray-400))!important;stroke:hsl(var(--gray-400))!important;}#mermaid-diagram-r107 .label,#mermaid-diagram-r107 text,#mermaid-diagram-r107 text>tspan{fill:hsl(var(--black))!important;color:hsl(var(--black))!important;}#mermaid-diagram-r107 .background,#mermaid-diagram-r107 rect.relationshipLabelBox{fill:hsl(var(--white))!important;}#mermaid-diagram-r107 .entityBox,#mermaid-diagram-r107 .attributeBoxEven{fill:hsl(var(--gray-150))!important;}#mermaid-diagram-r107 .attributeBoxOdd{fill:hsl(var(--white))!important;}#mermaid-diagram-r107 .label-container,#mermaid-diagram-r107 rect.actor{fill:hsl(var(--white))!important;stroke:hsl(var(--gray-400))!important;}#mermaid-diagram-r107 line{stroke:hsl(var(--gray-400))!important;}#mermaid-diagram-r107 :root{--mermaid-font-family:var(--font-geist-sans);}ParaleloEntrada do Usuáriobuild_first_queriesspawn_researcherssingle_searchfinal_writerResposta Final
```

### Componentes Principais

1. **Interface do Usuário**: Implementada com Streamlit, fornece uma interface web intuitiva para inserção de perguntas.
2. **Motor de Grafo de Estados**: Utiliza LangGraph para orquestrar o fluxo de trabalho da aplicação.
3. **Modelos de Linguagem**: Utiliza modelos Llama e DeepSeek através do Ollama para processamento de linguagem natural.
4. **Cliente de Pesquisa Web**: Integra-se com a API Tavily para realizar buscas na web e extrair conteúdo relevante.


## 🔄 Fluxo de Dados

O fluxo de processamento do Local Perplexity segue estas etapas principais:

1. **Entrada do Usuário**: O usuário insere uma pergunta através da interface Streamlit.
2. **Geração de Consultas**:
O sistema analisa a pergunta do usuário e gera múltiplas consultas de pesquisa específicas:

```python
def build_first_queries(state: ReportState):
    # Gera 3-5 consultas estratégicas baseadas na pergunta do usuário
    prompt = build_queries.format(user_input=user_input)
    query_llm = llm.with_structured_output(QueryList)
    result = query_llm.invoke(prompt)
    return {"queries": result.queries}
```


3. **Pesquisa Paralela**:
Cada consulta gerada é processada paralelamente:

```python
def spawn_researchers(state: ReportState):
    return [Send("single_search", {"query": query, "user_input": state.user_input})
            for query in state.queries]
```


4. **Busca e Síntese Individual**:
Para cada consulta, o sistema:

1. Realiza uma busca web usando a API Tavily
2. Extrai o conteúdo das páginas encontradas
3. Sintetiza as informações relevantes



5. **Síntese Final**:
Todas as informações coletadas são combinadas em uma resposta final coerente e bem estruturada, incluindo referências às fontes.


## 🧰 Tecnologias Utilizadas

| Tecnologia | Versão | Função
|-----|-----|-----
| **Streamlit** | 1.45.1 | Interface web interativa
| **LangGraph** | 0.4.8 | Orquestração do fluxo de trabalho baseado em grafos
| **LangChain** | 0.3.25 | Framework para aplicações com LLMs
| **Ollama** | 0.5.1 | Execução local de modelos de linguagem
| **Tavily Python** | 0.7.5 | Cliente para API de pesquisa web
| **Python-dotenv** | 1.1.0 | Gerenciamento de variáveis de ambiente
| **Pydantic** | 2.11.5 | Validação de esquemas de dados


## 📦 Instalação

### Pré-requisitos

- Python 3.12+
- Ollama instalado e configurado com os modelos:

- `llama3.2:1b`
- `deepseek-r1:1.5b`



- Chave de API do Tavily para pesquisa web


### Passos para Instalação

1. **Clone o repositório**


```shellscript
git clone https://github.com/seu-usuario/local-perplexity.git
cd local-perplexity
```

2. **Configure o ambiente virtual (opcional, mas recomendado)**


```shellscript
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

3. **Instale as dependências**


```shellscript
pip install -r requirements.txt
```

4. **Configure as variáveis de ambiente**


Crie um arquivo `.env` na raiz do projeto:

```plaintext
TAVILY_API_KEY=sua_chave_api_tavily
```

## 🚀 Como Usar

### Executando a Aplicação

```shellscript
python app.py
```

Isso iniciará o servidor Streamlit e abrirá a aplicação no navegador (geralmente em [http://localhost:8501](http://localhost:8501)).

### Interface da Aplicação

1. Digite sua pergunta no campo de texto.
2. Clique no botão "Pesquisar".
3. Acompanhe o progresso da pesquisa em tempo real.
4. Visualize a resposta gerada, incluindo as referências às fontes utilizadas.
5. (Opcional) Expanda a seção "🧠 Reflexão" para ver o raciocínio do modelo.


## 📁 Estrutura do Projeto

```plaintext
local-perplexity/
├── app.py                    # Ponto de entrada principal
├── requirements.txt          # Dependências do projeto
├── pyproject.toml           # Configuração do poetry
├── poetry.lock              # Lock file das dependências
└── src/
    └── local_perplexity/
        ├── __init__.py
        ├── graph.py         # Definição do grafo e interface
        ├── prompts.py       # Templates de prompts para os LLMs
        ├── schemas.py       # Esquemas de dados usando Pydantic
        └── utils.py         # Funções utilitárias e APIs
```

## 🔍 Funcionalidades Principais

### Geração Inteligente de Consultas

O sistema analisa a pergunta do usuário e gera automaticamente múltiplas consultas específicas para garantir uma cobertura abrangente do tópico.

### Pesquisa Web com Fontes Verificáveis

Utiliza a API Tavily para realizar buscas na web e extrair conteúdo completo de páginas relevantes, fornecendo informações atualizadas e verificáveis.

### Processamento Paralelo

Executa múltiplas pesquisas simultaneamente, melhorando a eficiência e a velocidade de resposta.

### Síntese Avançada de Informações

Combina informações de múltiplas fontes em uma resposta coerente, bem estruturada e tecnicamente precisa.

### Sistema de Citações

Inclui referências numeradas para todas as fontes utilizadas, permitindo ao usuário verificar as informações originais.

## 💻 Exemplos de Prompts

Os prompts utilizados pelo sistema são cuidadosamente estruturados para guiar os modelos de linguagem:

### Prompt para Geração de Consultas

```python
build_queries = agent_prompt + """
Seu primeiro objetivo é construir uma lista de consultas
que serão usadas para encontrar respostas à pergunta do usuário.

Responda com algo entre 3-5 consultas.
"""
```

### Prompt para Síntese Final

```python
build_final_response = agent_prompt + """
Seu objetivo aqui é desenvolver uma resposta final para o usuário usando
os relatórios feitos durante a pesquisa web, com suas sínteses.

A resposta deve conter algo entre 500 - 800 palavras.

Aqui estão os resultados da pesquisa web:
<SEARCH_RESULTS>
{search_results}
</SEARCH_RESULTS>

Você deve adicionar citações de referência (com o número da citação, exemplo: [1]) para os 
artigos que você usou em cada parágrafo da sua resposta.
"""
```

## ⚠️ Limitações Conhecidas

- Depende de modelos locais, exigindo recursos computacionais adequados
- Limitado a 1 resultado por consulta por padrão (configurável)
- Processamento sequencial de extração de conteúdo pode ser lento para páginas complexas
- Qualidade das respostas depende dos modelos de linguagem utilizados


## 🔮 Melhorias Futuras

- Implementação de cache para consultas repetidas
- Suporte a múltiplos provedores de pesquisa
- Interface mais rica com visualizações e histórico de pesquisas
- Sistema de feedback do usuário para melhorar respostas futuras
- Opção para escolher diferentes modelos de linguagem
- Otimização de prompts para casos de uso específicos


## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

1. Faça um fork do projeto
2. Crie sua branch de feature (`git checkout -b feature/nova-funcionalidade`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/nova-funcionalidade`)
5. Abra um Pull Request


## 📄 Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo LICENSE para detalhes.

---

Desenvolvido por [Seu Nome] - [Seu Email]