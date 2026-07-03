# 文档站点 PRD

## 目标

为本仓库建设一个基于 MkDocs 和 GitHub Actions 的双语文档站点。

## 要求

- 文档源码必须组织为英文和中文两套结构。
- 站点必须解释 LeetCode、支持语言、生成流程、MkDocs 和 GitHub Actions。
- 使用 Mermaid 图说明多文件文档结构和部署流程。
- 文档站点应可通过 GitHub Pages 部署。
- 工作流应简单、可维护、可复用。

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

