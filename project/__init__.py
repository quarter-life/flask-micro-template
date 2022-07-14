#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:quarterlife
# datetime:2022/5/18 10:33
# software: PyCharm
import os

from flask import Flask

from utils.config import get_app_config


def create_app():
    app = Flask(__name__)

    app.config.from_object(get_app_config())    # 更新配置文件

    os.makedirs(app.instance_path, exist_ok=True)  # 创建实例文件夹

    from . import blueprint
    app.register_blueprint(blueprint.bp)

    return app
