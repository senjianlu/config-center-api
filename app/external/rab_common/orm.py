#!/usr/bin/env python
# -*- coding:UTF-8 -*-
#
# @AUTHOR: Rabbir
# @FILE: ~/Projects/rabbir/rab_common/orm
# @DATE: 2023/07/30 周日
# @TIME: 15:19:22
#
# @DESCRIPTION: ORM


from sqlalchemy import create_engine, event
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text
from datetime import datetime
# 涉及到路径问题的导入
try:
    from external.rab_common import config as external_rab_common_config
except Exception as e:
    import config as external_rab_common_config
try:
    from external.rab_common import logger as external_rab_common_logger
except Exception as e:
    import logger as external_rab_common_logger


# ORM 相关配置
ORM_CONFIG = external_rab_common_config.CONFIG["external"]["rab_common"]["orm"]
# 基类
Base = declarative_base()


def set_created_by(mapper, connection, instance):
    """
    @description: 设置创建者信息
    @param {type} 
    user_id: 用户 ID
    user_name: 用户名
    @return: 
    """
    instance.created_by = ORM_CONFIG["user"]["id"]
    instance.created_by_name = ORM_CONFIG["user"]["name"]
    instance.created_at = datetime.now()

def set_updated_by(mapper, connection, instance):
    """
    @description: 设置更新者信息
    @param {type}
    user_id: 用户 ID
    user_name: 用户名
    @return:
    """
    instance.updated_by = external_rab_common_config.CONFIG["user"]["id"]
    instance.updated_by_name = external_rab_common_config.CONFIG["user"]["name"]
    instance.updated_at = datetime.now()


def init_db(host: str=None, port: int=None, username: str=None, password: str=None, database: str=None):
    """
    @description: 初始化数据库
    @param {type} 
    engine: 数据库引擎
    @return: 
    """
    # 1. 读取配置文件（暂时只支持 PostgreSQL 数据库）
    postgresql_config = ORM_CONFIG["database"]
    host = host if host else postgresql_config["host"]
    port = port if port else postgresql_config["port"]
    username = username if username else postgresql_config["username"]
    password = password if password else postgresql_config["password"]
    database = database if database else postgresql_config["database"]
    # 2. 建立数据库连接
    engine = create_engine(
        f"postgresql://{username}:{password}@{host}:{port}/{database}")
    # 3. 创建表，如果有字段变更则删除重建
    Base.metadata.create_all(engine)
    # 4. 创建 DBSession
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    # 5. 查看数据库版本
    external_rab_common_logger.LOGGER.info("数据库连接建立：{}".format(session.execute(text("SELECT version()")).fetchone()[0]))
    # 6. 监听插入和更新事件，设置创建者和更新者信息
    for mapper in Base.registry.mappers:
        event.listen(mapper, "before_insert", set_created_by)
        event.listen(mapper, "before_update", set_updated_by)
    # 7. 返回 session
    return session
