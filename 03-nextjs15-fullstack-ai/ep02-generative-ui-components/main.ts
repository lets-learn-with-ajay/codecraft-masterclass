"""
CodeCraft Masterclass: Nextjs15 Fullstack Ai - Episode 2
"""

// Phase 1: Server Action & Token Streaming
import { streamText } from 'ai';
import { openai } from '@ai-sdk/openai';
import { createStreamableValue } from 'ai/rsc';

export async function streamCompletion(prompt: string) {
  const stream = createStreamableValue('');
  (async () => {
    const { textStream } = await streamText({
      model: openai('gpt-4o'),
      prompt,
    });
    for await (const delta of textStream) stream.update(delta);
    stream.done();
  })();
  return { output: stream.value };
}


# ============================================================================
# NEXT SCENE
# ============================================================================

// Phase 2: React 19 Client Component Integration
'use client';
import { readStreamableValue } from 'ai/rsc';
import { useState } from 'react';

export function ChatStreamView() {
  const [text, setText] = useState('');
  async function handleSend(query: string) {
    const { output } = await streamCompletion(query);
    for await (const chunk of readStreamableValue(output)) {
      setText((prev) => prev + (chunk ?? ''));
    }
  }
  return <div className="font-mono p-6 bg-slate-900">{text}</div>;
}


# ============================================================================
# NEXT SCENE
# ============================================================================

// Phase 2: React 19 Client Component Integration
'use client';
import { readStreamableValue } from 'ai/rsc';
import { useState } from 'react';

export function ChatStreamView() {
  const [text, setText] = useState('');
  async function handleSend(query: string) {
    const { output } = await streamCompletion(query);
    for await (const chunk of readStreamableValue(output)) {
      setText((prev) => prev + (chunk ?? ''));
    }
  }
  return <div className="font-mono p-6 bg-slate-900">{text}</div>;
}


# ============================================================================
# NEXT SCENE
# ============================================================================

// Phase 1: Server Action & Token Streaming
import { streamText } from 'ai';
import { openai } from '@ai-sdk/openai';
import { createStreamableValue } from 'ai/rsc';

export async function streamCompletion(prompt: string) {
  const stream = createStreamableValue('');
  (async () => {
    const { textStream } = await streamText({
      model: openai('gpt-4o'),
      prompt,
    });
    for await (const delta of textStream) stream.update(delta);
    stream.done();
  })();
  return { output: stream.value };
}


# ============================================================================
# NEXT SCENE
# ============================================================================

// Phase 2: React 19 Client Component Integration
'use client';
import { readStreamableValue } from 'ai/rsc';
import { useState } from 'react';

export function ChatStreamView() {
  const [text, setText] = useState('');
  async function handleSend(query: string) {
    const { output } = await streamCompletion(query);
    for await (const chunk of readStreamableValue(output)) {
      setText((prev) => prev + (chunk ?? ''));
    }
  }
  return <div className="font-mono p-6 bg-slate-900">{text}</div>;
}


# ============================================================================
# NEXT SCENE
# ============================================================================

// Phase 2: React 19 Client Component Integration
'use client';
import { readStreamableValue } from 'ai/rsc';
import { useState } from 'react';

export function ChatStreamView() {
  const [text, setText] = useState('');
  async function handleSend(query: string) {
    const { output } = await streamCompletion(query);
    for await (const chunk of readStreamableValue(output)) {
      setText((prev) => prev + (chunk ?? ''));
    }
  }
  return <div className="font-mono p-6 bg-slate-900">{text}</div>;
}


# ============================================================================
# NEXT SCENE
# ============================================================================

// Phase 1: Server Action & Token Streaming
import { streamText } from 'ai';
import { openai } from '@ai-sdk/openai';
import { createStreamableValue } from 'ai/rsc';

export async function streamCompletion(prompt: string) {
  const stream = createStreamableValue('');
  (async () => {
    const { textStream } = await streamText({
      model: openai('gpt-4o'),
      prompt,
    });
    for await (const delta of textStream) stream.update(delta);
    stream.done();
  })();
  return { output: stream.value };
}
