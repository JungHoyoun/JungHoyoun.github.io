---
layout: page
title: Home
permalink: /ko/
---

<style>
.dynamic-title {
  display: none;
}
.page-lang-switch {
  display: flex;
  justify-content: flex-end;
  gap: 0.35rem;
  margin: -0.25rem 0 0.8rem;
  font-size: 0.78rem;
  letter-spacing: 0.02em;
  text-transform: uppercase;
}
.page-lang-switch a,
.page-lang-switch span {
  border: 1px solid var(--main-border-color);
  border-radius: 999px;
  padding: 0.12rem 0.48rem;
}
.page-lang-switch span {
  color: var(--heading-color);
  background: var(--main-bg);
  font-weight: 700;
}
.hero-lede {
  margin-top: -0.25rem;
  font-size: 1.08rem;
  color: var(--text-muted-color);
}
.metric-grid {
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 0.75rem;
  margin: 1.25rem 0 1.35rem;
}
.metric {
  border: 1px solid var(--main-border-color);
  border-radius: 8px;
  padding: 0.85rem;
  background: var(--card-bg);
}
.metric strong {
  display: block;
  font-size: 1.1rem;
  line-height: 1.15;
}
.metric span {
  display: block;
  margin-top: 0.25rem;
  color: var(--text-muted-color);
  font-size: 0.88rem;
  line-height: 1.25;
}
.work-list h3 {
  margin-top: 1.4rem;
}
@media (max-width: 720px) {
  .metric-grid {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
}
</style>

<div class="page-lang-switch" aria-label="Language switch">
  <a href="/">EN</a>
  <span>KO</span>
</div>

# 정호윤

<p class="hero-lede">
대규모 LLM 사전학습 시스템에서 GPU 커널, 분산학습, 평가 파이프라인을 함께 최적화하는 AI Research Engineer입니다.
</p>

[프로젝트 보기](/ko/projects/){: .btn .btn-primary }
[CV 다운로드](/assets/files/JungHoyoun_CV_SKT.pdf){: .btn .btn-outline-primary }

<div class="metric-grid">
  <div class="metric"><strong>100B+ MoE</strong><span>Foundation model 사전학습 시스템</span></div>
  <div class="metric"><strong>72% memory 감소</strong><span>Fused linear cross entropy activation memory</span></div>
  <div class="metric"><strong>1.25x speedup</strong><span>Non-gated MoE backward path</span></div>
  <div class="metric"><strong>KT Foundation LLM</strong><span>사전학습 및 출시 기여</span></div>
</div>

## What I Work On

- Dense 및 MoE foundation model을 위한 training-system optimization
- CUDA, Triton, CUTLASS/CuTe 기반 kernel path와 실제 training stack 통합
- communication, memory, bandwidth, kernel hotspot에 대한 profiling 기반 개선
- experiment, quality check, training recipe 사이의 feedback loop 단축

## Selected Work
{: .work-list }

### Non-gated MoE activation fusion

`squared_relu` 등 non-gated MoE activation을 위한 fused backward path를 구현하고 benchmark했습니다. 별도 PyTorch operation과 memory traffic을 줄였고, targeted dgrad path에서 `torch.compile` baseline 대비 최대 `1.25x` speedup을 확인했습니다.

### Fused linear cross entropy for Megatron-LM

LLM pretraining 중 full vocabulary logits materialization을 피하기 위해 Hopper GPU용 fused linear cross entropy path를 구현했습니다. Benchmark configuration에서 Triton baseline 대비 activation memory를 `72%` 줄였습니다.

### Foundation-model pretraining systems

KT Foundation LLM pretraining에서 dense 및 100B+ scale MoE training setup, distributed configuration tuning, profiling 기반 병목 분석, native evaluation workflow를 다뤘습니다.

## Availability

LLM pretraining, training systems, GPU kernels, efficient model-development infrastructure를 다루는 AI Research Engineer 역할에 열려 있습니다.
