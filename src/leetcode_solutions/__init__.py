"""LeetCode 多语言题解生成包。

包内模块按职责拆分：

- `dataset_loader`：读取、筛选和排序本地题目数据；
- `prompt_builder`：构造题目 prompt 和语言 prompt；
- `ollama_client`：封装 Python Ollama 调用；
- `generator`：编排断点续跑、模型调用和 Markdown 写入；
- `markdown_writer`：集中管理输出路径、Markdown 渲染和已有文件解析；
- `audit` / `resume`：复用同一套完成度判断，支持审计和续跑；
- `logger`：分流普通日志、错误日志和结构化失败记录。

这里不导出额外符号，避免包入口和内部模块形成隐式耦合。
"""
