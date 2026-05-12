# write-novel

本仓库（`carringtonherman249-ai/write-novel`）已包含可直接使用的 `million-novel-writer` skill，路径：

- `skills/million-novel-writer/`

## 快速开始

### 1) 本地初始化小说工程
```bash
python skills/million-novel-writer/scripts/init_novel_project.py --path ./novel-project
```

### 2) 本地启动 API
```bash
pip install -r skills/million-novel-writer/requirements.txt
uvicorn api_server:app --app-dir skills/million-novel-writer/scripts --host 0.0.0.0 --port 8080
```

### 3) Docker 启动（仓库根目录 Dockerfile）
```bash
docker build -t million-novel-writer:latest .
docker run --rm -p 8080:8080 million-novel-writer:latest
```

> 说明：微信云托管会在代码仓库根目录查找 `Dockerfile`，本仓库已提供根目录 `Dockerfile`。

## 微信云托管
请参考：
- `skills/million-novel-writer/templates/wechat-cloud-deploy.md`
