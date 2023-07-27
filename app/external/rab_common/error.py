#!/usr/bin/env python
# -*- coding:UTF-8 -*-
#
# @AUTHOR: Rabbir
# @FILE: ~/Projects/rabbir/rab_common/error.py
# @DATE: 2023/07/27 周四
# @TIME: 08:52:07
#
# @DESCRIPTION: 自定义错误


class ConfigFileNotFoundError(Exception):
    """
    @description: 配置文件不存在
    """
    raise RuntimeError("配置文件不存在！请检查项目根目录下是否存在 config.toml 文件！")

class ConfigFileReadError(Exception):
    """
    @description: 配置文件读取失败
    """
    raise RuntimeError("配置文件读取失败！请检查 config.toml 文件是否存在语法错误！")