// Phase 1: Next.js 15 Server Action & Token Streaming
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

// Phase 2: React 19 Client Component Stream Consumer
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

// Phase 3: AbortController Cancellation & Edge Rate Guard
import { NextRequest, NextResponse } from 'next/server';

export async function POST(req: NextRequest) {
  const controller = new AbortController();
  req.signal.addEventListener('abort', () => controller.abort());
  const { prompt } = await req.json();
  if (!prompt || prompt.length > 8000) {
    return NextResponse.json({ error: 'Prompt bounds exceeded' }, { status: 400 });
  }
  return NextResponse.json({ status: 'STREAM_READY' });
}
