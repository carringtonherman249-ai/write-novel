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

### 3) Docker 启动
```bash
docker build -f skills/million-novel-writer/Dockerfile -t million-novel-writer:latest .
docker run --rm -p 8080:8080 million-novel-writer:latest
```

## 微信云托管
请参考：
- `skills/million-novel-writer/templates/wechat-cloud-deploy.md`
