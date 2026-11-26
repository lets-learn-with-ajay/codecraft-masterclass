"""
Unit tests for Episode 27: Text Encoders at Scale
"""

import tempfile
import unittest
from pathlib import Path

from model import DualTextConditioner, PromptEmbeddingCache


class TestTextEncodersScale(unittest.TestCase):
    def setUp(self):
        self.encoder = DualTextConditioner(clip_dim=256, t5_dim=512, max_seq_len=32)

    def test_dual_encoding_dimensions(self):
        prompt = "A cinematic portrait of an astronaut exploring an ancient Martian temple, detailed reflections."
        emb = self.encoder.encode(prompt)

        # Check CLIP pooled vector
        self.assertEqual(len(emb.clip_pooled), 256)
        # Check T5 sequence length and token dimension
        self.assertEqual(len(emb.t5_sequence), 32)
        self.assertEqual(len(emb.t5_sequence[0]), 512)
        # Check attention mask
        self.assertEqual(len(emb.attention_mask), 32)
        num_tokens = len(self.encoder.tokenize(prompt))
        self.assertEqual(sum(emb.attention_mask), num_tokens)

    def test_embedding_disk_cache(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            cache = PromptEmbeddingCache(tmpdir)
            prompt = "Hyperrealistic photo of a futuristic electric sports car at night."

            # Cache miss initially
            self.assertIsNone(cache.get(prompt))

            # Encode and store
            emb = self.encoder.encode(prompt)
            cache.set(emb)

            # Cache hit
            cached_emb = cache.get(prompt)
            self.assertIsNotNone(cached_emb)
            self.assertEqual(cached_emb.prompt, prompt)
            self.assertEqual(len(cached_emb.clip_pooled), 256)
            self.assertEqual(cached_emb.attention_mask, emb.attention_mask)


if __name__ == "__main__":
    unittest.main()
