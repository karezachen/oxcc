# -*- coding: utf-8 -*-# 
# filename: handle.py
# author: kareza
# email: kareza@qq.com
# description: 转发粉丝发送的内容

import hashlib
import web
import reply
import receive

class Handle(object):
    def POST(self):
        try:
            webData = web.data()
            webData = webData.decode()
            print('接收到粉丝发送内容：\n', webData)
            recMsg = receive.parse_xml(webData)
            if isinstance(recMsg, receive.Msg):
                fromUser = recMsg.FromUserName
                toUser = recMsg.ToUserName
                if recMsg.MsgType == 'text':
                    # 避免超过5秒未回复，直接回复 success
                    reply.Msg().send()
                    textContent = recMsg.Content
                    textContent = textContent.decode()
                    replyMsg = reply.TextMsg(fromUser, toUser, textContent)
                    return replyMsg.send()
                if recMsg.MsgType == 'image':
                    mediaId = recMsg.MediaId
                    replyMsg = reply.ImageMsg(fromUser, toUser, mediaId)
                    return replyMsg.send()
                else:
                    return reply.Msg().send()
            else:
                return "success"
        except(Exception) as Argment:
            return Argment
