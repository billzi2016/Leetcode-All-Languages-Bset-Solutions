# Ollama 生成流程

项目使用 Python `ollama` 包作为模型客户端封装，不直接用 `requests` 调 HTTP。

Ollama 把本地模型运行里麻烦的部分基本封装掉了：模型加载、本地服务和请求处理都通过一个简单的本地 API 暴露出来。对本项目来说，生成器只需要通过 Python `ollama` 包调用这个 API。

这里的重点不是把 Ollama 当成聊天工具使用，而是把它当成稳定的本地推理服务。题解生成器负责读取数据、拼 prompt、写文件和记录日志；Ollama 负责模型加载、推理执行和流式响应。这样边界清楚，后续更换机器或重跑失败项时不需要改生成器主体逻辑。

## 拆分页面

- [Ollama 安装和源码编译](ollama-install.md): 服务器无 sudo 权限时的源码编译、CPU/CUDA/MLX backend、llama.cpp / GGML 和 native payload。
- [Agent 生成流程](agent.md): 生成器如何调用 Ollama、如何组织 prompt、如何利用 prompt 复用、如何处理失败。

## 模型参数

当前生成参数：

- 模型：`gpt-oss:120b`
- 本地运行目标：q4km 风格部署
- Easy think 模式：`low`
- Medium think 模式：`medium`
- Hard think 模式：`high`
- 上下文长度：`128k`，实际为 `131_072` tokens
- 最大输出 tokens：`100_000`
- 温度：`0.1`
- 重试次数：`3`

参数意图：

- `gpt-oss:120b` 用于覆盖多语言 LeetCode 题解，要求模型既熟悉算法又熟悉各语言提交入口。
- `128k / 131_072` 上下文给题目描述、examples、constraints、hints 和 optional editorial 留出足够空间。
- `100_000` 最大输出 tokens 是单语言上限，避免复杂语言或长题解被截断。
- `0.1` 温度用于降低随机性，让同一题同一语言的输出更稳定。
- think 模式按难度递增，是为了把推理预算用在真正复杂的题上。

## 本地硬件背景

测试使用的本地工作站是 Apple M2 Ultra：

- 24 CPU 核
- 76 GPU 核
- 192 GB 统一内存

备用计算目标是单节点 2 张 NVIDIA H100 GPU 运行 Ollama。它使用同一套项目流程：一个节点运行 Ollama，接收题目和语言 prompt，并通过同一套仓库工具写入生成题解。

在测试环境中，吞吐可以达到约 100 tokens/second。这个速度对本项目很重要，因为每道题会生成多种语言的题解，本地吞吐会直接影响全量数据集的生成耗时。

在 Apple Silicon 上，文档应说明 MLX 和 MPS 相关加速路径；在 NVIDIA 硬件上，2 张 H100 的单节点是高吞吐方案。具体运行方式取决于本地 Ollama 构建和模型打包方式，但站点需要明确：这套流程面向高内存本地推理，而不是远程托管 API。

## 为什么适合本地生成

本项目反复发送稳定的 system prompt、可复用的 problem prompt，以及很小的 language prompt。本地生成适合这个项目，因为：

- 同一道题的上下文会在多种语言之间复用；
- 数据集内容不需要发送到远程 API；
- 失败语言可以在本地重试；
- 生成文件可以通过已有 Markdown 输出断点续跑。

