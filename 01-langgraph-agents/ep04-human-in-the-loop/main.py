# Phase 1: Dynamic Breakpoints & Approval Interruption
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.sqlite import SqliteSaver

checkpointer = SqliteSaver.from_conn_string(':memory:')

# Compile graph with dynamic breakpoint before sensitive actions
app = workflow.compile(
    checkpointer=checkpointer,
    interrupt_before=['execute_transaction_node']
)

config = {'configurable': {'thread_id': 'txn_user_9921'}}
# Graph pauses execution immediately before sensitive node
pending_state = app.invoke({'amount': 25000, 'currency': 'USD'}, config=config)
