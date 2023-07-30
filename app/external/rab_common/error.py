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

    def __init__(self, message="配置文件不存在！请检查项目根目录下是否存在 config.toml 文件！"):
        super().__init__(self)
        self.message = message

    def __str__(self):
        return self.message

class ConfigFileReadError(Exception):
    """
    @description: 配置文件读取失败
    """

    def __init__(self, message="配置文件读取失败！请检查 config.toml 文件是否存在语法错误！"):
        super().__init__(self)
        self.message = message

    def __str__(self):
        return self.message

class ConfigUpdateError(Exception):
    """
    @description: 配置更新失败
    """

    def __init__(self, message="配置更新失败！", detail=None):
        super().__init__(self)
        self.message = message
        self.detail = detail

    def __str__(self):
        if self.detail:
            return self.message + "详情：" + self.detail
        else:
            return self.message
