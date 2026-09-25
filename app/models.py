from pydantic import BaseModel
from typing import List, Dict, Any

class NaturalLanguageQuery(BaseModel):
    query: str

class SQLAgentResult(BaseModel):
    natural_query: str
    generated_sql: str
    execution_result: List[Dict[str, Any]]
    explanation: str
    safety_check_passed: bool
