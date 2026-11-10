// Phase 3: Durable Edge-to-Postgres CRDT Checkpoint Compaction
'use server';
import { db } from '@/lib/postgres';

export async function flushCrdtCheckpoint(workspaceId: string, registers: CrdtBlockRegister[]) {
  for (const reg of registers) {
    await db.query(
      `INSERT INTO workspace_blocks (workspace_id, block_id, content, hlc_ts, peer_id)
       VALUES ($1, $2, $3, $4, $5)
       ON CONFLICT (workspace_id, block_id) DO UPDATE SET
         content = CASE WHEN EXCLUDED.hlc_ts >= workspace_blocks.hlc_ts THEN EXCLUDED.content ELSE workspace_blocks.content END,
         hlc_ts = GREATEST(workspace_blocks.hlc_ts, EXCLUDED.hlc_ts)`,
      [workspaceId, reg.blockId, reg.value, reg.hlcTimestamp, reg.peerId]
    );
  }
  return { status: 'CHECKPOINT_COMMITTED', count: registers.length };
}
