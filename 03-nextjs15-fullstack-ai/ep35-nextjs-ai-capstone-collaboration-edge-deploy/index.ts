// Phase 1: Hybrid Logical Clock (HLC) & LWW-Element-Set Block CRDT
export interface CrdtBlockRegister {
  blockId: string;
  value: string;
  hlcTimestamp: number;
  peerId: string;
}

export function mergeBlockRegisters(local: CrdtBlockRegister, remote: CrdtBlockRegister): CrdtBlockRegister {
  if (remote.hlcTimestamp > local.hlcTimestamp) return remote;
  if (remote.hlcTimestamp < local.hlcTimestamp) return local;
  return remote.peerId > local.peerId ? remote : local;
}

// Phase 2: Edge Presence Coordinator & Ephemeral Cursor Broadcast
export interface PeerCursorPresence {
  peerId: string;
  activeBlockId: string;
  selectionOffset: number;
  heartbeatMs: number;
}

export function pruneStalePeers(peers: PeerCursorPresence[], nowMs: number, ttlMs = 15000): PeerCursorPresence[] {
  return peers.filter((p) => nowMs - p.heartbeatMs <= ttlMs);
}

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
