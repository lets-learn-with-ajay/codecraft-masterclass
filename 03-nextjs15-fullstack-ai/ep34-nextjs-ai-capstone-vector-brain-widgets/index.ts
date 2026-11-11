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

// Phase 2: Generative UI Tool Router Streaming Interactive Workspace Cards
import { z } from 'zod';

export const KanbanBoardToolSchema = z.object({
  boardTitle: z.string(),
  columns: z.array(z.object({
    status: z.enum(['TODO', 'IN_PROGRESS', 'DONE']),
    tasks: z.array(z.object({ id: z.string(), title: z.string(), sourceBlockId: z.string() })),
  })),
});

export type KanbanBoardSpec = z.infer<typeof KanbanBoardToolSchema>;

// Phase 3: Bi-Directional Block Citation Anchor & Scroll Highlighter
export interface BlockCitationRef {
  citationIndex: number;
  sourceBlockId: string;
  similarityScore: number;
}

export function filterVerifiedBlockCitations(refs: BlockCitationRef[], minScore = 0.78): BlockCitationRef[] {
  return refs.filter((r) => r.similarityScore >= minScore);
}
