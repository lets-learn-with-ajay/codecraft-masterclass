# Phase 2: Node Lookup & Hotspot Rebalancing
    def get_node(self, key: str) -> str:
        if not self.ring: return None
        h = self._hash(key)
        idx = bisect.bisect_right(self.ring, h)
        if idx == len(self.ring): idx = 0
        return self.node_map[self.ring[idx]]

ring = ConsistentHashRing()
for shard in ['db_shard_01', 'db_shard_02', 'db_shard_03']: ring.add_node(shard)
target_shard = ring.get_node('user_session_98412')
