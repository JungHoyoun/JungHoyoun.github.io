---
layout: page
title: 프로젝트
permalink: /ko/projects/
---

<div style="display:flex;justify-content:flex-end;gap:.35rem;margin:-.25rem 0 .8rem;font-size:.78rem;letter-spacing:.02em;text-transform:uppercase" aria-label="Language switch">
  <a href="/projects/" style="border:1px solid var(--main-border-color);border-radius:999px;padding:.12rem .48rem">EN</a>
  <span style="border:1px solid var(--main-border-color);border-radius:999px;padding:.12rem .48rem;font-weight:700">KO</span>
</div>

## Non-Gated MoE Backward Fusion in QuACK

[PR #143](https://github.com/Dao-AILab/quack/pull/143) / 2026.06

- non-gated MoE backward의 scaling과 reduction을 CUTLASS `gemm_dact`에 fusion하고 regular 및 varlen-M 경로 지원
- Qwen-30B-A3B 설정 기준 `torch.compile` 대비 최대 1.25x dgrad speedup 및 22% memory reduction 확인

## Fused Linear Cross Entropy in Megatron-LM

[PR #3345](https://github.com/NVIDIA/Megatron-LM/pull/3345) / 2026.01

- split GEMM과 online cross entropy를 결합한 Hopper용 fused linear cross entropy를 구현해 전체 vocabulary logits 생성을 방지
- benchmark 설정에서 Triton baseline 대비 1.02x speedup 및 72% activation-memory reduction 확인
