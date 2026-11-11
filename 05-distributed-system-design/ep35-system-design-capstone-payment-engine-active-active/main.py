# Phase 1: Consistent Hash Ring with Virtual Nodes
import hashlib
import bisect

class ConsistentHashRing:
    def __init__(self, vnodes: int = 128):
        self.vnodes = vnodes
        self.ring: list[int] = []
        self.node_map: dict[int, str] = {}

    def _hash(self, key: str) -> int:
        return int(hashlib.sha256(key.encode('utf-8')).hexdigest()[:16], 16)

    def add_shard(self, shard_id: str) -> None:
        for i in range(self.vnodes):
            h = self._hash(f'{shard_id}:vnode:{i}')
            bisect.insort(self.ring, h)
            self.node_map[h] = shard_id

# Phase 2: Deterministic Partition Routing & Quorum Lookup
    def route_key(self, partition_key: str) -> str:
        if not self.ring:
            raise RuntimeError('No active storage shards in ring')
        h = self._hash(partition_key)
        idx = bisect.bisect_right(self.ring, h)
        if idx == len(self.ring):
            idx = 0
        return self.node_map[self.ring[idx]]

# Phase 3: Idempotent Consumer Deduplication & Outbox Commit
def process_distributed_event(event_id: str, payload: dict, seen_ledger: set[str]) -> dict:
    if event_id in seen_ledger:
        return {'status': 'DUPLICATE_SKIPPED', 'event_id': event_id}
    seen_ledger.add(event_id)
    return {'status': 'COMMITTED', 'event_id': event_id, 'keys': len(payload)}
