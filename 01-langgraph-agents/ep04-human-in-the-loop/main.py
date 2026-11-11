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

# Phase 2: State Inspection, Human Feedback Injection & Resume
# Inspect paused state snapshot waiting for human approval
current_snapshot = app.get_state(config)
print(f'Next paused node: {current_snapshot.next}')

# Human reviewer approves or edits state payload
app.update_state(
    config,
    {'status': 'approved', 'approved_by': 'sre_admin@corp.internal'},
    as_node='human_review_node'
)

# Resume execution seamlessly from exact breakpoint
completed_state = app.invoke(None, config=config)

# Phase 2: State Inspection, Human Feedback Injection & Resume
# Inspect paused state snapshot waiting for human approval
current_snapshot = app.get_state(config)
print(f'Next paused node: {current_snapshot.next}')

# Human reviewer approves or edits state payload
app.update_state(
    config,
    {'status': 'approved', 'approved_by': 'sre_admin@corp.internal'},
    as_node='human_review_node'
)

# Resume execution seamlessly from exact breakpoint
completed_state = app.invoke(None, config=config)

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

# Phase 2: State Inspection, Human Feedback Injection & Resume
# Inspect paused state snapshot waiting for human approval
current_snapshot = app.get_state(config)
print(f'Next paused node: {current_snapshot.next}')

# Human reviewer approves or edits state payload
app.update_state(
    config,
    {'status': 'approved', 'approved_by': 'sre_admin@corp.internal'},
    as_node='human_review_node'
)

# Resume execution seamlessly from exact breakpoint
completed_state = app.invoke(None, config=config)

# Phase 2: State Inspection, Human Feedback Injection & Resume
# Inspect paused state snapshot waiting for human approval
current_snapshot = app.get_state(config)
print(f'Next paused node: {current_snapshot.next}')

# Human reviewer approves or edits state payload
app.update_state(
    config,
    {'status': 'approved', 'approved_by': 'sre_admin@corp.internal'},
    as_node='human_review_node'
)

# Resume execution seamlessly from exact breakpoint
completed_state = app.invoke(None, config=config)

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
