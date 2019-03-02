import os
import zmail
from contextlib import suppress
import traceback
from utility import todayDateStr

USERNAME = "baidu@htdadao.net"
PASSWORD = "baidu@dmin1"

date_str=todayDateStr()
backup_dir = './_backup/'
persist_walk = True
walk_steps = 20
backup_walk_path = backup_dir + '_mail_walk.txt'

srv = zmail.server(USERNAME, PASSWORD,pop_host='pop.ym.163.com')#,pop_port=995)
mail_count, mail_size = srv.stat()
print("[mail_count]: " + str(mail_count) + " [mail_size]: " + str(mail_size))
print("backup_dir: "+backup_dir)
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
    print("walk {} mail_count {}".format(walk,mail_count))
    try:
        walk += 1
        mails = srv.get_mails(start_index=walk, end_index=walk + walk_steps)
        for mail in mails:
            try:
                mail_subject=mail['subject']
                mail_date_str=mail['date']
                mail_from = mail['from']
                print("{0} send mail {1} on {2}".format(mail_from,mail_subject,mail_date_str))
                if mail_subject in ["market","bigdata","finance","hr","gyzn","scx"]:
                    folder_path='./_backup/{0}/{1}'.format(date_str,mail_subject) 
                    print("{}".format(folder_path))
                    # Make directory if not exist.
                    with suppress(FileExistsError):
                        os.makedirs(folder_path)
                    zmail.save_attachment(mail,folder_path)
            except:
                traceback.print_exc
                print("error!exception")
            if persist_walk:
                save_walk(walk)
    except:
        print("get_mails error")
