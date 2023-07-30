#!/usr/bin/env python
# -*- coding:UTF-8 -*-
#
# @AUTHOR: Rabbir
# @FILE: ~/Projects/rabbir/rab_common/config.py
# @DATE: 2023/05/04 周四
# @TIME: 08:52:07
#
# @DESCRIPTION: 配置文件


import os
import toml
# 涉及到路径问题的导入
try:
    from external.rab_common import error as external_rab_common_error
except Exception as e:
    import error as external_rab_common_error


# 配置
CONFIG = {}
# 项目根目录下的配置文件，往往和 app 目录同级
CONFIG_FILE_PATH = "../config.toml"
# 判断文件是否存在
if os.path.exists(CONFIG_FILE_PATH):
    # 读取配置文件
    try:
        CONFIG = toml.load(CONFIG_FILE_PATH)
    except Exception as e:
        raise external_rab_common_error.ConfigFileReadError()
else:
    raise external_rab_common_error.ConfigFileNotFoundError()


def switch_to_config(env: str):
    """
    @description: 切换到指定配置
    @param {str} env: dev/test/pre/prod
    """
    # 1. 拼凑配置文件路径
    env_config_file_path = "../config/config.{}.toml".format(env)
    # 2. 读取指定环境等配置
    if os.path.exists(env_config_file_path):
        try:
            env_config = toml.load(env_config_file_path)
        except Exception as e:
            raise external_rab_common_error.ConfigFileReadError(
                "配置文件不存在！请检查项目 config 目录下的" \
                    + " config.{}.toml 文件是否存在语法错误！".format(env))
    else:
        raise external_rab_common_error.ConfigFileNotFoundError(
            "配置文件不存在！请检查项目的 config 目录下是否存在" \
                + " config.{}.toml 文件！".format(env))
    # 3. 更新配置
    global CONFIG
    # 需要不断判断是否为 dict
    try:
        for key in env_config:
            if isinstance(env_config[key], dict):
                for sub_key in env_config[key]:
                    CONFIG[key][sub_key] = env_config[key][sub_key]
            else:
                CONFIG[key] = env_config[key]
    except Exception as e:
        raise external_rab_common_error.ConfigUpdateError(
            "配置更新失败！", str(e))


# 读取 config.toml 中 env 的值
ENV = CONFIG["external"]["rab_common"]["config"]["env"]
switch_to_config(ENV)