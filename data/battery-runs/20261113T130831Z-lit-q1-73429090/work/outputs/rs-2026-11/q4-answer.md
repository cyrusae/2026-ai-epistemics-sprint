# Q4 — GPU memory reduction for GPT-3 175B in LoRA (arXiv:2106.09685)

## Short answer

The paper **does not report a "reduction in GB" figure**. It reports the two absolute VRAM numbers, and the GB reduction is an arithmetic difference you have to compute:

> "On GPT-3 175B, we reduce the VRAM consumption during training from **1.2TB to 350GB**."
> — Sec. 4.2 "Practical Benefits and Limitations", p. 5 of arXiv:2106.09685v2 (identical wording in v1, p. 4)

So, for a table:

- **Absolute reduction: 850 GB** (1,200 GB − 350 GB, treating 1 TB = 1000 GB). If you use 1 TB = 1024 GB it is 1,228.8 − 350 = **878.8 GB**.
- **Relative reduction: ~3.4×** less VRAM (1,200 / 350 ≈ 3.43), i.e. a ~71% reduction.
- The abstract/Introduction round this to "**reduce … the GPU memory requirement by 3 times**" (abstract, p. 1), and Sec. 4.2 separately says "we reduce that VRAM usage by up to **2/3**".

⚠️ Do not write "3 GB" or "3× = 3 GB" — the "3 times" is a *factor*, not a GB quantity. There is no sentence in the paper of the form "LoRA reduces GPU memory by N GB".

## Important caveats for the methods section

1. **"1.2TB → 350GB" is total VRAM for the training setup, not per-GPU memory.** The paper gives no per-GPU figure. In v1 (Sec. 5) it states: "For GPT-3, we use 96 GPUs for fine-tuning and 24 GPUs for LoRA" — but never divides the VRAM numbers by GPU count, and model-parallel sharding makes such a division non-trivial.
2. **350 GB is also the deployment/checkpoint size**, not only training VRAM: footnote 4 says "We still need the 350GB model during deployment". So the 350 GB figure does double duty; the 1.2 TB figure is explicitly "VRAM consumption during training".
3. **The reduction comes from not storing optimizer states** for frozen weights with Adam, which is why the paper frames it as "up to 2/3" (Sec. 4.2).
4. **Version differences:** v1 (17 Jun 2021) says "we reduce the VRAM consumption from 1.2TB to 350GB"; v2 (16 Oct 2021) says "we reduce the VRAM consumption during training from 1.2TB to 350GB". Same numbers in both. v1's abstract instead says "reduce … the computation hardware requirement by 3 times"; v2's abstract says "the GPU memory requirement by 3 times".

## Suggested table wording

> LoRA reduces GPT-3 175B training VRAM from 1.2 TB to 350 GB (≈850 GB less, ~3.4× reduction) [Hu et al., 2021, §4.2].

## Sources checked

| # | Source | URL | What was read |
|---|--------|-----|----------------|
| 1 | Hu et al., "LoRA: Low-Rank Adaptation of Large Language Models", arXiv:2106.09685v2 (16 Oct 2021) | https://arxiv.org/pdf/2106.09685 | Full PDF text; Sec. 4.2, abstract, footnote 4 |
| 2 | Same paper, v1 (17 Jun 2021) | https://arxiv.org/pdf/2106.09685v1 | Full PDF text; Sec. 3.1 "Practical Benefits", Sec. 5 GPU counts |
| 3 | arXiv abstract page | https://arxiv.org/abs/2106.09685 | Abstract text, version history |

## Coverage status

- **Verified directly:** the 1.2 TB → 350 GB sentence in both v1 and v2; the "3 times" abstract claim; the "up to 2/3" claim; the 96/24 GPU counts in v1.
- **Derived (inference, not a quoted paper claim):** the 850 GB difference and the ~3.4× ratio.
- **Not found:** any per-GPU memory figure, any explicit "N GB reduction" statement, and any memory table for GPT-3 (the GPT-3 results table reports accuracy/ROUGE and trainable-parameter counts only).
