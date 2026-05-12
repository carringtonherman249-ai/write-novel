---
name: million-novel-writer
description: 在本地笔记本电脑与微信云托管运行的“百万字小说”写作流水线技能；支持大纲规划、分卷分章生成、角色设定一致性检查、续写与迭代。
---

# Million Novel Writer Skill（本地 + 微信云托管）

这个 skill 用于帮助你完成 **百万字长篇小说** 的工程化创作，支持两种运行方式：
- 本地笔记本（单机创作）
- 微信云托管（多人协作/API 化）

## 适用场景
- 想写 50 万～200 万字中文网文/长篇小说。
- 需要按“卷-章-场景”稳定产出。
- 需要把写作能力封装成 API，供小程序/后台调用。

## 运行模式

### 模式 A：本地笔记本
- Python 3.10+
- Ollama 或兼容 OpenAI API 的本地网关

### 模式 B：微信云托管
- Python 3.10+ 容器服务
- 通过环境变量注入模型网关密钥
- 通过 HTTP API 调用章节规划/初始化能力

## 目录约定

```text
novel-project/
  00_meta/
  01_outline/
  02_characters/
  03_drafts/
  04_memory/
  05_revision/
```

## 一键初始化小说工程

```bash
python skills/million-novel-writer/scripts/init_novel_project.py --path ./novel-project
```

## 启动 API（适配微信云托管）

本 skill 内置 FastAPI 服务入口：

```bash
pip install -r skills/million-novel-writer/requirements.txt
uvicorn skills.million-novel-writer.scripts.api_server:app --host 0.0.0.0 --port 8080
```

> 注：在代码仓里目录名包含 `-` 不适合 Python import 路径。
> 实际部署时建议将目录重命名为 `million_novel_writer`，或在容器启动命令中用 `--app-dir` 指定并以文件方式启动。

推荐启动命令（无需改目录名）：

```bash
uvicorn api_server:app --app-dir skills/million-novel-writer/scripts --host 0.0.0.0 --port 8080
```

## 微信云托管部署步骤
1. 在微信云托管创建服务，运行端口设为 `8080`。
2. 将仓库上传并设置启动命令为上面的 `uvicorn` 命令。
3. 在“环境变量”中配置：
   - `LLM_BASE_URL`（例如你的模型网关地址）
   - `LLM_API_KEY`
   - `LLM_MODEL`（如 `gpt-4o-mini` / 本地网关模型名）
4. 健康检查路径设置为 `/healthz`。
5. 发布后用 `/init_project` 和 `/chapter_card` 接口联调。

## API 说明
- `GET /healthz`：健康检查
- `POST /init_project`：初始化小说工程目录
- `POST /chapter_card`：生成章节意图卡（先占位，便于后接任意模型）

## 可直接用的 Prompt 模板
见 `templates/prompts.md`。

## 质量规则（建议硬约束）
1. 单章必须有“冲突推进”或“关系变化”。
2. 禁止连续 3 章无实质剧情进展。
3. 新设定出现后，24 章内必须有验证或反转。
4. 主角每卷必须完成一次认知升级或代价支付。
