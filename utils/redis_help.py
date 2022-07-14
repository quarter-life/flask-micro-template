#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:quarterlife
# datetime:2022/7/14 10:29
# software: PyCharm

import redis


class RedisHelp(object):
    def __init__(self):
        self.keys = {
        }

        self.config = {
            'host': '127.0.0.1',
            'port': 6379,
            'password': '',
            'db': 0,
            'decode_responses': True
        }

    def connect_redis(self):
        return redis.Redis(**self.config)

    def get(self, key):
        redis_connect = self.connect_redis()
        return redis_connect.get(key)
