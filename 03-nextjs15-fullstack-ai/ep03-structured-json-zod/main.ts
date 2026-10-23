"""
CodeCraft Masterclass: Nextjs15 Fullstack Ai - Episode 3
"""

// Phase 1: Zod Defensive Schema Contracts
import { z } from 'zod';
import { generateObject } from 'ai';
import { openai } from '@ai-sdk/openai';

export const AnalyticsPayloadSchema = z.object({
  metricName: z.string(),
  p99LatencyMs: z.number().positive(),
  errorRatePercent: z.number().min(0).max(100),
  recommendation: z.enum(['SCALE_UP', 'RETRY_BACKOFF', 'HEALTHY']),
});

export type AnalyticsPayload = z.infer<typeof AnalyticsPayloadSchema>;


# ============================================================================
# NEXT SCENE
# ============================================================================

// Phase 2: Type-Safe Generation & Auto-Repair
export async function generateSafeMetrics(rawLogs: string): Promise<AnalyticsPayload> {
  const { object } = await generateObject({
    model: openai('gpt-4o'),
    schema: AnalyticsPayloadSchema,
    prompt: `Extract metrics from logs: ${rawLogs}`,
    maxRetries: 3,
  });
  return object;
}


# ============================================================================
# NEXT SCENE
# ============================================================================

// Phase 2: Type-Safe Generation & Auto-Repair
export async function generateSafeMetrics(rawLogs: string): Promise<AnalyticsPayload> {
  const { object } = await generateObject({
    model: openai('gpt-4o'),
    schema: AnalyticsPayloadSchema,
    prompt: `Extract metrics from logs: ${rawLogs}`,
    maxRetries: 3,
  });
  return object;
}


# ============================================================================
# NEXT SCENE
# ============================================================================

// Phase 1: Zod Defensive Schema Contracts
import { z } from 'zod';
import { generateObject } from 'ai';
import { openai } from '@ai-sdk/openai';

export const AnalyticsPayloadSchema = z.object({
  metricName: z.string(),
  p99LatencyMs: z.number().positive(),
  errorRatePercent: z.number().min(0).max(100),
  recommendation: z.enum(['SCALE_UP', 'RETRY_BACKOFF', 'HEALTHY']),
});

export type AnalyticsPayload = z.infer<typeof AnalyticsPayloadSchema>;


# ============================================================================
# NEXT SCENE
# ============================================================================

// Phase 2: Type-Safe Generation & Auto-Repair
export async function generateSafeMetrics(rawLogs: string): Promise<AnalyticsPayload> {
  const { object } = await generateObject({
    model: openai('gpt-4o'),
    schema: AnalyticsPayloadSchema,
    prompt: `Extract metrics from logs: ${rawLogs}`,
    maxRetries: 3,
  });
  return object;
}


# ============================================================================
# NEXT SCENE
# ============================================================================

// Phase 2: Type-Safe Generation & Auto-Repair
export async function generateSafeMetrics(rawLogs: string): Promise<AnalyticsPayload> {
  const { object } = await generateObject({
    model: openai('gpt-4o'),
    schema: AnalyticsPayloadSchema,
    prompt: `Extract metrics from logs: ${rawLogs}`,
    maxRetries: 3,
  });
  return object;
}


# ============================================================================
# NEXT SCENE
# ============================================================================

// Phase 1: Zod Defensive Schema Contracts
import { z } from 'zod';
import { generateObject } from 'ai';
import { openai } from '@ai-sdk/openai';

export const AnalyticsPayloadSchema = z.object({
  metricName: z.string(),
  p99LatencyMs: z.number().positive(),
  errorRatePercent: z.number().min(0).max(100),
  recommendation: z.enum(['SCALE_UP', 'RETRY_BACKOFF', 'HEALTHY']),
});

export type AnalyticsPayload = z.infer<typeof AnalyticsPayloadSchema>;
