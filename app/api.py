from fastapi import FastAPI, HTTPException
from app.config import settings
from app.models import NaturalLanguageQuery, SQLAgentResult
from app.services.sql_engine import run_text_to_sql

app = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION)

@app.post("/query-database", response_model=SQLAgentResult)
def query_db(q: NaturalLanguageQuery):
    sql, rows, exp, passed = run_text_to_sql(q.query)
    if not passed:
        raise HTTPException(status_code=403, detail=exp)
    return SQLAgentResult(
        natural_query=q.query,
        generated_sql=sql,
        execution_result=rows,
        explanation=exp,
        safety_check_passed=passed
    )
