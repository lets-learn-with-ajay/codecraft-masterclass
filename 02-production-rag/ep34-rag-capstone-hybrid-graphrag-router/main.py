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

# Phase 2: Adaptive Complexity Router (Vector Fast-Path vs GraphRAG)
def route_rag_query(query: str, entity_count: int) -> str:
    multi_hop_markers = ('how does', 'relationship between', 'compare', 'impact of', 'chain')
    q_low = query.lower()
    if entity_count >= 2 or any(m in q_low for m in multi_hop_markers):
        return 'HYBRID_NEO4J_GRAPHRAG'
    return 'DENSE_VECTOR_FASTPATH'

# Phase 3: Self-Correcting Triplet Hallucination Verifier
def verify_triplet_grounding(answer_text: str, triplets: list[KnowledgeTriplet]) -> dict:
    ans_low = answer_text.lower()
    supported = [t for t in triplets if t.head.lower() in ans_low and t.tail.lower() in ans_low]
    ratio = len(supported) / max(len(triplets), 1)
    return {
        'action': 'COMMIT_ANSWER' if ratio >= 0.5 else 'REWRITE_GRAPH_QUERY',
        'supported_triplets': len(supported),
        'grounding_ratio': round(ratio, 3),
    }
