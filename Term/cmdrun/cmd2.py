print "Importing... This could take a while!"
import ctypes
ctypes.windll.user32.MessageBoxA(0, "FOS has many bugs! Please report them at whco.ga", "FOS Notification", 1)
import foslogging
foslogging.info ("imported FOSLogging system")
import os
foslogging.info("imported os")
import time
foslogging.info("imported time")
import os
foslogging.info("imported os")
import importlib
foslogging.info("imported importlib")
import sys
foslogging.info("imported sys")
import foscmd
foslogging.info("-------SESSION READY-----------")
foscmd.init ()
#################FINISH BOOTUP###########################
foslogging.info('started bootup')
print "Hello"
print "I am the new terminal window"
print "I now have a logging system!"
foslogging.info('Finished intro')
global cd
cd = "F:/Term/commands/"
os.chdir (cd)
#SYSTEM#
while True:
    os.chdir (cd)
    foslogging.info('Command Ready')
    cmd = raw_input (cd)
    #############LOGGING ENDING DATA######################
    lginf = 'ran command ' + cmd + " on directory " + cd
    foslogging.info(lginf)
    ################RUN COMMAND##########################
    if cmd in ['etrash', 'delete', 'update', 'cd', 'catfish', 'cls', 'dl', 'hello', 'help', 'help 1', 'help 2', 'info', 'logout', 'ping', 'run', 'stop', 'time']:
        foslogging.info ("Command Known")
        sys.path.insert(0, 'F:/Term/commands/')
        answermodule = importlib.import_module(cmd)
    else:
        foslogging.warn ("Command unknown")
        print "Unknown command!"
    #stopper
