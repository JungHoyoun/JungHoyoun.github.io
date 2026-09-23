---
layout: home
title: Hoyoun Jung
description: Hoyoun Jung is an AI Research Scientist focused on LLM pretraining, training systems, and GPU kernels.
---

<header class="home-nav" aria-label="Primary navigation">
  <a class="home-wordmark" href="{{ '/' | relative_url }}">Hoyoun Jung<span class="home-mark" aria-hidden="true"></span></a>
  <nav class="home-nav-links" aria-label="Sections">
    <a href="#about">About</a>
    <a href="#writing">Writing</a>
    <a href="#work">Work</a>
    <a href="#now-title">Now</a>
  </nav>
</header>

<main class="home-content">
  <section id="about" aria-labelledby="about-title">
    <div class="home-identity">
      <img class="home-avatar" src="{{ '/assets/img/avatar.png' | relative_url }}" alt="Hoyoun Jung">
      <div>
        <h1 id="about-title">Hoyoun Jung</h1>
        <p class="home-role">AI Research Scientist / Research Engineer</p>
        <div class="home-socials" aria-label="External links">
          <a href="https://github.com/JungHoyoun">GitHub</a>
          <a href="https://www.linkedin.com/in/hoyoun-jung-0859421b7">LinkedIn</a>
          <a href="https://scholar.google.com/citations?user=hfYf6nAAAAAJ&amp;hl=en">Scholar</a>
          <a href="mailto:ghdbsl98@gmail.com">Email</a>
        </div>
      </div>
    </div>

    <div class="home-intro">
      <p>I work on large language model pretraining and the systems that make training reliable, efficient, and scalable.</p>
      <p>My interests include mixture-of-experts models, distributed training, GPU kernels, and evaluation workflows. I use experiments, profiling, and code to turn bottlenecks into reusable engineering and research evidence.</p>
    </div>
  </section>

  <section id="writing" class="home-section" aria-labelledby="writing-title">
    <h2 id="writing-title">Writing</h2>
    {% assign notes = site.posts | where_exp: "post", "post.url contains '/notes/'" %}
    {% if notes.size > 0 %}
    <ul>
      {% for post in notes %}
      <li>
        <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
        {% if post.date %}<span class="home-work-meta"> ({{ post.date | date: "%b %Y" }})</span>{% endif %}
      </li>
      {% endfor %}
    </ul>
    {% else %}
    <p class="home-empty">No public writing yet. New posts will appear here when they are published from Obsidian.</p>
    {% endif %}
  </section>

  <section id="work" class="home-section" aria-labelledby="work-title">
    <h2 id="work-title">Selected Work</h2>
    <ul class="home-work-list">
      <li>
        <strong><a href="https://github.com/Dao-AILab/quack/pull/143">Non-Gated MoE Backward Fusion in QuACK</a></strong>
        <span class="home-work-meta">CUDA / CUTLASS · 2026</span>
      </li>
      <li>
        <strong><a href="https://github.com/NVIDIA/Megatron-LM/pull/3345">Fused Linear Cross Entropy in Megatron-LM</a></strong>
        <span class="home-work-meta">Training systems / memory efficiency · 2026</span>
      </li>
      <li>
        <strong><a href="https://github.com/JungHoyoun">GitHub</a></strong>
        <span class="home-work-meta">Code, experiments, and public contributions</span>
      </li>
    </ul>
  </section>

  <section class="home-section" aria-labelledby="now-title">
    <h2 id="now-title">Now</h2>
    <p>Building stronger evidence in LLM training systems, GPU optimization, and technical writing.</p>
  </section>
</main>

<footer class="home-footer">
  Last updated {{ site.time | date: "%B %Y" }} · © Hoyoun Jung
</footer>
