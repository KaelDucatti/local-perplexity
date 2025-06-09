import operator
from typing import List

from pydantic import BaseModel
from typing_extensions import Annotated


class QueryResult(BaseModel):
    title: str = ""
    url: str = ""
    resume: str = ""


class ReportState(BaseModel):
    user_input: str = ""
    final_response: str = ""
    queries: List[str] = []
    queries_results: Annotated[List[QueryResult], operator.add]
