#!/usr/bin/env python
# -*- coding:UTF-8 -*-
#
# @AUTHOR: Rabbir
# @FILE: ~/Projects/rab_fastapi_login/controller/auth
# @DATE: 2023/07/30 周日
# @TIME: 17:27:04
#
# @DESCRIPTION: 认证控制器


from fastapi import APIRouter, Depends, Request
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from external.rab_common import config as external_rab_common_config
from external.rab_fastapi_auth.business import admin_biz


# FastAPI 认证路由相关配置
FASTAPI_AUTH_ROUTER_CONFIG = external_rab_common_config.CONFIG["external"]["rab_fastapi_auth"]["router"]
# OAuth2 密码模式
OAUTH2_SCHEME = OAuth2PasswordBearer(tokenUrl=FASTAPI_AUTH_ROUTER_CONFIG["token"])
# FastAPI 认证路由
ROUTER = APIRouter(
    prefix=FASTAPI_AUTH_ROUTER_CONFIG["prefix"],
    tags=["auth"]
)


from external.rab_fastapi_auth.business import auth_biz


@ROUTER.on_event("startup")
async def startup():
    # 1. 加载配置文件中的 Admin
    admin_biz.load_config_admin()
    print("FastAPI - 认证路由 - 配置文件 Admin 加载完成。")

@ROUTER.post('/login')
async def login(request: Request, form_data: OAuth2PasswordRequestForm = Depends()):
    # 1. 登录
    current_user = await auth_biz.do_login(form_data.username, form_data.password, request.app.state.session)
    return current_user.__dict__

@ROUTER.get('/me')
async def get_me(token: str = Depends(OAUTH2_SCHEME)):
    return { "token": token}

@ROUTER.get('/token')
async def get_token():
    return { "message": "we are adding numbers"}

@ROUTER.post('/logout')
async def logout():
    return { "message": "we are adding numbers"}
