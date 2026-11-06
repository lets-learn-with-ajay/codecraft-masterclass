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
