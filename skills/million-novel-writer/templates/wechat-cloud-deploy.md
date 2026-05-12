# 微信云托管部署清单

## 端口与健康检查
- 服务端口：`8080`
- 健康检查：`/healthz`

## 启动命令
```bash
uvicorn api_server:app --app-dir skills/million-novel-writer/scripts --host 0.0.0.0 --port 8080
```

## 建议环境变量
- `LLM_BASE_URL`
- `LLM_API_KEY`
- `LLM_MODEL`

## 首次联调
1. `GET /healthz`
2. `POST /init_project`
3. `POST /chapter_card`


## Docker 构建
```bash
docker build -f skills/million-novel-writer/Dockerfile -t million-novel-writer:latest .
docker run --rm -p 8080:8080 million-novel-writer:latest
```
