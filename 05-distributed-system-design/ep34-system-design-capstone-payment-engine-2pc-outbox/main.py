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
