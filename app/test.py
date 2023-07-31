#!/usr/bin/env python
# -*- coding:UTF-8 -*-
#
# @AUTHOR: Rabbir
# @FILE: ~/Projects/rabbir/config-center-api/test.py
# @DATE: 2023/07/27 周四
# @TIME: 13:58:07
#
# @DESCRIPTION: 测试


def test_rab_common():
    # from external.rab_common import path as external_rab_common_path
    from external.rab_common import config as external_rab_common_config
    from external.rab_common import logger as external_rab_common_logger
    from external.rab_common import orm as external_rab_common_orm
    from external.rab_common import redis as external_rab_common_redis
    # external_rab_common_path.print_paths()
    print(external_rab_common_config.ENV)
    print(external_rab_common_config.CONFIG)
    external_rab_common_logger.LOGGER.debug("debug")
    external_rab_common_logger.LOGGER.info("info")
    external_rab_common_logger.LOGGER.warning("warning")
    external_rab_common_logger.LOGGER.error("error")
    external_rab_common_logger.LOGGER.critical("critical")
    session = external_rab_common_orm.init_db()
    external_rab_common_redis.init_redis()

def test_fastapi():
    import uvicorn
    from controller import main as controller_main
    uvicorn.run(app="controller.main:APP", host="0.0.0.0", port=8000, reload=True)


# 单体测试
if __name__ == "__main__":
    test_fastapi()

