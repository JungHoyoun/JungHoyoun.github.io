---
icon: fas fa-folder-open
order: 4
---

# Portfolio

[Download PDF Portfolio](/assets/files/JungHoyoun_Portfolio_SKT.pdf){: .btn .btn-primary }

## LLM Pretraining & Training Systems Portfolio

This portfolio highlights systems-heavy AI research work across MoE kernel paths, fused language-model objectives, and pretraining feedback loops.

## Case Studies

### 1. Non-gated MoE activation fusion

Sonic-MoE and QuACK already had efficient paths for gated activation families such as SwiGLU. Non-gated activation families required separate operations for activation gradients, per-token router score scaling, and router-score gradient reduction.

The work extended the fast backward path so non-gated activations could apply per-token scaling and reduction inside the fused kernel path. This reduced HBM traffic and kernel-launch overhead.

**Result:** up to `1.25x` dgrad speedup, `22%` memory reduction in the targeted backward path, and `1.08x` end-to-end MoE kernel speedup in the Sonic-MoE integration setting.

![Sonic-MoE activation fusion](/assets/img/portfolio/sonic_quack_activation_fusion.png)

### 2. Fused linear cross entropy

LLM pretraining with large vocabularies can spend significant activation memory storing full logits from the LM head before cross entropy. The fused path avoids keeping the full logits tensor in HBM by computing cross entropy over vocabulary splits and recomputing partial logits during backward.

**Result:** on the Qwen-style 30B-A3B benchmark shape, the work reduced peak activation memory substantially and showed `72%` activation-memory reduction against the Triton baseline.

![Fused linear cross entropy memory layout](/assets/img/portfolio/fused_lce_memory_layout.png)

### 3. Pretraining system optimization

Large-scale training requires coordinated decisions across parallelism strategy, batch configuration, recomputation, communication overlap, and evaluation design. The work used profiler and Nsight traces to diagnose bottlenecks and built evaluation workflows that reduced conversion overhead between checkpoints and benchmark feedback.

**Result:** more stable training operations, faster evaluation feedback, and better iteration speed for foundation-model training decisions.

![Training profiler summary](/assets/img/portfolio/training_profiler_thumb.png)
