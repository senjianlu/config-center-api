#!/usr/bin/env python
# -*- coding:UTF-8 -*-
#
# @AUTHOR: Rabbir
# @FILE: ~/Projects/rab_fastapi_login/business/token_biz
# @DATE: 2023/07/31 周一
# @TIME: 20:56:34
#
# @DESCRIPTION: Token 业务逻辑


import jwt
from external.rab_common import config as external_rab_common_config
from external.rab_fastapi_auth.models.User import User


# FastAPI Login 相关配置
FASTAPI_AUTH_TOKEN_CONFIG = external_rab_common_config.CONFIG["external"]["rab_fastapi_auth"]["token"]


def encode_token(user: User, secret_key: str=None, algorithm: str=None):
    """
    @description: 编码 Token
    @param {User} user: 用户
    @param {str} secret_key: 密钥
    @param {str} algorithm: 算法
    @return {str} Token
    """
    payload = {
        "id": user.id,
        "username": user.username,
    }
    secret_key = secret_key or FASTAPI_AUTH_TOKEN_CONFIG["secret_key"]
    algorithm = algorithm or FASTAPI_AUTH_TOKEN_CONFIG["algorithm"]
    return jwt.encode(payload, secret_key, algorithm=algorithm)

def decode_token(token: str, secret_key: str=None, algorithm: str=None):
    """
    @description: 解码 Token
    @param {type}
    @return:
    """
    secret_key = secret_key or FASTAPI_AUTH_TOKEN_CONFIG["secret_key"]
    algorithm = algorithm or FASTAPI_AUTH_TOKEN_CONFIG["algorithm"]
    return jwt.decode(token, secret_key, algorithms=[algorithm])
