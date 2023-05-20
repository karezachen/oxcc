# -*- coding: utf-8 -*-
# filename: main.py
# author: kareza
# email: kareza@qq.com
# description: 主函数

import web
from handle import Handle
# from authentication import Handle

urls = (
    '/wechat', 'Handle',
)

if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()
