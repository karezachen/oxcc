# -*- coding: utf-8 -*-# 
# filename: handle.py
import hashlib
import reply
import receive
import web
class Handle(object):
    def POST(self):
        try:
            webData = web.data()
            print("Handle Post webdata is ", webData)
            #后台打日志
            recMsg = receive.parse_xml(webData)
            if isinstance(recMsg, receive.Msg):
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                print('fromUser == oi8ob1S7zabQTx3LJUk6FUUtJCj4? fromUser: ' + toUser)
                if recMsg.MsgType == 'text':
                    if toUser == 'oi8ob1S7zabQTx3LJUk6FUUtJCj4':
                        replyMsg = reply.PunchTheClock(toUser, fromUser, recMsg.Content)
                    else:
                        content = "http://www.kareza.cn/jetbrain-activate-code.html"
                        replyMsg = reply.TextMsg(toUser, fromUser, content)
                    return replyMsg.send()
                if recMsg.MsgType == 'image':
                    mediaId = recMsg.MediaId
                    replyMsg = reply.ImageMsg(toUser, fromUser, mediaId)
                    return replyMsg.send()
                else:
                    return reply.Msg().send()
            else:
                print("暂且不处理")
                return "success"
        except(Exception) as Argment:
            return Argment
