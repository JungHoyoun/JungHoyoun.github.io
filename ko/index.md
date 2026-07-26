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
[CV 보기](/ko/cv/){: .btn .btn-outline-primary }

<div class="metric-grid">
  <div class="metric"><strong>100B+ MoE</strong><span>Foundation model 사전학습 시스템</span></div>
  <div class="metric"><strong>72% memory 감소</strong><span>Fused linear cross entropy activation memory</span></div>
  <div class="metric"><strong>1.25x speedup</strong><span>Non-gated MoE backward path</span></div>
  <div class="metric"><strong>KT Foundation LLM</strong><span>사전학습 및 출시 기여</span></div>
</div>
