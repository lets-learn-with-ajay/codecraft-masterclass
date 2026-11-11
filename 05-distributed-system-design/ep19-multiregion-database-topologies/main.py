# Phase 1: Consistent Hash Ring with Virtual Nodes
import hashlib
import bisect

class ConsistentHashRing:
    def __init__(self, replicas: int = 150):
        self.replicas = replicas
        self.ring = []
        self.node_map = {}

    def _hash(self, key: str) -> int:
        return int(hashlib.md5(key.encode('utf-8')).hexdigest(), 16)

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

# Phase 1: Consistent Hash Ring with Virtual Nodes
import hashlib
import bisect

class ConsistentHashRing:
    def __init__(self, replicas: int = 150):
        self.replicas = replicas
        self.ring = []
        self.node_map = {}

    def _hash(self, key: str) -> int:
        return int(hashlib.md5(key.encode('utf-8')).hexdigest(), 16)

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

# Phase 1: Consistent Hash Ring with Virtual Nodes
import hashlib
import bisect

class ConsistentHashRing:
    def __init__(self, replicas: int = 150):
        self.replicas = replicas
        self.ring = []
        self.node_map = {}

    def _hash(self, key: str) -> int:
        return int(hashlib.md5(key.encode('utf-8')).hexdigest(), 16)
