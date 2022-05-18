#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:quarterlife
# datetime:2022/5/18 10:27
# software: PyCharm
from project.blueprint import bp


@bp.route('/bp')
def bp_test():
    return 'blueprint set successfully'
