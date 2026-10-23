// Phase 1: Generative UI Tool Definition
import { streamUI } from 'ai/rsc';
import { z } from 'zod';
import { StockWidget } from '@/components/StockWidget';

export async function submitUserMessage(userInput: string) {
  'use server';
  return await streamUI({
    model: openai('gpt-4o'),
    prompt: userInput,
    tools: {
      showStockChart: {
        parameters: z.object({ ticker: z.string(), days: z.number() }),
        generate: async ({ ticker, days }) => <StockWidget ticker={ticker} days={days} />,
      },
    },
  });
}
