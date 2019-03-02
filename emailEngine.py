# encoding: UTF-8

from __future__ import print_function
import os
import zmail
from contextlib import suppress
import traceback
from utility import *
from engine import EventEngine 
# [done]add random EmailEngine check ,send this git
# [done]get Email info to show it in table

########################################################################

class EmailHeader(object):
    """"""
    #----------------------------------------------------------------------
    def __init__(self,mail_id,sender,timeStr,subject):
        """Constructor"""
        self.sender=sender
        self.subject=subject
        self.mail_id=mail_id
        #self.attach=attach # bool 
        self.time_str=str(timeStr)
    
class EmailEngine(object):
    #----------------------------------------------------------------------
    def __init__(self,username,password,event_engine):
        """初始化事件引擎"""
        # 事件队列
        #self.smtp_addr = smtp
        #self.pop_addr = pop
        self.username =username
        self.password = password
        self.server = zmail.server(self.username, self.password)
        self.event_engine= event_engine

    def sendMail(self,to_addr,subject,content):
        print('begin to sendMail to ' + subject + "content: " + content)
        self.server.send_mail(to_addr,{'subject':subject,'content_text':content})

    def forwardMail(self,to_addr,mail_id):
        mail= self.getMailById(mail_id)
        if mail:
            print("forward mail" + str(mail['id']) + "--" + mail['subject'])
            self.server.send_mail(to_addr,{'subject':mail['subject'],'content_html':mail['content_text']})
        else:
            print(str(mail_id) + " is null, no need to forward it")
        
    def getMailById(self,mail_id):
        mail=self.server.get_mail(mail_id)
        return mail
    
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
        zmail.show(latest_mail)

    def getMailServerStat(self):
        mailbox_info = self.server.stat()
        print(mailbox_info)
        
    def saveAttach(self,mail_id,folder_path):
        mail=self.server.get_mail(mail_id)
        #with suppress(folder_path):
        #    os.mkdir(folder_path)
        zmail.save_attachment(mail,folder_path)
 
    #----------------------------------------------------------------------
    def getMailHeader(self,start_index,end_index):
        """"""
        maillist=[]
        all=self.server.get_headers(start_index,end_index)
        for elem in all:
            print("***********")
            # print(elem.__dict__)
            print("---"+ str(elem['id']))
            mail=EmailHeader(elem['id'],elem['from'], elem['date'], elem['subject'])
            # print(mail.__dict__)
            maillist.append(mail)
        return maillist
        
# 直接运行脚本可以进行测试
if __name__ == '__main__':
    import zmail
    config= load_json("mail.json")
    print(config['fr_mail'],config['fr_passwd'])
    #print(config['mail']+"--"+ config['passwd'])
    #engine= EventEngine()
    #server = EmailEngine(config['mail'],config['passwd'],engine)
#    fr_server=zmail.server(config['fr_mail'],config['fr_passwd'],smtp_host='192.168.102.207',smtp_port='25',smtp_ssl=False)
    fr_server=zmail.server("baidu@xczdadao.net","AB12345678c",smtp_host='192.168.102.207',smtp_port='25',
                           pop_host="192.168.102.207",pop_port="110",pop_ssl=False,smtp_ssl=False)
#    server = zmail.server('username','password',smtp_host='smtp.163.com',smtp_port=994,smtp_ssl=True,pop_host='pop.163.com',pop_port=995,pop_tls=True)
    
    mailbox_info = fr_server.stat()
    print(mailbox_info)
    
    latest_mail = fr_server.get_latest()
    zmail.show(latest_mail)
    
    ret=fr_server.send_mail("baidu@xczdadao.net",{'subject':"aaa",'content_text':"bbb"})
    print(ret)
    # server = EmailEngine("vigarxueer@126.com","opcu@163")
    # server.getLatestMailInfo()
    """
    print("--------------------")
    
    #server.sendMail("vigarcheck@bccto.me", '功能验证 function', '我需要验收,逗吧')
    server.forwardMail("vigarcheck@bccto.me", 1200)
    headers = server.getMailHeader(1100,1110)
    print("-------!!!---------")
    print(headers)
    for header in headers:
        print("!!!"+ str(header))
        #print(header.__dict__)
    print("======+++++++++++++++============")
    mail=server.saveAttach(1457,"d:\\jpm")
    
    mail=server.getMailById(1200)
    print("*******************")
    for k,v in mail.items():
        print("===")
        print("[debug]",k,v)
    
    print("!!!!" + str(mail['subject']))
    print("!!!!" + str(mail['content_text']))
    
    server.getLatestMailInfo()
    print("------------------")
    server.getMailServerStat()
    print("------------------")
    server.getMailHeader(1100,1110)
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