#!/usr/bin/env python
# -*- coding:UTF-8 -*-
#
# @AUTHOR: Rabbir
# @FILE: ~/Projects/rab_fastapi_login/business/auth_biz
# @DATE: 2023/07/30 周日
# @TIME: 20:20:21
#
# @DESCRIPTION: 认证业务逻辑


import jwt
import hashlib
from external.rab_fastapi_auth.controller import auth as external_rab_fastapi_auth_controller_auth
from external.rab_fastapi_auth.models.User import User


# def decode_token(token: str):
#     """
#     @description: 解码令牌
#     @param {str} token: 访问令牌
#     @return {dict} 令牌信息
#     """
#     return external_rab_fastapi_auth_controller_auth.OAUTH2_SCHEME.__call__(token)

def _verify_password(plain_password: str, hashed_password: str):
    """
    @description: 校验密码
    @param {str} plain_password: 明文密码
    @param {str} hashed_password: 密文密码
    @return {bool} 是否匹配
    """
    return hashlib.sha256(plain_password.encode()).hexdigest() == hashed_password

async def do_login(username: str, password: str, session):
    """
    @description: 登录
    @param {str} username: 用户名
    @param {str} password: 密码
    @return {User} 用户
    """
    # 1. 查询用户
    user = session.query(User).filter(User.username == username).first()
    # 2. 校验密码
    if not user or not _verify_password(password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="用户名或密码错误"
        )
    # 3. 返回用户
    return user

async def get_current_user(token: str = external_rab_fastapi_auth_controller_auth.OAUTH2_SCHEME):
    """
    @description: 获取当前用户
    @param {str} token: 访问令牌
    @return {dict} 用户信息
    """
    # 1. 根据令牌解码
    # token_info = decode_token(token)
    # 2. 获取用户信息
    pass
