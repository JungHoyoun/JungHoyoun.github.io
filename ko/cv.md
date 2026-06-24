---
layout: page
title: 한국어 CV
permalink: /ko/cv/
---

# 정호윤

<div style="display:flex;justify-content:flex-end;gap:.35rem;margin:-.25rem 0 .8rem;font-size:.78rem;letter-spacing:.02em;text-transform:uppercase" aria-label="Language switch">
  <a href="/cv/" style="border:1px solid var(--main-border-color);border-radius:999px;padding:.12rem .48rem">EN</a>
  <span style="border:1px solid var(--main-border-color);border-radius:999px;padding:.12rem .48rem;font-weight:700">KO</span>
</div>

AI Research Engineer / LLM Pretraining & Training Systems Optimization

[PDF 다운로드](/assets/files/JungHoyoun_CV_SKT.pdf){: .btn .btn-primary }

## 연락처

- Email: <ghdbsl98@gmail.com>
- LinkedIn: <https://www.linkedin.com/in/hoyoun-jung-0859421b7>
- GitHub: <https://github.com/JungHoyoun>

## Summary

LLM pretraining과 training systems를 함께 다루는 AI Research Engineer입니다.

GPU kernel, 분산학습 최적화, 평가 파이프라인, 실험 자동화를 개선하며 제한된 자원에서 더 많은 연산량을 확보하고 실험-평가 반복 속도를 높이는 데 집중해왔습니다.

최근에는 하드웨어 특성을 고려한 모델 아키텍처·학습 알고리즘, AI가 AI 연구 개발을 가속하는 방법론에 관심이 있습니다.

## Experience

### KT LanguageAI Team

AI Research Scientist / Research Engineer  
2024.08 - 재직 중

Dense 및 100B+급 MoE Foundation LLM의 사전학습 설계, 안정화, 평가 파이프라인, 학습 시스템 최적화 담당

- KT Foundation LLM '믿음' 사전학습 주도 및 출시 기여
- AAII Index v3.0 기준 40B 미만 중소형 모델 부문 한국어 모델 최고 성능 달성
- CUDA/Triton kernel 구현, 분산학습 병목 최적화로 MoE 학습 속도 40% 개선

Tech: PyTorch, Megatron-LM, CUDA, Triton, Distributed Training, Low Precision Training

### NAVER Cloud Vision Understanding Team

AI Engineer Intern  
2024.01 - 2024.07

HyperCLOVA-V 멀티모달 데이터 파이프라인 개선, vision encoder 학습, multimodal benchmark 설계 담당

- HyperCLOVA-V 출시, 한국어 및 multimodal benchmark 기준 GPT-4V 대비 약 90% 수준 성능 달성
- Multimodal data 수집, 정제 및 합성 등 데이터 파이프라인 설계 및 ablation 실험
- 모델 성능 분석을 위한 각종 benchmark 설계 및 evaluation viewer 개발

Tech: PyTorch, FSDP, Vision Language Model, Data Pipeline

## Projects

### Sonic-MoE Training Optimization

on-going project / 2026.06

- SonicMoE 내 GELU/ReLU 등 non-gated MoE fused kernel 경로 지원 추가
- activation type별 forward `gemm_act`, backward `gemm_dact` dispatch 로직 수정
- Qwen-30B-A3B 설정 기준 `torch.compile` 대비 1.08x speedup 및 18% memory reduction 달성

### Non-Gated MoE Backward Fusion in QuACK

PR #143 / 2026.06

- `squared_relu` 등 activation에 대한 non-gated MoE backward fusion 구현
- CUTLASS GEMM epilogue에 colvec scale/reduce support를 추가하여 MoE backward computation의 memory access overhead 감소
- Qwen-30B-A3B 설정 기준 `torch.compile` 대비 1.25x speedup 및 22% memory reduction 달성

### Fused Linear Cross Entropy in Megatron-LM

PR #3345 / 2026.01

- CUTLASS/Triton을 활용해 Hopper GPU용 fused linear cross entropy kernel 구현
- Linear projection과 cross entropy path를 fusion해 LLM pretraining 중 activation 저장 비용 감소
- Qwen-30B-A3B 설정 기준 Triton baseline 대비 1.02x speedup 및 72% memory reduction 달성

### Emotris - Game AI Jam

Game AI School / 2022.08

- Facial emotion recognition 기반 emotion-aware Tetris 게임 제작
- 플레이어 표정 인식 결과를 게임 상태와 상호작용하는 AI 기능으로 연결
- Game AI School AI game hackathon 총 11팀 중 1위

### Kaggle Optiver Volatility Prediction Competition

Kaggle / 2021.09

- Market microstructure data 기반 개별 주식 realized volatility 예측
- LightGBM, MLP, ensemble strategy 기반 예측 모델 개발
- 총 3,852팀 중 80위, 상위 2.1%, 은메달 달성

## Education

### Gwangju Institute of Science and Technology (GIST)

석사, 융합기술학제학부  
2022.03 - 2024.02, 광주

- GPA: 4.08 / 4.5
- 세부전공: Reinforcement Learning

### Sungkyunkwan University

학사, 통계학과  
2015.03 - 2019.02, 서울

- GPA: 3.86 / 4.5

## Publications

1. Hoyoun Jung and Kyung-Joong Kim. "Discrete Prompt Compression with Reinforcement Learning." IEEE Access. 2024.
2. Hyeon-Chang Jeon, In-Chang Baek, Cheong-mok Bae, Taehwa Park, Wonsang You, Taegwan Ha, Hoyoun Jung, Jinha Noh, Seungwon Oh, and Kyung-Joong Kim. "RaidEnv: Exploring New Challenges in Automated Content Balancing for Boss Raid Games." IEEE Transactions on Games. 2023.
3. Issac Han, Seungwon Oh, Hoyoun Jung, and Kyung-Joong Kim. "Monte Carlo and Temporal Difference Methods in Reinforcement Learning [AI-eXplained]." IEEE Computational Intelligence Magazine. 2023.
4. Hyeonchang Jeon, Songmi Oh, Wonsang You, Hoyoun Jung, and Kyung-Joong Kim. "Inferring Relationship using Theory of Mind in Press Diplomacy." ICML 2022 Workshop AI for Agent-Based Modelling. 2022.
