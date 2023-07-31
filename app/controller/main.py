#!/usr/bin/env python
# -*- coding:UTF-8 -*-
#
# @AUTHOR: Rabbir
# @FILE: ~/Projects/sbeer/config-center-api/app/controller/main.py
# @DATE: 2023/07/31 周一
# @TIME: 21:17:03
#
# @DESCRIPTION: Controller - 主控制器


import uvicorn
from fastapi import FastAPI
from external.rab_common import redis as external_rab_common_redis
from external.rab_common import logger as external_rab_common_logger
from external.rab_common import orm as external_rab_common_orm
from external.rab_fastapi_auth.controller import auth as external_rab_fastapi_auth_controller_auth


# FastAPI 实例
APP = FastAPI()


@APP.on_event("startup")
async def startup():
    """
    @description: 启动时执行
    """
    # 1. 初始化 Redis
    # APP.state.redis = await external_rab_common_redis.init_redis_async()
    print("FastAPI - Redis 连接建立。")
    # 2. 建立数据库连接
    APP.state.session = external_rab_common_orm.init_db()
    print("FastAPI - 数据库连接建立。")


@APP.on_event("shutdown")
async def shutdown():
    """
    @description: 关闭时执行
    """
    # 1. 关闭 Redis
    # await APP.state.redis.close()
    print("FastAPI - Redis 连接关闭。")
    # 2. 关闭数据库连接
    APP.state.session.close()
    print("FastAPI - 数据库连接关闭。")


@APP.get("/")
async def root():
    return {"message": "Hello World"}


# 路由
APP.include_router(
    external_rab_fastapi_auth_controller_auth.ROUTER
)
