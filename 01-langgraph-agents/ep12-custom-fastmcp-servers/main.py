# Phase 1: MCP Tool Schemas & Server Connection
from typing import Annotated, TypedDict
from langchain_core.tools import tool
from pydantic import BaseModel, Field

class DatabaseQueryInput(BaseModel):
    query: str = Field(description='SQL query string')
    max_rows: int = Field(default=100, le=1000)

@tool('query_production_db', args_schema=DatabaseQueryInput)
def query_production_db(query: str, max_rows: int = 100) -> dict:
    '''Executes read-only SQL queries against Postgres replica.'''
    return {'status': 'success', 'rows': [{'id': 1, 'metric': 42.8}]}
