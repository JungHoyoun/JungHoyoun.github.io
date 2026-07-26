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

- `squared_relu` 등 activation에 대한 non-gated MoE backward fusion 구현
- CUTLASS GEMM epilogue에 colvec scale/reduce support를 추가하여 MoE backward computation의 memory access overhead 감소
- regular 및 varlen-M `gemm_dact`의 정확성을 PyTorch float32 reference와 비교 검증
- Qwen-30B-A3B 설정 기준 `torch.compile` 대비 최대 1.25x dgrad speedup 및 22% memory reduction 확인

## Fused Linear Cross Entropy in Megatron-LM

[PR #3345](https://github.com/NVIDIA/Megatron-LM/pull/3345) / 2026.01

- CUTLASS/CuTe 스타일 kernel 작업으로 Hopper GPU용 fused linear cross entropy 경로 구현
- Linear projection과 cross entropy 경로를 fusion해 LLM pretraining 중 전체 vocabulary logits 저장 방지
- forward에서는 vocab-split online cross entropy, backward에서는 split 단위 recomputation 사용
- benchmark 설정에서 Triton baseline 대비 1.02x speedup 및 72% activation-memory reduction 확인
