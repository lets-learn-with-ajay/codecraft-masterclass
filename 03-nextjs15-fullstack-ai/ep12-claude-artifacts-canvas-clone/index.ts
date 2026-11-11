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

// Phase 2: Dynamic Streaming UI Handlers
'use client';
import { useActions, useUIState } from 'ai/rsc';

export function GenerativeUIPanel() {
  const [conversation, setConversation] = useUIState();
  const { submitUserMessage } = useActions();

  const onSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    const responseUI = await submitUserMessage(input);
    setConversation((current: any) => [...current, responseUI]);
  };
  return <div className="space-y-4">{conversation}</div>;
}

// Phase 2: Dynamic Streaming UI Handlers
'use client';
import { useActions, useUIState } from 'ai/rsc';

export function GenerativeUIPanel() {
  const [conversation, setConversation] = useUIState();
  const { submitUserMessage } = useActions();

  const onSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    const responseUI = await submitUserMessage(input);
    setConversation((current: any) => [...current, responseUI]);
  };
  return <div className="space-y-4">{conversation}</div>;
}

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

// Phase 2: Dynamic Streaming UI Handlers
'use client';
import { useActions, useUIState } from 'ai/rsc';

export function GenerativeUIPanel() {
  const [conversation, setConversation] = useUIState();
  const { submitUserMessage } = useActions();

  const onSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    const responseUI = await submitUserMessage(input);
    setConversation((current: any) => [...current, responseUI]);
  };
  return <div className="space-y-4">{conversation}</div>;
}

// Phase 2: Dynamic Streaming UI Handlers
'use client';
import { useActions, useUIState } from 'ai/rsc';

export function GenerativeUIPanel() {
  const [conversation, setConversation] = useUIState();
  const { submitUserMessage } = useActions();

  const onSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    const responseUI = await submitUserMessage(input);
    setConversation((current: any) => [...current, responseUI]);
  };
  return <div className="space-y-4">{conversation}</div>;
}

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
