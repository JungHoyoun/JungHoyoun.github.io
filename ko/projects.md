---
layout: page
title: 프로젝트
permalink: /ko/projects/
---

# 프로젝트

[English Projects](/projects/){: .btn .btn-outline-secondary }

## Sonic-MoE Training Optimization

on-going project / 2026.06

- SonicMoE 내 GELU/ReLU 등 non-gated MoE fused kernel 경로 지원 추가
- activation type별 forward `gemm_act`, backward `gemm_dact` dispatch 로직 수정
- Qwen-30B-A3B 설정 기준 `torch.compile` 대비 1.08x speedup 및 18% memory reduction 달성

![Sonic-MoE activation fusion](/assets/img/portfolio/sonic_quack_activation_fusion.png)

## Non-Gated MoE Backward Fusion in QuACK

PR #143 / 2026.06

- `squared_relu` 등 activation에 대한 non-gated MoE backward fusion 구현
- CUTLASS GEMM epilogue에 colvec scale/reduce support를 추가하여 MoE backward computation의 memory access overhead 감소
- Qwen-30B-A3B 설정 기준 `torch.compile` 대비 1.25x speedup 및 22% memory reduction 달성

## Fused Linear Cross Entropy in Megatron-LM

PR #3345 / 2026.01

- CUTLASS/Triton을 활용해 Hopper GPU용 fused linear cross entropy kernel 구현
- Linear projection과 cross entropy path를 fusion해 LLM pretraining 중 activation 저장 비용 감소
- Qwen-30B-A3B 설정 기준 Triton baseline 대비 1.02x speedup 및 72% memory reduction 달성

![Fused linear cross entropy memory layout](/assets/img/portfolio/fused_lce_memory_layout.png)

## LLM Pretraining System Optimization

KT Foundation LLM / 2024-2026

- Dense 및 100B급 MoE Foundation LLM에 맞춘 분산학습 설정 최적화
- TP/PP/VPP/EP/CP, batch, recomputation, communication overlap, activation memory, kernel hotspot 분석
- BPB evaluation과 Megatron-LM checkpoint native benchmark evaluation을 통해 평가 피드백 지연 감소

![Training profiler summary](/assets/img/portfolio/training_profiler_thumb.png)
