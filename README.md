### Local Perplexity





## 📝 Sobre o Projeto

O **Local Perplexity** é uma aplicação de pesquisa avançada que combina modelos de linguagem locais (LLMs) com pesquisa web em tempo real para responder perguntas dos usuários de maneira detalhada e fundamentada. Inspirado no serviço Perplexity.ai, este projeto permite executar pesquisas robustas usando modelos executados localmente, proporcionando respostas técnicas precisas com citações adequadas.

## 🏗️ Arquitetura

O Local Perplexity utiliza uma arquitetura baseada em grafos de estados para orquestrar o fluxo de trabalho de pesquisa e síntese de informações:

![Texto Alternativo](/home/kael/cursos/local_perplexity/local_perplexity.excalidraw.png)

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