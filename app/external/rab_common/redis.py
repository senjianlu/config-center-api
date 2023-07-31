#!/usr/bin/env python
# -*- coding:UTF-8 -*-
#
# @AUTHOR: Rabbir
# @FILE: ~/Projects/rabbir/rab_common/redis.py
# @DATE: 2023/07/30 周日
# @TIME: 20:29:54
#
# @DESCRIPTION: Redis 工具类


import redis
import aioredis
# 涉及到路径问题的导入
try:
    from external.rab_common import config as external_rab_common_config
except Exception as e:
    import config as external_rab_common_config
try:
    from external.rab_common import logger as external_rab_common_logger
except Exception as e:
    import logger as external_rab_common_logger


# Redis 相关配置
REDIS_CONFIG = external_rab_common_config.CONFIG["external"]["rab_common"]["redis"]


async def init_redis_async(host: str=None, port: int=None, password: str=None, database: int=None):
    """
    @description: 初始化 Redis
    @param {str} host: 主机
    @param {int} port: 端口
    @param {str} password: 密码
    @param {int} db: 数据库
    """
    host = host if host else REDIS_CONFIG["host"]
    port = port if port else REDIS_CONFIG["port"]
    password = password if password else REDIS_CONFIG["password"]
    database = database if database else REDIS_CONFIG["database"]
    # 连接 Redis
    r = await aioredis.from_url(f"redis://{host}:{port}/{database}", password=password)
    # 检索 Redis 版本信息，执行 "INFO" 命令
    external_rab_common_logger.LOGGER.info("异步 Redis 连接建立。")
    return r


def init_redis(host: str=None, port: int=None, password: str=None, database: int=None):
    """
    @description: 初始化 Redis
    @param {str} host: 主机
    @param {int} port: 端口
    @param {str} password: 密码
    @param {int} db: 数据库
    """
    host = host if host else REDIS_CONFIG["host"]
    port = port if port else REDIS_CONFIG["port"]
    password = password if password else REDIS_CONFIG["password"]
    database = database if database else REDIS_CONFIG["database"]
    # 连接 Redis
    pool = redis.ConnectionPool(host=host, port=port, password=password, db=database, decode_responses=True)
    # 检索 Redis 版本信息
    r = redis.Redis(connection_pool=pool)
    external_rab_common_logger.LOGGER.info(f"Redis 连接建立: Redis v{r.info()['redis_version']} {r.info()['os']}")
    return r
