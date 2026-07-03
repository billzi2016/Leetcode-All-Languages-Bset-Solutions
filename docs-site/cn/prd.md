# 文档站点 PRD

## 目标

为本仓库建设一个基于 MkDocs 和 GitHub Actions 的双语文档站点。

文档站点不只是项目介绍页，而是运行手册。它需要让读者理解为什么数据文件不进 Git、为什么 prompt 被拆成三层、为什么生成顺序是 Easy 到 Hard、为什么日志要拆分，以及 GitHub Pages 只负责发布文档而不负责跑模型。

## 要求

- 文档源码必须组织为英文和中文两套结构。
- 站点必须解释 LeetCode、支持语言、生成流程、MkDocs 和 GitHub Actions。
- 使用 Mermaid 图说明多文件文档结构和部署流程。
- 文档站点应可通过 GitHub Pages 部署。
- 工作流应简单、可维护、可复用。
- 文档必须说明全量生成的运行入口、tmux 使用方式、依赖安装位置和取消方式。
- 文档必须说明 stdout、stderr、failures 三类日志的分工。
- 文档必须说明生成器和文档站点的边界：生成器依赖本地 Ollama，GitHub Actions 只部署文档。

## 设计意图

- 双语目录放在 `docs-site/cn/` 和 `docs-site/en/`，避免中英文内容互相穿插，后续新增页面也能保持清晰。
- 根目录 `docs-site/index.md` 只做语言入口，保证 GitHub Pages 项目根路径可以打开。
- `workflow.md` 负责串联数据、prompt、Ollama、输出、日志和部署，避免每个页面只讲局部。
- `ollama.md` 负责解释本地推理和服务器源码编译，让读者知道模型服务不是 GitHub Actions 的职责。
- `languages.md` 用 LeetCode 1 展示提交入口，确保读者理解最终代码必须保留 starter code 形态。

## 交付物

- `docs-site/en/` 下的英文文档。
- `docs-site/cn/` 下的中文文档。
- MkDocs 规划文档。
- GitHub Actions 规划文档。
- Mermaid 工作流图。

## 验收标准

- 存在英文和中文文件夹。
- 两种语言具备对应主题文件。
- LeetCode、语言、Ollama 流程、MkDocs、GitHub Actions 和端到端流程均有说明。
- Mermaid 图能在兼容 Markdown 的查看器中渲染。
- 文档能指导后续真正实现 MkDocs + GitHub Actions。
- 项目根路径能打开文档首页，并能进入中文和英文页面。
- 读者能根据文档启动 tmux 全量生成、查看进度、取消任务并定位失败日志。
