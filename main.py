#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:QuarterLife
# datetime:2022/5/18 09:42
# software: PyCharm

from gevent import monkey
from gevent.pywsgi import WSGIServer

monkey.patch_all()

from project import create_app

app = create_app()

if __name__ == '__main__':
    #   单进程 + 协程
    WSGIServer(('127.0.0.1', 8080), app).serve_forever()

    #   多进程 + 协程
    # from multiprocessing import cpu_count, Process
    # mulserver = WSGIServer(('0.0.0.0', 8080), app)
    # mulserver.start()
    #
    #
    # def server_forever():
    #     mulserver.start_accepting()
    #     mulserver._stop_event.wait()
    #
    #
    # for i in range(cpu_count()):
    #     p = Process(target=server_forever)
    #     p.start()
