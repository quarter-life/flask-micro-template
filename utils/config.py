#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:quarterlife
# datetime:2022/7/13 17:51
# software: PyCharm

import os

import yaml
from flask import current_app

default_config_path = '../config/default.yaml'


def get_config_yaml(file_path):
    """
    获取配置文件
    Args:
        file_path: 文件路径

    Returns:    文件内容(dict / None)

    """
    if not os.path.exists(file_path):
        print('无法找到文件')
        return {}

    with open(file_path, 'r', encoding="utf-8") as f:
        return yaml.load(f, Loader=yaml.FullLoader)


def get_app_config():
    return get_config_yaml(default_config_path)


def get_app_config_by_key(key, default_value=None):
    if current_app:
        return current_app.config.get(key, default_value)
    else:
        return get_app_config().get(key, default_value)


if __name__ == '__main__':
    param = '../config/base.yaml'
    res = get_app_config_by_key('WX_APP_ID')
    print(res)  # {'test': 1}
