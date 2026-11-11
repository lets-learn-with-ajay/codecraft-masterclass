// Phase 1: IndexedDB Vector Store & Float32 Embedding Persistence
export interface LocalVectorRecord {
  id: string;
  content: string;
  embedding: Float32Array;
  updatedAt: number;
  synced: boolean;
}

export async function openVectorDB(): Promise<IDBDatabase> {
  return new Promise((resolve, reject) => {
    const req = indexedDB.open('ai_offline_vectors_v1', 1);
    req.onupgradeneeded = () => {
      const db = req.result;
      const store = db.createObjectStore('vectors', { keyPath: 'id' });
      store.createIndex('by_synced', 'synced', { unique: false });
    };
    req.onsuccess = () => resolve(req.result);
    req.onerror = () => reject(req.error);
  });
}

// Phase 2: In-Browser Cosine Similarity Search & WebGPU Fallback
export function cosineSimilarity(a: Float32Array, b: Float32Array): number {
  let dot = 0.0, normA = 0.0, normB = 0.0;
  for (let i = 0; i < a.length; i++) {
    dot += a[i] * b[i];
    normA += a[i] * a[i];
    normB += b[i] * b[i];
  }
  return dot / (Math.sqrt(normA) * Math.sqrt(normB) + 1e-8);
}

export async function searchOfflineVectors(
  records: LocalVectorRecord[],
  queryVec: Float32Array,
  topK = 4
): Promise<LocalVectorRecord[]> {
  return records
    .map((rec) => ({ rec, score: cosineSimilarity(rec.embedding, queryVec) }))
    .sort((a, b) => b.score - a.score)
    .slice(0, topK)
    .map((item) => item.rec);
}

// Phase 3: Background Cloud Sync & PostgreSQL pgvector Reconciliation
'use server';
import { db } from '@/lib/postgres';

export interface SyncMutationBatch {
  clientId: string;
  records: Array<{ id: string; content: string; embedding: number[]; updatedAt: number }>;
}

export async function reconcileOfflineMutations(batch: SyncMutationBatch) {
  const syncedIds: string[] = [];
  for (const item of batch.records) {
    await db.query(
      `INSERT INTO document_vectors (id, content, embedding, updated_at)
       VALUES ($1, $2, $3::vector, to_timestamp($4 / 1000.0))
       ON CONFLICT (id) DO UPDATE SET
         content = EXCLUDED.content,
         embedding = EXCLUDED.embedding,
         updated_at = GREATEST(document_vectors.updated_at, EXCLUDED.updated_at)`,
      [item.id, item.content, JSON.stringify(item.embedding), item.updatedAt]
    );
    syncedIds.push(item.id);
  }
  return { status: 'RECONCILED', syncedIds };
}
