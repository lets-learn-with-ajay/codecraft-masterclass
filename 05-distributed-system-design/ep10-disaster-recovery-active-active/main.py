# Phase 2: Idempotent Kafka Consumer Deduplication
def consume_kafka_event(event: dict, redis_client):
    event_id = event['event_id']
    # Atomic idempotency check with 24-hour TTL window
    is_new = redis_client.set(f'dedup:{event_id}', 'processed', ex=86400, nx=True)
    if not is_new:
        log(f'Duplicate event {event_id} discarded cleanly')
        return

    dispatch_event_to_handler(event)
