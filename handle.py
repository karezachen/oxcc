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
            webData = webData.decode()
            print("Handle Post webdata is ", webData)
            #后台打日志
            recMsg = receive.parse_xml(webData)
            if isinstance(recMsg, receive.Msg):
                fromUser = recMsg.FromUserName
                toUser = recMsg.ToUserName
                textContent = recMsg.Content
                textContent = textContent.decode()
                if recMsg.MsgType == 'text':
                    replyMsg = reply.PunchTheClock(fromUser, toUser, textContent)
                    return replyMsg.send()
                if recMsg.MsgType == 'image':
                    mediaId = recMsg.MediaId
                    replyMsg = reply.ImageMsg(fromUser, toUser, mediaId)
                    return replyMsg.send()
                else:
                    return reply.Msg().send()
            else:
                print("暂且不处理")
                return "success"
        except(Exception) as Argment:
            return Argment
