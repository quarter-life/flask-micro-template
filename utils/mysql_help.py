#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:quarterlife
# datetime:2022/7/14 10:38
# software: PyCharm
import time
import pymysql
from dbutils.pooled_db import PooledDB
from flask import g

from utils.config import get_app_config_by_key

POOL = PooledDB(
    creator=pymysql,  # 使用链接数据库的模块
    maxconnections=6,  # 连接池允许的最大连接数，0和None表示不限制连接数
    mincached=2,  # 初始化时，链接池中至少创建的空闲的链接，0表示不创建
    maxcached=5,  # 链接池中最多闲置的链接，0和None不限制
    maxshared=1,  # 链接池中最多共享的链接数量，0和None表示全部共享
    blocking=True,  # 连接池中如果没有可用连接后，是否阻塞等待。True，等待；False，不等待然后报错
    maxusage=None,  # 一个链接最多被重复使用的次数，None表示无限制
    setsession=[],  # 开始会话前执行的命令列表。如：["set datestyle to ...", "set time zone ..."]
    ping=0,
    # ping MySQL服务端，检查是否服务可用。
    # 如：0 = None = never,
    # 1 = default = whenever it is requested,
    # 2 = when a cursor is created,
    # 4 = when a query is executed,
    # 7 = always
    charset='utf8',
    host=get_app_config_by_key('MYSQL_HOST', '127.0.0.1'),
    port=get_app_config_by_key('MYSQL_PORT', 3306),
    user=get_app_config_by_key('MYSQL_USER'),
    password=get_app_config_by_key('MYSQL_PWD'),
    database=get_app_config_by_key('MYSQL_DB'),
    cursorclass=pymysql.cursors.DictCursor,
)


class MysqlHelpBaseError(Exception):
    def __init__(self):
        pass


class MysqlHelp(object):
    def __init__(self):
        pass

    def connect(self):
        """Connects to the specific database."""
        return POOL.connection()

    def get_db(self):
        """Opens a new database connection if there is none yet for the
        current application context.
        """
        if not g:
            return self.connect()

        if not hasattr(g, 'mysql'):
            g.mysql = self.connect()

        return g.mysql


if __name__ == '__main__':
    mh = MysqlHelp()
    connection = mh.get_db()
    print(connection)
    cur = connection.cursor()
    print(cur)
    cur.execute('select * from cabinet')
    print(cur.fetchall())
    connection.close()
