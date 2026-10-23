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
