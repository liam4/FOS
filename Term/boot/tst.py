import os
os.chdir ("F:/Term/cmdrun/cmd2.py")
import fosrun
print "FOSLAUNCHER VERSION 0.1"
print "PLEASE ENTER A LETTER FOR THE OPTION YOU WANT"
import time
time.sleep(1)
print """
A: DEFAULT BOOTUP
B: SINGLE COMMAND
C: SHUT DOWN
D: ERASE
E: RECOVER
USE LOWERCASE LETTERS
"""
VARE = raw_input ("F:/TERM/BOOT/TST.PY/")
if VARE == "a":
    fosrun.boot ()
if VARE == "b":
    fosrun.safe ()
if VARE == "c":
    fosrun.sd ()
if VARE == "d":
    fosrun.erase ()
if VARE == "e":
    fosrun.recover ()
    
    
    
