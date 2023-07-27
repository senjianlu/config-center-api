# config-center-api
配置中心后端接口

## 部署&启动
### 1. 部署方式
#### 1.1 Docker 部署
```bash
docker run -d \
  --name config-center-api \
  -p 18000:8000 \
  -v /rabbir/docker/config-center-api/logs:/app/config-center-api/logs \
  -e RAB_DEBUG="False" \
  -e RAB_LOG_LEVEL="INFO" \
  -e RAB_FASTAPI_HOST="0.0.0.0" \
  -e RAB_FASTAPI_PORT="8000" \
  -e RAB_POSTGRESQL_HOST="127.0.0.1" \
  -e RAB_POSTGRESQL_PORT="5432" \
  -e RAB_POSTGRESQL_USERNAME="postgres" \
  -e RAB_POSTGRESQL_PASSWORD="postgres" \
  -e RAB_POSTGRESQL_DATABASE="config_center" \
  -e RAB_REDIS_HOST="127.0.0.1" \
  -e RAB_REDIS_PORT="6379" \
  -e RAB_REDIS_PASSWORD="redis" \
  -e RAB_REDIS_DATABASE="0" \
  rabbir/config-center-api:latest
```
#### 1.2 手动部署
下载源码后，修改 `config.toml` 中的配置项目，接着进入 `app/` 目录执行：
```bash
python3 main.py
```

### 2. 环境变量
**注意，环境变量的优先级高于 `config.toml` 中的配置项！**
> 我已经通过 `RAB` 前缀来预防和你的既有环境变量冲突。  
> 如果你有部署多个我开发的项目的需求，且环境变量还需要设置得不一样，那并做不到，只能删除所有环境变量，并手动修改各项目的 `config.toml` 配置项。

| 环境变量 | 说明 | 默认值 | 必填 | 备注 |
| :---: | :---: | :---: | :---: | :---: |
| RAB_DEBUG | 是否开启调试模式 | False | 否 | True, False |
| RAB_LOG_LEVEL | 日志级别 | INFO | 否 | DEBUG, INFO, WARNING, ERROR, CRITICAL |
| RAB_FASTAPI_HOST | FastAPI 服务监听地址 | 0.0.0.0 | 否 | |
| RAB_FASTAPI_PORT | FastAPI 服务监听端口 | 8000 | 否 | |
| RAB_POSTGRESQL_HOST | PostgreSQL 数据库地址 | | | |
| RAB_POSTGRESQL_PORT | PostgreSQL 数据库端口 | | | |
| RAB_POSTGRESQL_USERNAME | PostgreSQL 数据库用户名 | | | |
| RAB_POSTGRESQL_PASSWORD | PostgreSQL 数据库密码 | | | |
| RAB_POSTGRESQL_DATABASE | PostgreSQL 数据库名 | | | |
| RAB_REDIS_HOST | Redis 数据库地址 | | | |
| RAB_REDIS_PORT | Redis 数据库端口 | | | |
| RAB_REDIS_PASSWORD | Redis 数据库密码 | | | |
| RAB_REDIS_DATABASE | Redis 数据库名 | | | |


## 使用
### 1. 部署 `config-center-web` 前端项目
> 详细内容请参考 [senjianlu/config-center-web](https://github.com/senjianlu/config-center-web) 项目。
```bash
docker run -d \
  --name config-center-web \
  -p 13000:3000 \
  -v /rabbir/docker/config-center-web/logs:/app/config-center-web/logs \
  -e RAB_CONFIG_CENTER_API_HOST="114.114.114.114" \
  -e RAB_CONFIG_CENTER_API_PORT="18000" \
  -e RAB_CONFIG_CENTER_WEB_HOST="0.0.0.0" \
  -e RAB_CONFIG_CENTER_WEB_PORT="3000" \
  rabbir/config-center-web:latest
```
之后前往 [http://localhost:13000](http://localhost:13000) 即可访问，初始用户名密码均为 `admin`。

### 2. 配置中心接口文档
访问 [http://localhost:18000/docs](http://localhost:18000/docs) 即可查看接口文档，认证用户名密码均为 `admin`。