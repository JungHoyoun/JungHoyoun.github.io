---
layout: page
title: Hoyoun Jung
---

<style>
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

<p class="hero-lede">
AI Research Engineer working on large-scale LLM pretraining systems across GPU kernels, distributed training, and evaluation pipelines.
</p>

[View Projects](/projects/){: .btn .btn-primary }
[Download CV](/assets/files/JungHoyoun_CV_EN.pdf){: .btn .btn-outline-primary }
[Korean](/ko/){: .btn .btn-outline-secondary }

<div class="metric-grid">
  <div class="metric"><strong>100B+ MoE</strong><span>Foundation-model pretraining systems</span></div>
  <div class="metric"><strong>72% less memory</strong><span>Fused linear cross entropy activation memory</span></div>
  <div class="metric"><strong>1.25x speedup</strong><span>Non-gated MoE backward path</span></div>
  <div class="metric"><strong>KT Foundation LLM</strong><span>Pretraining and release contribution</span></div>
</div>

## What I Work On

- Training-system optimization for dense and MoE foundation models.
- CUDA, Triton, CUTLASS/CuTe kernel paths integrated into real training stacks.
- Profiling-driven improvements across communication, memory, bandwidth, and kernel hotspots.
- Evaluation workflows that shorten the loop between experiments, quality checks, and training recipes.

## Selected Work
{: .work-list }

### Non-gated MoE activation fusion

Implemented and benchmarked a fused backward path for non-gated MoE activations such as `squared_relu`, reducing separate PyTorch operations and memory traffic. The targeted dgrad path reached up to `1.25x` speedup against a `torch.compile` baseline.

### Fused linear cross entropy for Megatron-LM

Implemented a Hopper-oriented fused linear cross entropy path to avoid materializing full vocabulary logits during LLM pretraining. In the benchmark configuration, the work reduced activation memory by `72%` against the Triton baseline.

### Foundation-model pretraining systems

Worked on KT Foundation LLM pretraining, including dense and 100B+ scale MoE training setup, distributed configuration tuning, profiling-led bottleneck analysis, and native evaluation workflows for faster quality feedback.

## Availability

Open to AI Research Engineer roles around LLM pretraining, training systems, GPU kernels, and efficient model-development infrastructure.
