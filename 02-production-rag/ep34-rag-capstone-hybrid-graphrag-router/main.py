# Phase 1: Hybrid Neo4j K-Hop Subgraph & Dense Vector Retriever
from dataclasses import dataclass

@dataclass(frozen=True)
class KnowledgeTriplet:
    head: str
    relation: str
    tail: str
    confidence: float

def build_cypher_khop_query(entity_names: list[str], max_hops: int = 2) -> tuple[str, dict]:
    cypher = (
        f'MATCH (e:Entity)-[r:RELATES*1..{max_hops}]-(target:Entity) '
        'WHERE e.name IN $entities '
        'RETURN e.name AS head, type(r[0]) AS rel, target.name AS tail LIMIT 50'
    )
    return cypher, {'entities': entity_names}
