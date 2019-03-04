# encoding: UTF-8

from __future__ import print_function
import multiprocessing
import os,time
#----------------------------------------------------------------------
def runChildProcess():
    """子进程运行函数"""
    print('-'*20)
    print(os.system("ping www.baidu.com"))


#----------------------------------------------------------------------
def runParentProcess():
    """父进程运行函数"""
    
    
    p = None        # 子进程句柄

    while True:

        # 记录时间则需要启动子进程
        if  p is None:
        #    le.info(u'启动子进程')
            p = multiprocessing.Process(target=runChildProcess)
            p.start()
        #    le.info(u'子进程启动成功')

        time.sleep(120)

if __name__ == '__main__':
    runParentProcess()
