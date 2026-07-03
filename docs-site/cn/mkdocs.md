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
  index.md
  en/
  cn/
```

当前站点直接使用 `docs-site/` 作为 `docs_dir`。根目录 `index.md` 是语言入口，`en/` 和 `cn/` 是双语正文目录。这样结构更扁平，GitHub Pages 项目根路径也能直接生成首页。

`site_dir` 指向 `../docs-site-build`，构建产物不进入文档源码目录，并通过 `.gitignore` 排除。

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

## 设计意图

MkDocs 只负责把 Markdown 发布成静态站点，不参与题解生成。这样 GitHub Actions 可以使用轻量 Python 环境构建文档，而不需要安装 Ollama、下载模型或读取本地数据集。

中英文页面保持平行命名，是为了让每次修改都能明确知道是否需要同步翻译。根首页只做入口，不承载复杂内容，避免中英文导航在项目根路径上混在一起。
