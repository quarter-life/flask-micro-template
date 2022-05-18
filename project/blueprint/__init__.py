#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:quarterlife
# datetime:2022/5/18 10:26
# software: PyCharm
from flask import Blueprint

bp = Blueprint('model', __name__, url_prefix='')

from . import bp1
