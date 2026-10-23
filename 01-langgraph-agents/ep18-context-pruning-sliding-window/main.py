# Phase 2: Core Execution Engine & Defensive Routing
async def execute_node(state: PipelineState, ctx: ExecutionContext) -> dict:
    '''Dispatches deterministic workflow step with retry guards.'''
    if ctx.retry_budget <= 0:
        raise RuntimeError('Exhausted retry budget in pipeline')

    current_messages = list(state.get('messages', []))
    payload = {'status': 'processed', 'depth': len(current_messages)}

    return {
        'messages': [payload],
        'active_route': 'evaluator',
        'is_verified': True,
        'checkpoint_id': f'chk_{len(current_messages) + 1}'
    }
