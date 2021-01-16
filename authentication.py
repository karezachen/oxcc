# -*- coding: utf-8 -*-
# filename: authentication.py
# author: kareza
# email: kareza@qq.com
# description: 微信公众号后台服务器修改时，需要与服务器进行的token验证功能

import hashlib
import web

class Handle(object):
    def GET(self):
        try:
            data = web.input()

            # 不需要修改
            signature = data.signature
            timestamp = data.timestamp
            nonce = data.nonce
            echostr = data.echostr
            
            # 修改为公众号网页后台填写的Token值
            token = "d34f98175d2e76865c3b01a820929073"

            # 将获取的信息进行加密处理
            list = [token, timestamp, nonce]
            list.sort()
            sha1 = hashlib.sha1()
            sha1.update("".join(list).encode('utf-8'))
            hashcode = sha1.hexdigest()
            print("handle/GET func: hashcode, signature: ", hashcode, signature)

            # 签名认证
            if hashcode == signature:
                return echostr
            else:
                return ""
        except (Exception) as Argument:
            return Argument
