#!/usr/bin/env python
# -*- coding:UTF-8 -*-
#
# @AUTHOR: Rabbir
# @FILE: ~/Projects/rab_fastapi_login/business/auth_biz
# @DATE: 2023/07/30 周日
# @TIME: 20:20:21
#
# @DESCRIPTION: 认证业务逻辑


from external.rab_fastapi_auth.controller import auth as external_rab_fastapi_auth_controller_auth


def decode_token(token: str):
    """
    @description: 解码令牌
    @param {str} token: 访问令牌
    @return {dict} 令牌信息
    """
    return external_rab_fastapi_auth_controller_auth.OAUTH2_SCHEME.__call__(token)

async def get_current_user(token: str = external_rab_fastapi_auth_controller_auth.OAUTH2_SCHEME):
    """
    @description: 获取当前用户
    @param {str} token: 访问令牌
    @return {dict} 用户信息
    """
    # 1. 根据令牌解码
    token_info = decode_token(token)
    # 2. 获取用户信息
