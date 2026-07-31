from pydantic import BaseModel

class SearchRequest(BaseModel):
    query: str
    n_results: int = 3