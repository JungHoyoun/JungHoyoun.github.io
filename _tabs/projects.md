---
title: Projects
icon: fas fa-microchip
order: 1
---

<div style="display:flex;justify-content:flex-end;gap:.35rem;margin:-.25rem 0 .8rem;font-size:.78rem;letter-spacing:.02em;text-transform:uppercase" aria-label="Language switch">
  <span style="border:1px solid var(--main-border-color);border-radius:999px;padding:.12rem .48rem;font-weight:700">EN</span>
  <a href="/ko/projects/" style="border:1px solid var(--main-border-color);border-radius:999px;padding:.12rem .48rem">KO</a>
</div>

## Non-Gated MoE Backward Fusion in QuACK

[PR #143](https://github.com/Dao-AILab/quack/pull/143) / 2026.06

- Implemented non-gated MoE backward fusion for activations such as `squared_relu`.
- Added colvec scale/reduce support in the CUTLASS GEMM epilogue path to reduce memory-access overhead during MoE backward computation.
- Verified regular and varlen-M `gemm_dact` correctness against PyTorch float32 references.
- Observed up to `1.25x` dgrad speedup and `22%` memory reduction compared with a `torch.compile` baseline on the Qwen-30B-A3B configuration.

## Fused Linear Cross Entropy in Megatron-LM

[PR #3345](https://github.com/NVIDIA/Megatron-LM/pull/3345) / 2026.01

- Implemented a Hopper GPU path for fused linear cross entropy using CUTLASS/CuTe-style kernel work.
- Fused the linear projection and cross entropy path to avoid storing full vocabulary logits during LLM pretraining.
- Used vocab-split online cross entropy in forward and split-wise recomputation in backward.
- Observed `1.02x` speedup and `72%` activation-memory reduction against the Triton baseline on the benchmark configuration.
