#!/usr/bin/env python
# -*- coding:UTF-8 -*-
#
# @AUTHOR: Rabbir
# @FILE: ~/Projects/rabbir/rab_common/path.py
# @DATE: 2023/07/27 周四
# @TIME: 08:52:07
#
# @DESCRIPTION: 路径测试


import os
import sys


def print_paths():
    """
    @description: 打印路径
    """
    # 打印当前文件的绝对路径
    print(os.path.abspath(__file__))
    print(os.path.dirname(os.path.abspath(__file__)))
    print(sys.path)