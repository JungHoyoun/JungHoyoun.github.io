---
layout: page
title: 프로젝트
permalink: /ko/projects/
---

<style>
.project-entry {
  display: grid;
  grid-template-columns: minmax(0, 1fr) 220px;
  gap: 1.5rem;
  align-items: start;
  margin-bottom: 2.5rem;
}

.project-entry h2 {
  margin-top: 0;
}

.project-thumb {
  display: block;
  margin-top: .25rem;
  border: 1px solid var(--main-border-color);
  border-radius: .5rem;
  overflow: hidden;
  background: #fff;
}

.project-thumb img {
  display: block;
  width: 100%;
  height: 150px;
  object-fit: contain;
}

@media (max-width: 767px) {
  .project-entry {
    grid-template-columns: 1fr;
    gap: .75rem;
  }

  .project-thumb {
    max-width: 320px;
  }

  .project-thumb img {
    height: auto;
  }
}
</style>

<div style="display:flex;justify-content:flex-end;gap:.35rem;margin:-.25rem 0 .8rem;font-size:.78rem;letter-spacing:.02em;text-transform:uppercase" aria-label="Language switch">
  <a href="/projects/" style="border:1px solid var(--main-border-color);border-radius:999px;padding:.12rem .48rem">EN</a>
  <span style="border:1px solid var(--main-border-color);border-radius:999px;padding:.12rem .48rem;font-weight:700">KO</span>
</div>

<section class="project-entry">
  <div>
    <h2>Non-Gated MoE Backward Fusion in QuACK</h2>
    <p><a href="https://github.com/Dao-AILab/quack/pull/143">PR #143</a> / 2026.06</p>
    <ul>
      <li>non-gated MoE backward의 scaling과 reduction을 CUTLASS <code>gemm_dact</code>에 fusion하고 regular 및 varlen-M 경로 지원</li>
      <li>Qwen-30B-A3B 설정 기준 <code>torch.compile</code> 대비 최대 1.25x dgrad speedup 및 22% memory reduction 확인</li>
    </ul>
  </div>
  <a class="project-thumb" href="https://github.com/Dao-AILab/quack/pull/143" aria-label="QuACK PR #143 열기">
    <img src="/assets/img/portfolio/sonic_quack_activation_fusion.png" alt="Non-gated MoE backward fusion 다이어그램">
  </a>
</section>

<section class="project-entry">
  <div>
    <h2>Fused Linear Cross Entropy in Megatron-LM</h2>
    <p><a href="https://github.com/NVIDIA/Megatron-LM/pull/3345">PR #3345</a> / 2026.01</p>
    <ul>
      <li>split GEMM과 online cross entropy를 결합한 Hopper용 fused linear cross entropy를 구현해 전체 vocabulary logits 생성을 방지</li>
      <li>benchmark 설정에서 Triton baseline 대비 1.02x speedup 및 72% activation-memory reduction 확인</li>
    </ul>
  </div>
  <a class="project-thumb" href="https://github.com/NVIDIA/Megatron-LM/pull/3345" aria-label="Megatron-LM PR #3345 열기">
    <img src="/assets/img/portfolio/fused_lce_memory_layout.png" alt="Fused linear cross entropy memory layout 다이어그램">
  </a>
</section>
