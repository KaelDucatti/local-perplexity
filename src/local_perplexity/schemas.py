import operator
from typing import List

from pydantic import BaseModel
from typing_extensions import Annotated


class QueryResult(BaseModel):
    """Resultado de uma consulta de busca."""
    title: str = ""
    url: str = ""
    resume: str = ""


class ReportState(BaseModel):
    """Estado do sistema durante a geração de relatórios."""
    user_input: str = ""
    final_response: str = ""
    queries: List[str] = []
    queries_results: Annotated[List[QueryResult], operator.add]


class QueryList(BaseModel):
    """Lista de consultas para busca."""
    queries: List[str] = []
