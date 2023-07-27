#!/usr/bin/env python
# -*- coding:UTF-8 -*-
#
# @AUTHOR: Rabbir
# @FILE: ~/Projects/rab_fastapi_login/models/User
# @DATE: 2023/07/25 周二
# @TIME: 11:20:09
#
# @DESCRIPTION: 代理节点 Container 模型


import uuid
from enum import Enum
from typing import Union
from datetime import datetime
from sqlalchemy import Column, String, Text, Boolean, DateTime, Integer


# 导入父项目的 Base 或建立自己的 Base
try:
    from models.Base import Base
except Exception:
    from sqlalchemy.ext.declarative import declarative_base
    Base = declarative_base()


class User(Base):
    username: str
    email: Union[str, None] = None
    full_name: Union[str, None] = None
    disabled: Union[bool, None] = None