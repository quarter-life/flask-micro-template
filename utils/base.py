#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:quarterlife
# datetime:2022/7/13 16:44
# software: PyCharm
# description:  基础工具

import os

import yaml


def get_config_yaml(file_path):
    if not os.path.exists(file_path):
        print('无法找到文件')
        return None

    with open(file_path, 'r', encoding="utf-8") as f:
        return yaml.load(f, Loader=yaml.FullLoader)


if __name__ == '__main__':
    param = '../config/base.yaml'
    res = get_config_yaml(param)
    print(res)  # {'test': 1}
