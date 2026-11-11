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

# Phase 2: Time-Travel Debugging & State Replay
# Inspect full historical audit trail of state transitions
state_history = list(app.get_state_history(session_config))
print(f'Total checkpoint supersteps: {len(state_history)}')

# Rewind to target historical checkpoint before failure
target_checkpoint = state_history[-2]
rewind_config = target_checkpoint.config

# Fork execution path with sanitized state updates
app.update_state(rewind_config, {'messages': [{'role': 'system', 'content': 'Strict mode'}]})
resumed_state = app.invoke(None, config=rewind_config)

# Phase 2: Time-Travel Debugging & State Replay
# Inspect full historical audit trail of state transitions
state_history = list(app.get_state_history(session_config))
print(f'Total checkpoint supersteps: {len(state_history)}')

# Rewind to target historical checkpoint before failure
target_checkpoint = state_history[-2]
rewind_config = target_checkpoint.config

# Fork execution path with sanitized state updates
app.update_state(rewind_config, {'messages': [{'role': 'system', 'content': 'Strict mode'}]})
resumed_state = app.invoke(None, config=rewind_config)

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

# Phase 2: Time-Travel Debugging & State Replay
# Inspect full historical audit trail of state transitions
state_history = list(app.get_state_history(session_config))
print(f'Total checkpoint supersteps: {len(state_history)}')

# Rewind to target historical checkpoint before failure
target_checkpoint = state_history[-2]
rewind_config = target_checkpoint.config

# Fork execution path with sanitized state updates
app.update_state(rewind_config, {'messages': [{'role': 'system', 'content': 'Strict mode'}]})
resumed_state = app.invoke(None, config=rewind_config)

# Phase 2: Time-Travel Debugging & State Replay
# Inspect full historical audit trail of state transitions
state_history = list(app.get_state_history(session_config))
print(f'Total checkpoint supersteps: {len(state_history)}')

# Rewind to target historical checkpoint before failure
target_checkpoint = state_history[-2]
rewind_config = target_checkpoint.config

# Fork execution path with sanitized state updates
app.update_state(rewind_config, {'messages': [{'role': 'system', 'content': 'Strict mode'}]})
resumed_state = app.invoke(None, config=rewind_config)

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
