# Ollama Generation Workflow

The project uses the Python `ollama` package as the model client wrapper. Direct HTTP calls through `requests` are intentionally avoided.

Ollama removes most of the operational friction around running local models: model loading, local serving, and request handling are hidden behind a simple local API. For this project, the generator only needs to call that API through the Python `ollama` package.

The important point is that Ollama is used as a stable local inference service, not as an interactive chat tool. The generator owns dataset loading, prompt assembly, file output, and logging. Ollama owns model loading, inference execution, and response handling. This boundary keeps reruns and hardware changes from affecting the generator's core logic.

## Split Pages

- [Ollama Installation and Source Build](ollama-install.md): source builds without full sudo privileges, CPU/CUDA/MLX backends, llama.cpp / GGML, and native payload layout.
- [Agent Generation Flow](agent.md): how the generator calls Ollama, organizes prompts, uses prompt reuse, and handles failures.

## Model Options

Current generation options:

- model: `gpt-oss:120b`
- local runtime target: q4km-style deployment
- Easy think mode: `low`
- Medium think mode: `medium`
- Hard think mode: `high`
- context length: `128k`, actually `131_072` tokens
- max output tokens: `100_000`
- temperature: `0.1`
- retry limit: `3`

Parameter intent:

- `gpt-oss:120b` is used because the project needs algorithm knowledge and correct submission shapes across many languages.
- `128k / 131_072` context leaves enough room for statements, examples, constraints, hints, and optional editorial references.
- `100_000` max output tokens is a per-language ceiling, preventing long or complex outputs from being truncated too early.
- `0.1` temperature reduces randomness and keeps repeated runs stable.
- Think mode increases with problem difficulty so reasoning budget is spent where it matters.

## Local Hardware Context

The tested local workstation is an Apple M2 Ultra machine with:

- 24 CPU cores
- 76 GPU cores
- 192 GB unified memory

An alternate compute target is a single Ollama node with 2x NVIDIA H100 GPUs. This serves the same project workflow: one node runs Ollama, receives the problem/language prompts, and writes generated solutions through the same repository tooling.

Under the tested local setup, throughput can reach about 100 tokens per second. This matters because the project generates solutions for many languages per problem, so local throughput directly affects full-dataset generation time.

For Apple Silicon, the documentation should mention MLX and MPS-oriented acceleration paths. For NVIDIA hardware, the 2x H100 node is the high-throughput option. The exact runtime choice can depend on the local Ollama build and model packaging, but the site should make it clear that this workflow is intended for high-memory local inference rather than a remote hosted API.

## Why Local Generation Fits This Project

The project repeatedly sends a stable system prompt, a reusable problem prompt, and small language-specific prompts. This makes local generation attractive because:

- the same problem context is reused across many languages,
- the workflow can run without sending dataset content to a hosted API,
- failed languages can be retried locally,
- generated files can be resumed by checking existing Markdown output.

