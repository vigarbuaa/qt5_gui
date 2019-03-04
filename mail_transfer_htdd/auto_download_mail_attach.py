# encoding: UTF-8
import os
import zmail
import logging
from contextlib import suppress
import traceback
from utility import todayDateStr

def initLog():
    """"""
    print("call initLog")
    #------------------ logging config ----------------------------------------------
    LOG_FORMAT = "%(asctime)s %(name)s %(levelname)s %(pathname)s %(message)s "
    DATE_FORMAT = '%Y-%m-%d  %H:%M:%S %a ' #配置输出时间的格式
    today_date= todayDateStr()
    log_file_name= todayDateStr()+"_baidu.log"

    log_output_dir="./baidu_log/"
    if not os.path.isdir(log_output_dir):
        os.makedirs(log_output_dir)
        
    logging.basicConfig(level=logging.INFO,
                        format=LOG_FORMAT,
                        filemode='a',
                        datefmt = DATE_FORMAT ,
                        filename=log_output_dir+log_file_name
                   )

USERNAME = "baidu@htdadao.net"
PASSWORD = "baidu@dmin1"

initLog()

date_str=todayDateStr()
backup_dir = './_backup/'
persist_walk = True
walk_steps = 20
backup_walk_path = backup_dir + '_mail_walk.txt'
logging.info("logging in mailserver")
srv = zmail.server(USERNAME, PASSWORD,pop_host='pop.ym.163.com')
mail_count, mail_size = srv.stat()
logging.info("[mail_count]: " + str(mail_count) + " [mail_size]: " + str(mail_size))
logging.info("backup_dir: "+backup_dir)
# Make directory if not exist.
with suppress(FileExistsError):
    os.makedirs(backup_dir)

# walk functions.
def get_walk():
    if os.path.exists(backup_walk_path):
        with open(backup_walk_path, mode='r') as f:
            _walk = int(f.read())
        return _walk
    return 1

def save_walk(_walk):
    with open(backup_walk_path, mode='w') as f:
        f.write(str(_walk))

def safe_str(o, max_len=220):
    if o is None:
        return ''
    s = str(o).replace('/', ':')
    if len(s) > max_len:
        return s[:max_len]
    return s

walk = get_walk() if persist_walk else 1
while walk <= mail_count:
    logging.info("walk {} mail_count {}".format(walk,mail_count))
    try:
        walk += 1
        mails = srv.get_mails(start_index=walk, end_index=walk + walk_steps)
        for mail in mails:
            try:
                mail_subject=mail['subject']
                mail_date_str=mail['date']
                mail_from = mail['from']
                logging.info("{0} send mail {1} on {2}".format(mail_from,mail_subject,mail_date_str))
                if mail_subject in ["market","bigdata","finance","hr","gyzn","scx"]:
                    folder_path='./_backup/{0}/{1}'.format(date_str,mail_subject) 
                    logging.info("{}".format(folder_path))
                    # Make directory if not exist.
                    with suppress(FileExistsError):
                        os.makedirs(folder_path)
                    zmail.save_attachment(mail,folder_path)
            except:
                traceback.print_exc
                logging.info("error!exception")
            if persist_walk:
                save_walk(walk)
    except:
        logging.info("get_mails error")