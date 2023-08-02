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
from external.rab_fastapi_auth.business import auth_biz
from external.rab_fastapi_auth.business import token_biz
from external.rab_fastapi_auth.models.User import User
from external.rab_fastapi_auth.models.Error import UserNotFoundException, UsernameOrPasswordErrorException, TokenInvalidException, TokenExpiredException, TokenNotExistsException


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


async def _get_current_user(request: Request, token: str = Depends(OAUTH2_SCHEME)):
    """
    @description: 获取当前用户
    @param {str} token: 访问令牌
    @return {dict} 用户信息
    """
    # 1. 根据令牌解码
    try:
        decoded_token_info = token_biz.decode_token(token)
    except jwt.exceptions.DecodeError:
        raise TokenIllegalException()
    except jwt.exceptions.ExpiredSignatureError:
        raise TokenExpiredException()
    except Exception as e:
        raise HTTPException(status_code=401, detail="Token 解码出现未知错误！")
    # 2. 从 Redis 中获取用户信息
    try:
        user_info = await token_biz.get_user_info_from_redis(token, request.app.state.redis)
    except TokenNotExistsException:
        raise TokenNotExistsException()
    except Exception as e:
        raise HTTPException(status_code=401, detail="Token 对应的数据解析出现未知错误！")
    # 3. 对比用户信息
    if decoded_token_info["id"] != user_info["id"] or decoded_token_info["sub"] != user_info["username"]:
        raise TokenInvalidException()
    return User(**user_info)


@ROUTER.on_event("startup")
async def startup():
    # 1. 加载配置文件中的 Admin
    admin_biz.load_config_admin()
    print("FastAPI - 认证路由 - 配置文件 Admin 加载完成。")

@ROUTER.post('/login')
async def login(request: Request, form_data: OAuth2PasswordRequestForm = Depends()):
    # 1. 登录
    try:
        current_user = await auth_biz.do_login(form_data.username, form_data.password, request.app.state.session)
    except UserNotFoundException:
        raise UserNotFoundException
    except UsernameOrPasswordErrorException:
        raise UsernameOrPasswordErrorException
    # 2. 生成访问令牌
    access_token = token_biz.encode_token(current_user)
    # 3. 将令牌存储到 Redis 中
    access_token = await token_biz.save_token_to_redis(access_token, current_user, request.app.state.redis)
    return {"code": 200, "msg": "登录成功", "data": {"token": access_token}, "access_token": access_token, "token_type": "bearer"}

@ROUTER.get('/me')
async def get_me(current_user: User = Depends(_get_current_user)):
    return {"code": 200, "msg": "获取用户信息成功", "data": current_user}

@ROUTER.get('/token')
async def get_token(token: str = Depends(OAUTH2_SCHEME)):
    return { "code": 200, "msg": "获取 Token 成功", "data": {"token": token}}

@ROUTER.post('/logout')
async def logout(request: Request, token: str = Depends(OAUTH2_SCHEME)):
    await auth_biz.do_logout(token, request.app.state.redis)
    return {"code": 200, "msg": "登出成功", "data": {}}
