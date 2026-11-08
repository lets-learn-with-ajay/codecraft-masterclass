// Phase 1: Incremental Block-Level Content Hashing & Delta Embedding
import crypto from 'crypto';

export interface IndexedBlockChunk {
  blockId: string;
  contentHash: string;
  embedding: number[];
}

export function computeBlockDelta(
  blocks: Array<{ blockId: string; text: string }>,
  existingHashes: Record<string, string>
) {
  return blocks.filter((b) => {
    const hash = crypto.createHash('sha256').update(b.text).digest('hex');
    return existingHashes[b.blockId] !== hash;
  });
}
