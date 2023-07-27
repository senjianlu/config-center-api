#!/usr/bin/env python
# -*- coding:UTF-8 -*-
#
# @AUTHOR: Rabbir
# @FILE: ~/Projects/sbeer/proxy-pool/proxypool/model/base.py
# @DATE: 2023/05/01 周一
# @TIME: 20:52:27
#
# @DESCRIPTION: 模型基类


from sqlalchemy import create_engine, event
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text
from datetime import datetime

from common.config import config
from common.logger import logger


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
    instance.created_by = config["user"]["id"]
    instance.created_by_name = config["user"]["name"]
    instance.created_at = datetime.now()

def set_updated_by(mapper, connection, instance):
    """
    @description: 设置更新者信息
    @param {type}
    user_id: 用户 ID
    user_name: 用户名
    @return:
    """
    instance.updated_by = config["user"]["id"]
    instance.updated_by_name = config["user"]["name"]
    instance.updated_at = datetime.now()


def init_db():
    """
    @description: 初始化数据库
    @param {type} 
    engine: 数据库引擎
    @return: 
    """
    # 1. 读取配置文件
    postgresql_config = config["postgresql"]
    host = postgresql_config["host"]
    port = postgresql_config["port"]
    username = postgresql_config["username"]
    password = postgresql_config["password"]
    database = postgresql_config["database"]
    # 2. 建立数据库连接
    engine = create_engine(
        f"postgresql://{username}:{password}@{host}:{port}/{database}")
    # 3. 创建表，如果有字段变更则删除重建
    Base.metadata.create_all(engine)
    # 4. 创建 DBSession
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    # 5. 查看数据库版本
    logger.info("数据库连接建立：{}".format(session.execute(text("SELECT version()")).fetchone()[0]))
    # 6. 监听插入和更新事件，设置创建者和更新者信息
    for mapper in Base.registry.mappers:
        event.listen(mapper, "before_insert", set_created_by)
        event.listen(mapper, "before_update", set_updated_by)
    # 7. 返回 session
    return session