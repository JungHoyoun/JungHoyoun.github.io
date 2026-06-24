---
title: Projects
icon: fas fa-microchip
order: 2
---

# Projects

<div style="display:flex;justify-content:flex-end;gap:.35rem;margin:-.25rem 0 .8rem;font-size:.78rem;letter-spacing:.02em;text-transform:uppercase" aria-label="Language switch">
  <span style="border:1px solid var(--main-border-color);border-radius:999px;padding:.12rem .48rem;font-weight:700">EN</span>
  <a href="/ko/projects/" style="border:1px solid var(--main-border-color);border-radius:999px;padding:.12rem .48rem">KO</a>
</div>

## Sonic-MoE Training Optimization

Ongoing project / 2026.06

- Added support for non-gated MoE fused-kernel paths such as GELU/ReLU-style activation families.
- Updated activation-specific forward `gemm_act` and backward `gemm_dact` dispatch logic.
- Observed `1.08x` speedup and `18%` memory reduction compared with a `torch.compile` baseline on the Qwen-30B-A3B configuration.

![Sonic-MoE activation fusion](/assets/img/portfolio/sonic_quack_activation_fusion.png)

## Non-Gated MoE Backward Fusion in QuACK

PR #143 / 2026.06

- Implemented non-gated MoE backward fusion for activations such as `squared_relu`.
- Added colvec scale/reduce support in the CUTLASS GEMM epilogue path to reduce memory-access overhead during MoE backward computation.
- Verified regular and varlen-M `gemm_dact` correctness against PyTorch float32 references.
- Observed up to `1.25x` dgrad speedup and `22%` memory reduction compared with a `torch.compile` baseline on the Qwen-30B-A3B configuration.

## Fused Linear Cross Entropy in Megatron-LM

PR #3345 / 2026.01

- Implemented a Hopper GPU path for fused linear cross entropy using CUTLASS/CuTe-style kernel work.
- Fused the linear projection and cross entropy path to avoid storing full vocabulary logits during LLM pretraining.
- Used vocab-split online cross entropy in forward and split-wise recomputation in backward.
- Observed `1.02x` speedup and `72%` activation-memory reduction against the Triton baseline on the benchmark configuration.

![Fused linear cross entropy memory layout](/assets/img/portfolio/fused_lce_memory_layout.png)

![Fused linear cross entropy backward layout](/assets/img/portfolio/fused_lce_backward_layout.png)

## LLM Pretraining System Optimization

KT Foundation LLM / 2024-2026

- Tuned distributed training configurations for dense and 100B-scale MoE foundation models.
- Analyzed TP/PP/VPP/EP/CP, batch, recomputation, communication overlap, activation memory, and kernel hotspots.
- Integrated BPB evaluation into the training loop and built native benchmark evaluation on Megatron-LM checkpoints to reduce checkpoint-conversion overhead.

![Training memory profile](/assets/img/portfolio/training_memory_thumb.png)

![Nsight training profile](/assets/img/portfolio/training_nsys_thumb.png)

![Training profiler summary](/assets/img/portfolio/training_profiler_thumb.png)
