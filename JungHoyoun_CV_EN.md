# Hoyoun Jung

AI Research Engineer / LLM Pretraining & Training Systems Optimization

- Email: ghdbsl98@gmail.com
- LinkedIn: <https://www.linkedin.com/in/hoyoun-jung-0859421b7>
- GitHub: <https://github.com/JungHoyoun>

## Summary

I am an AI Research Engineer working across LLM pretraining and training systems.

My work focuses on improving GPU kernels, distributed training, evaluation pipelines, and experiment automation to secure more useful compute under limited resources and shorten experiment-evaluation iteration cycles.

Recently, I have been interested in model architectures and training algorithms that account for hardware characteristics, as well as methodologies for using AI to accelerate AI research and development.

## Experience

### KT LanguageAI Team

AI Research Scientist / Research Engineer

2024.08 - Present

Responsible for pretraining design, stabilization, evaluation pipelines, and training-system optimization for dense and 100B+ scale MoE Foundation LLMs.

- Led and contributed to KT Foundation LLM "Mi:dm" pretraining and release.
- Achieved the top Korean-language model performance in the sub-40B small-to-mid-size model category based on AAII Index v3.0.
- Improved MoE training speed by 40% through CUDA/Triton kernel implementation and distributed-training bottleneck optimization.

Tech: PyTorch, Megatron-LM, CUDA, Triton, Distributed Training, Low Precision Training

### NAVER Cloud Vision Understanding Team

AI Engineer Intern

2024.01 - 2024.07

Responsible for improving HyperCLOVA-V multimodal data pipelines, training the vision encoder, and designing multimodal benchmarks.

- Contributed to the HyperCLOVA-V release, achieving approximately 90% of GPT-4V-level performance on Korean and multimodal benchmarks.
- Designed multimodal data collection, cleaning, and synthesis pipelines and ran data ablation experiments.
- Designed benchmarks and developed an evaluation viewer for model-performance analysis.

Tech: PyTorch, FSDP, Vision Language Model, Data Pipeline

## Projects

### Sonic-MoE Training Optimization

ongoing project / 2026.06

- Added support for non-gated MoE fused-kernel paths such as GELU/ReLU in Sonic-MoE.
- Updated activation-type-specific dispatch logic for forward `gemm_act` and backward `gemm_dact`.
- Achieved 1.08x speedup and 18% memory reduction compared with `torch.compile` on the Qwen-30B-A3B configuration.

### Non-Gated MoE Backward Fusion in QuACK

PR #143 / 2026.06

- Implemented non-gated MoE backward fusion for activations such as `squared_relu`.
- Added colvec scale/reduce support to the CUTLASS GEMM epilogue to reduce memory-access overhead in MoE backward computation.
- Achieved 1.25x speedup and 22% memory reduction compared with `torch.compile` on the Qwen-30B-A3B configuration.

### Fused Linear Cross Entropy in Megatron-LM

PR #3345 / 2026.01

- Implemented a Hopper GPU fused linear cross entropy kernel using CUTLASS/Triton.
- Fused the linear projection and cross entropy path to reduce activation storage cost during LLM pretraining.
- Achieved 1.02x speedup and 72% memory reduction compared with the Triton baseline on the Qwen-30B-A3B configuration.

### Emotris - Game AI Jam

Game AI School / 2022.08

- Built an emotion-aware Tetris game based on facial emotion recognition.
- Connected player facial-expression recognition results to AI features that interact with the game state.
- Won 1st place among 11 teams at the Game AI School AI game hackathon.

### Kaggle Optiver Volatility Prediction Competition

Kaggle / 2021.09

- Predicted realized volatility for individual stocks using market microstructure data.
- Developed prediction models based on LightGBM, MLP, and ensemble strategies.
- Ranked 80th out of 3,852 teams, top 2.1%, silver medal.

## Education

### Gwangju Institute of Science and Technology (GIST)

M.S., School of Integrated Technology

2022.03 - 2024.02, Gwangju

- GPA: 4.08 / 4.5
- Focus: Reinforcement Learning

### Sungkyunkwan University

B.S., Statistics

2015.03 - 2019.02, Seoul

- GPA: 3.86 / 4.5

## Publications

1. Hoyoun Jung and Kyung-Joong Kim. "Discrete Prompt Compression with Reinforcement Learning." IEEE Access. 2024.
2. Hyeon-Chang Jeon, In-Chang Baek, Cheong-mok Bae, Taehwa Park, Wonsang You, Taegwan Ha, Hoyoun Jung, Jinha Noh, Seungwon Oh, and Kyung-Joong Kim. "RaidEnv: Exploring New Challenges in Automated Content Balancing for Boss Raid Games." IEEE Transactions on Games. 2023.
3. Issac Han, Seungwon Oh, Hoyoun Jung, and Kyung-Joong Kim. "Monte Carlo and Temporal Difference Methods in Reinforcement Learning [AI-eXplained]." IEEE Computational Intelligence Magazine. 2023.
4. Hyeonchang Jeon, Songmi Oh, Wonsang You, Hoyoun Jung, and Kyung-Joong Kim. "Inferring Relationship using Theory of Mind in Press Diplomacy." ICML 2022 Workshop AI for Agent-Based Modelling. 2022.
