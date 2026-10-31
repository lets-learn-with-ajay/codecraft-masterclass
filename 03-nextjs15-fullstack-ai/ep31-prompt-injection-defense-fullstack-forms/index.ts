// Phase 3: Optimistic UI State & Error Boundary Recovery
'use client';
import { useOptimistic, useTransition } from 'react';

export function useResilientAction(initialState: ExecutionPayload[]) {
  const [isPending, startTransition] = useTransition();
  const [optimisticItems, addOptimistic] = useOptimistic(
    initialState,
    (state, newItem: ExecutionPayload) => [...state, newItem]
  );
  return { optimisticItems, addOptimistic, isPending, startTransition };
}
