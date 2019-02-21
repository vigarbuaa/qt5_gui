# encoding: UTF-8

from __future__ import print_function
import os
import zmail
from contextlib import suppress
import traceback
from utility import *
# [done]add random EmailEngine check ,send this git
# [done]get Email info to show it in table

########################################################################

class EmailHeader(object):
    """"""
    #----------------------------------------------------------------------
    def __init__(self,sender,timeStr,subject):
        """Constructor"""
        self.sender=sender
        self.subject=subject
        #self.attach=attach # bool 
        self.time_str=str(timeStr)
    
class EmailEngine(object):
    #----------------------------------------------------------------------
    def __init__(self,username,password):
        """初始化事件引擎"""
        # 事件队列
        #self.smtp_addr = smtp
        #self.pop_addr = pop
        self.username =username
        self.password = password
        self.server = zmail.server(self.username, self.password)

    def sendMail(self,to_addr,subject,content):
        self.server.send_mail(to_addr,{'subject':subject,'content_text':content})

    def getMailInfo(self,start_index, end_index):
        mails=[]
        try:
            mails = self.server.get_mails(start_index, end_index)
        except:
            traceback.print_exc()
            print("getMailInfo internal error")
            
        for mail in mails:
            print('----{} date:{}  from:{}'.format(mail['subject'], mail['date'],mail['from']))
            
        return mails
    
    def getLatestMailInfo(self):
        latest_mail = self.server.get_latest()
        print("attachment info: " + str(latest_mail['attachments']))
        zmail.show(latest_mail)

    def getMailServerStat(self):
        mailbox_info = self.server.stat()
        print(mailbox_info)
        
    #----------------------------------------------------------------------
    def getMailHeader(self):
        """"""
        maillist=[]
        all=self.server.get_headers(1200,1790)
        for elem in all:
            print("***********")
            # print(elem.__dict__)
            print("---"+ str(elem['id']))
            mail=EmailHeader(elem['from'], elem['date'], elem['subject'])
            # print(mail.__dict__)
            maillist.append(mail)
        return maillist
        
#----------------------------------------------------------------------
def test():
    """测试函数"""
    import sys
    from datetime import datetime
    from qtpy.QtCore import QCoreApplication
    
    def simpletest(event):
        print(u'处理每秒触发的计时器事件：{}'.format(str(datetime.now())))
    
    app = QCoreApplication(sys.argv)
    
    ee = EventEngine2()
    #ee.register(EVENT_TIMER, simpletest)
    ee.registerGeneralHandler(simpletest)
    ee.start()
    app.exec_()
    
# 直接运行脚本可以进行测试
if __name__ == '__main__':
    import zmail
    config= load_json("mail.json")
    print(config['mail']+"--"+ config['passwd'])
    server = EmailEngine(config['mail'],config['passwd'])
    #server = EmailEngine("vigarxueer@126.com","opcu@163")
    server.getLatestMailInfo()
    print("------------------")
    
    server.sendMail("vigarcheck@bccto.me", '功能验证 function', '我需要验收,逗吧')
    
    """
    server.getLatestMailInfo()
    print("------------------")
    server.getMailServerStat()
    print("------------------")
    server.getMailHeader()
    print("-------!!!---------")
    server.getLatestMailInfo()
    
    for elem in range(20):
        try:        
            server.getMailInfo(1000+elem*10,1010+elem*10)
        except:
            traceback.print_exc
            print("getMailInfo error")
    """
    # Send mail
    # server.send_mail('qufw@htdadao.net',{'subject':'Hello!','content_text':'By zmail.'})
    # Or to a list of friends.
    # server.send_mail(['friend1@example.com','friend2@example.com'],{'subject':'Hello!','content_text':'By zmail.'})