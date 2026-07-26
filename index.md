---
layout: page
title: Home
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
@media (max-width: 720px) {
  .metric-grid {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
}
</style>

<div class="page-lang-switch" aria-label="Language switch">
  <span>EN</span>
  <a href="/ko/">KO</a>
</div>

# Hoyoun Jung

<p class="hero-lede">
AI Research Engineer working on large-scale LLM pretraining systems across GPU kernels, distributed training, and evaluation pipelines.
</p>

[View Projects](/projects/){: .btn .btn-primary }
[View CV](/cv/){: .btn .btn-outline-primary }

<div class="metric-grid">
  <div class="metric"><strong>100B+ MoE</strong><span>Foundation-model pretraining systems</span></div>
  <div class="metric"><strong>72% less memory</strong><span>Fused linear cross entropy activation memory</span></div>
  <div class="metric"><strong>1.25x speedup</strong><span>Non-gated MoE backward path</span></div>
  <div class="metric"><strong>KT Foundation LLM</strong><span>Pretraining and release contribution</span></div>
</div>
