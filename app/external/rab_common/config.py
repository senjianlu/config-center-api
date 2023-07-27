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
import sys
import toml
# 涉及到路径问题的导入
try:
    from external.rab_common import error as external_rab_common_error
except Exception as e:
    import error as external_rab_common_error


# 项目根目录下的配置文件，往往和 app 目录同级
config_file_path = "../config.toml"
try:
    # 判断文件是否存在
    if os.path.exists(config_file_path):
        # 读取配置文件
        config = toml.load(config_file_path)
    else:
        raise external_rab_common_error.ConfigFileNotFoundError
except Exception as e:
    raise external_rab_common_error.ConfigFileReadError



# def switch_prod_config(path_to_add: str = "../"):
#     """
#     @description: 使用生产环境配置
#     """
#     # 1. 读取 config.toml   
#     config = toml.load("{}config.toml".format(path_to_add))
#     # 2. 读取 config.prod.toml
#     prod_config = toml.load("{}config.prod.toml".format(path_to_add))
#     # 3. 备份 config.toml
#     with open("{}config.toml.bak".format(path_to_add), "w") as f:
#         toml.dump(config, f)
#     # 3. 将 config.prod.toml 中的内容覆盖 config.toml
#     for key in prod_config:
#         config[key] = prod_config[key]
#     # 4. 将 config.toml 写入 config.toml
#     with open("{}config.toml".format(path_to_add), "w") as f:
#         toml.dump(config, f)

# def switch_dev_config(path_to_add: str = "../"):
#     """
#     @description: 使用开发环境配置
#     """
#     # 1. 判断是否有 config.toml.bak
#     config = toml.load("{}config.toml".format(path_to_add))
#     try:
#         with open("{}config.toml.bak".format(path_to_add), "r") as f:
#             config = toml.load(f)
#     except FileNotFoundError:
#         return
#     # 2. 将 config.toml.bak 中的内容覆盖 config.toml
#     with open("{}config.toml".format(path_to_add), "w") as f:
#         toml.dump(config, f)

# def test_intranet_config(path_to_add: str = "../"):
#     """
#     @description: 测试内网连接的配置是否可用
#     """
#     import psycopg2
#     import redis
#     # 1. PostgreSQL
#     is_postgresql_intranet_connected = False
#     # 1.1 内网 PostgreSQL 数据库 Host
#     intranet_postgresql_host = toml.load("{}config.intranet.toml".format(path_to_add))["postgresql"]["host"]
#     # 1.2 数据库连接信息
#     postgresql_port = toml.load("{}config.toml".format(path_to_add))["postgresql"]["port"]
#     postgresql_username = toml.load("{}config.toml".format(path_to_add))["postgresql"]["username"]
#     postgresql_password = toml.load("{}config.toml".format(path_to_add))["postgresql"]["password"]
#     postgresql_database = toml.load("{}config.toml".format(path_to_add))["postgresql"]["database"]
#     # 1.3 测试连接
#     print(intranet_postgresql_host, postgresql_port, postgresql_username, postgresql_password, postgresql_database)
#     conn, cur = None, None
#     try:
#         # 连接数据库，3 秒超时
#         conn = psycopg2.connect(
#             host=intranet_postgresql_host,
#             port=postgresql_port,
#             user=postgresql_username,
#             password=postgresql_password,
#             database=postgresql_database,
#             connect_timeout=3
#         )
#         # 查询数据库版本
#         cur = conn.cursor()
#         cur.execute('SELECT version()')
#         # 获取查询结果
#         db_version = cur.fetchone()
#         print("PostgreSQL 数据库版本：", db_version)
#         is_postgresql_intranet_connected = True
#     except Exception as e:
#         print("内网 PostgreSQL 数据库连接失败")
#         print(str(e))
#     finally:
#         try:
#             # 关闭游标  
#             cur.close()
#             # 关闭数据库连接
#             conn.close()
#         except Exception as e:
#             pass
#     # 2. Redis
#     is_redis_intranet_connected = False
#     # 2.1 内网 Redis Host
#     intranet_redis_host = toml.load("{}config.intranet.toml".format(path_to_add))["redis"]["host"]
#     # 2.2 Redis 连接信息
#     redis_port = toml.load("{}config.toml".format(path_to_add))["redis"]["port"]
#     redis_password = toml.load("{}config.toml".format(path_to_add))["redis"]["password"]
#     redis_database = toml.load("{}config.toml".format(path_to_add))["redis"]["database"]
#     # 2.3 测试连接
#     print(intranet_redis_host, redis_port, redis_password, redis_database)
#     r = None
#     try:
#         # 连接 Redis，3 秒超时
#         r = redis.Redis(
#             host=intranet_redis_host,
#             port=redis_port,
#             password=redis_password,
#             db=redis_database,
#             socket_timeout=3
#         )
#         r.set("intranet_test", "intranet_test")
#         print("Redis 内网连接成功")
#         is_redis_intranet_connected = True
#         r.delete("intranet_test")
#     except Exception as e:
#         print("Redis 内网连接失败")
#         print(str(e))
#     finally:
#         try:
#             r.close()
#         except Exception():
#             pass
#     # 3. 根据测试结果，修改 config.toml
#     if is_postgresql_intranet_connected:
#         config = toml.load("{}config.toml".format(path_to_add))
#         config["postgresql"]["host"] = intranet_postgresql_host
#         with open("{}config.toml".format(path_to_add), "w") as f:
#             toml.dump(config, f)
#         print("将 config.toml 中 PostgreSQL 的 host 修改为内网地址")
#     if is_redis_intranet_connected:
#         config = toml.load("{}config.toml".format(path_to_add))
#         config["redis"]["host"] = intranet_redis_host
#         with open("{}config.toml".format(path_to_add), "w") as f:
#             toml.dump(config, f)
#         print("将 config.toml 中 Redis 的 host 修改为内网地址")
#     # 4. 返回
#     print("内网连接测试结果：", is_postgresql_intranet_connected, is_redis_intranet_connected)
#     return is_postgresql_intranet_connected, is_redis_intranet_connected