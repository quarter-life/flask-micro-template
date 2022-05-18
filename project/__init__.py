#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:quarterlife
# datetime:2022/5/18 10:33
# software: PyCharm
from flask import Flask


def create_app():
    app = Flask(__name__)

    from . import blueprint
    app.register_blueprint(blueprint.bp)

    return app
