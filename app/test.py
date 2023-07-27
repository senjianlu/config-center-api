#!/usr/bin/env python
# -*- coding:UTF-8 -*-
#
# @AUTHOR: Rabbir
# @FILE: ~/Projects/rabbir/config-center-api/test.py
# @DATE: 2023/07/27 周四
# @TIME: 13:58:07
#
# @DESCRIPTION: 测试


from external.rab_common import path as external_rab_common_path
from external.rab_common import config as external_rab_common_config


# 单体测试
if __name__ == "__main__":
    external_rab_common_path.print_paths()