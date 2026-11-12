# Phase 1: Fixed-Window 77-Token CLIP Padding & Causal Masking
import torch
import torch.nn as nn

class CLIPTextConditioner(nn.Module):
    def __init__(self, vocab_size: int = 49408, embed_dim: int = 768, max_len: int = 77):
        super().__init__()
        self.max_len = max_len
        self.token_emb = nn.Embedding(vocab_size, embed_dim)
        self.pos_emb = nn.Parameter(torch.randn(1, max_len, embed_dim) * 0.02)
        self.ln_final = nn.LayerNorm(embed_dim)

    def pad_or_truncate(self, token_ids: list[int], bos_id: int = 49406, eos_id: int = 49407) -> torch.Tensor:
        seq = [bos_id] + token_ids[: self.max_len - 2] + [eos_id]
        padded = seq + [eos_id] * (self.max_len - len(seq))
        return torch.tensor(padded, dtype=torch.long).unsqueeze(0)

# Phase 2: Contextual Token Sequence & Pooled EOS Vector Extraction
    def encode_prompt(self, input_ids: torch.Tensor) -> tuple[torch.Tensor, torch.Tensor]:
        hidden = self.token_emb(input_ids) + self.pos_emb[:, : input_ids.size(1), :]
        contextual = self.ln_final(hidden)
        eos_indices = input_ids.argmax(dim=-1)
        pooled = contextual[torch.arange(contextual.size(0)), eos_indices]
        return contextual, pooled

# Phase 3: Classifier-Free Guidance with Negative Prompt Extrapolation
def apply_negative_prompt_cfg(
    eps_pos: torch.Tensor,
    eps_neg: torch.Tensor,
    guidance_scale: float = 7.5,
    rescale_phi: float = 0.7,
) -> torch.Tensor:
    guided = eps_neg + guidance_scale * (eps_pos - eps_neg)
    std_pos = eps_pos.std(dim=list(range(1, eps_pos.ndim)), keepdim=True)
    std_cfg = guided.std(dim=list(range(1, guided.ndim)), keepdim=True).clamp(min=1e-6)
    rescaled = guided * (std_pos / std_cfg)
    return rescale_phi * rescaled + (1.0 - rescale_phi) * guided
