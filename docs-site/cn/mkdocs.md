# MkDocs 站点规划

文档站点应作为独立 MkDocs 工程放在 `docs-site/` 下。

## 目标

- 文档站点文件与生成器源码分离。
- 中文和英文采用平行结构。
- 导航稳定可预测。
- 结构足够简单，便于人工维护。

## 规划结构

```text
docs-site/
  mkdocs.yml
  docs/
    en/
    cn/
```

当前规划文档直接放在 `docs-site/en/` 和 `docs-site/cn/` 下。后续真正创建完整 MkDocs 工程时，可以把这些文件移动或复制到 `docs-site/docs/`。

## 导航

英文和中文导航应尽量镜像：

- Overview / 总览
- LeetCode
- Languages / 支持语言
- Ollama Workflow / Ollama 流程
- MkDocs
- GitHub Actions
- End-to-End Workflow / 端到端流程
- PRD

