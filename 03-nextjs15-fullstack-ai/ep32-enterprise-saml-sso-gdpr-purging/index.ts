// Phase 1: SAML 2.0 / OIDC Tenant Session Claims & RBAC Guard
import { z } from 'zod';

export const EnterpriseSessionSchema = z.object({
  userId: z.string().uuid(),
  tenantOrgId: z.string(),
  idpEntityId: z.string(),
  roles: z.array(z.enum(['ORG_ADMIN', 'AI_BUILDER', 'AUDITOR'])),
  mfaVerified: z.boolean(),
});

export type EnterpriseSession = z.infer<typeof EnterpriseSessionSchema>;

export function assertTenantAccess(session: EnterpriseSession, targetOrgId: string): void {
  if (!session.mfaVerified || session.tenantOrgId !== targetOrgId) {
    throw new Error('Zero-Trust SSO Guard: Cross-tenant or unverified session rejected');
  }
}

// Phase 2: Tamper-Evident SHA-256 Hash-Chained AI Audit Log
import crypto from 'crypto';

export interface AuditLogEntry {
  tenantOrgId: string;
  actorId: string;
  action: string;
  promptSha256: string;
  prevChainHash: string;
  entryHash: string;
}

export function buildChainedAuditEntry(
  tenantOrgId: string,
  actorId: string,
  action: string,
  rawPrompt: string,
  prevChainHash: string
): AuditLogEntry {
  const promptSha256 = crypto.createHash('sha256').update(rawPrompt).digest('hex');
  const payload = `${tenantOrgId}:${actorId}:${action}:${promptSha256}:${prevChainHash}`;
  const entryHash = crypto.createHash('sha256').update(payload).digest('hex');
  return { tenantOrgId, actorId, action, promptSha256, prevChainHash, entryHash };
}

// Phase 3: GDPR Right-to-Erasure Cascading Purge (Relational + pgvector)
'use server';
import { db } from '@/lib/postgres';

export async function executeGdprRightToErasure(tenantOrgId: string, subjectUserId: string) {
  await db.query('BEGIN');
  try {
    await db.query('DELETE FROM ai_vector_embeddings WHERE tenant_id = $1 AND user_id = $2', [tenantOrgId, subjectUserId]);
    await db.query('DELETE FROM chat_messages WHERE tenant_id = $1 AND user_id = $2', [tenantOrgId, subjectUserId]);
    await db.query('COMMIT');
    return { status: 'GDPR_PURGED', subjectUserId, purgedVectors: true };
  } catch (err) {
    await db.query('ROLLBACK');
    throw err;
  }
}
