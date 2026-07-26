---
title: Projects
icon: fas fa-microchip
order: 1
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
  <span style="border:1px solid var(--main-border-color);border-radius:999px;padding:.12rem .48rem;font-weight:700">EN</span>
  <a href="/ko/projects/" style="border:1px solid var(--main-border-color);border-radius:999px;padding:.12rem .48rem">KO</a>
</div>

<section class="project-entry">
  <div>
    <h2>Non-Gated MoE Backward Fusion in QuACK</h2>
    <p><a href="https://github.com/Dao-AILab/quack/pull/143">PR #143</a> / 2026.06</p>
    <ul>
      <li>Fused non-gated MoE backward scaling and reduction into CUTLASS <code>gemm_dact</code>, covering regular and varlen-M paths.</li>
      <li>Observed up to <code>1.25x</code> dgrad speedup and <code>22%</code> memory reduction compared with a <code>torch.compile</code> baseline on the Qwen-30B-A3B configuration.</li>
    </ul>
  </div>
  <a class="project-thumb" href="https://github.com/Dao-AILab/quack/pull/143" aria-label="Open QuACK PR #143">
    <img src="/assets/img/portfolio/sonic_quack_activation_fusion.png" alt="Non-gated MoE backward fusion diagram">
  </a>
</section>

<section class="project-entry">
  <div>
    <h2>Fused Linear Cross Entropy in Megatron-LM</h2>
    <p><a href="https://github.com/NVIDIA/Megatron-LM/pull/3345">PR #3345</a> / 2026.01</p>
    <ul>
      <li>Implemented Hopper fused linear cross entropy with split GEMM and online cross entropy, avoiding materialized vocabulary logits.</li>
      <li>Observed <code>1.02x</code> speedup and <code>72%</code> activation-memory reduction against the Triton baseline on the benchmark configuration.</li>
    </ul>
  </div>
  <a class="project-thumb" href="https://github.com/NVIDIA/Megatron-LM/pull/3345" aria-label="Open Megatron-LM PR #3345">
    <img src="/assets/img/portfolio/fused_lce_memory_layout.png" alt="Fused linear cross entropy memory layout diagram">
  </a>
</section>
