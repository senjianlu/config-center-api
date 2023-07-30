#!/usr/bin/env python
# -*- coding:UTF-8 -*-
#
# @AUTHOR: Rabbir
# @FILE: ~/Projects/rab_fastapi_login/controller/auth
# @DATE: 2023/07/30 周日
# @TIME: 17:27:04
#
# @DESCRIPTION: 认证控制器


from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from external.rab_common import config as external_rab_common_config


# FastAPI 认证路由相关配置
FASTAPI_AUTH_ROUTER_CONFIG = external_rab_common_config.CONFIG["external"]["rab_fastapi_auth"]["router"]
# OAuth2 密码模式
OAUTH2_SCHEME = OAuth2PasswordBearer(tokenUrl=FASTAPI_AUTH_ROUTER_CONFIG["token"])