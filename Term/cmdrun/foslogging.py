f = open('new.log', 'a')
import time
def info (txt):
    txt = time.strftime("%H:%M:%S:") + "[INFO]" + txt + "\n"
    f.write (txt)
def warning (txt):
    txt = time.strftime("%H:%M:%S:") + "[WARN]" + txt + "\n"
    f.write (txt)
def fatal (txt):
    txt = time.strftime("%H:%M:%S:") + "[FATAL]" + txt + "\n"
    f.write (txt)
def undefined (txt):
    txt = time.strftime("%H:%M:%S:") + "[NULL]" + txt + "\n"
    f.write (txt)
def exception (txt):
    txt = time.strftime("%H:%M:%S:") + "[EXCE]" + txt + "\n"
    f.write (txt)
def close ():
    f.close()
    import os
    import shutil
    os.chdir ("F:/Logs/")
    fn = time.strftime('%H-%M-%S_%d-%m-%Y')
    os.mkdir (fn)
    shutil.move("F:/Term/cmdrun/new.log", "F:/Logs/" + fn)
    print "Successful! Program should stop now!"
    import sys
    sys.exit("Stopped")
def warn (txt):
    txt = time.strftime("%H:%M:%S:") + "[WARN]" + txt + "\n"
    f.write (txt)

#############################################################
#This program is made by the W-H Co. Team (C) 2015
#Do NOT resell or edit as your own
#############################################################
