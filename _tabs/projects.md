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

- Fused non-gated MoE backward scaling and reduction into CUTLASS `gemm_dact`, covering regular and varlen-M paths.
- Observed up to `1.25x` dgrad speedup and `22%` memory reduction compared with a `torch.compile` baseline on the Qwen-30B-A3B configuration.

## Fused Linear Cross Entropy in Megatron-LM

[PR #3345](https://github.com/NVIDIA/Megatron-LM/pull/3345) / 2026.01

- Implemented Hopper fused linear cross entropy with split GEMM and online cross entropy, avoiding materialized vocabulary logits.
- Observed `1.02x` speedup and `72%` activation-memory reduction against the Triton baseline on the benchmark configuration.
