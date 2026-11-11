# Phase 1: Transactional Outbox Pattern & CDC
CREATE TABLE orders (
    order_id UUID PRIMARY KEY,
    user_id UUID NOT NULL,
    total_amount NUMERIC(10,2) NOT NULL
);

CREATE TABLE transactional_outbox (
    event_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    aggregate_type VARCHAR(64) NOT NULL,
    payload JSONB NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

# Phase 2: Idempotent Kafka Consumer Deduplication
def consume_kafka_event(event: dict, redis_client):
    event_id = event['event_id']
    # Atomic idempotency check with 24-hour TTL window
    is_new = redis_client.set(f'dedup:{event_id}', 'processed', ex=86400, nx=True)
    if not is_new:
        log(f'Duplicate event {event_id} discarded cleanly')
        return

    dispatch_event_to_handler(event)

# Phase 2: Idempotent Kafka Consumer Deduplication
def consume_kafka_event(event: dict, redis_client):
    event_id = event['event_id']
    # Atomic idempotency check with 24-hour TTL window
    is_new = redis_client.set(f'dedup:{event_id}', 'processed', ex=86400, nx=True)
    if not is_new:
        log(f'Duplicate event {event_id} discarded cleanly')
        return

    dispatch_event_to_handler(event)

# Phase 1: Transactional Outbox Pattern & CDC
CREATE TABLE orders (
    order_id UUID PRIMARY KEY,
    user_id UUID NOT NULL,
    total_amount NUMERIC(10,2) NOT NULL
);

CREATE TABLE transactional_outbox (
    event_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    aggregate_type VARCHAR(64) NOT NULL,
    payload JSONB NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

# Phase 2: Idempotent Kafka Consumer Deduplication
def consume_kafka_event(event: dict, redis_client):
    event_id = event['event_id']
    # Atomic idempotency check with 24-hour TTL window
    is_new = redis_client.set(f'dedup:{event_id}', 'processed', ex=86400, nx=True)
    if not is_new:
        log(f'Duplicate event {event_id} discarded cleanly')
        return

    dispatch_event_to_handler(event)

# Phase 2: Idempotent Kafka Consumer Deduplication
def consume_kafka_event(event: dict, redis_client):
    event_id = event['event_id']
    # Atomic idempotency check with 24-hour TTL window
    is_new = redis_client.set(f'dedup:{event_id}', 'processed', ex=86400, nx=True)
    if not is_new:
        log(f'Duplicate event {event_id} discarded cleanly')
        return

    dispatch_event_to_handler(event)

# Phase 1: Transactional Outbox Pattern & CDC
CREATE TABLE orders (
    order_id UUID PRIMARY KEY,
    user_id UUID NOT NULL,
    total_amount NUMERIC(10,2) NOT NULL
);

CREATE TABLE transactional_outbox (
    event_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    aggregate_type VARCHAR(64) NOT NULL,
    payload JSONB NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);
