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
