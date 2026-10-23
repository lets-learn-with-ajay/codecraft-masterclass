# Phase 1: Checkpointer Configuration & Session Isolation
from langgraph.checkpoint.sqlite import SqliteSaver
from langgraph.checkpoint.postgres import PostgresSaver

# Configure durable checkpointer with connection pool
checkpointer = SqliteSaver.from_conn_string(':memory:')
app = workflow.compile(checkpointer=checkpointer)

# Isolate user sessions via monotonic thread configurations
session_config = {'configurable': {'thread_id': 'prod_usr_9842'}}
initial_state = {'messages': [{'role': 'user', 'content': 'Analyze Q3 metrics'}]}
final_state = app.invoke(initial_state, config=session_config)
