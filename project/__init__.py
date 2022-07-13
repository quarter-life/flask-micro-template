#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:quarterlife
# datetime:2022/5/18 10:33
# software: PyCharm
import os

from flask import Flask


def create_app():
    app = Flask(__name__)

    os.makedirs(app.instance_path, exist_ok=True)  # 创建实例文件夹

    from . import blueprint
    app.register_blueprint(blueprint.bp)

    return app
