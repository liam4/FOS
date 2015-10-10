def boot ():
    execfile ("F:/Term/cmdrun/cmd2.py")
def safe ():
    print "There is so system safe mode at the moment, rerunning bootup."
    import boot
def sd ():
    import sys
    sys.exit("Stopped")
def erase ():
    print "THIS IS IRREVERSABLE! ARE YOU SURE? ENTER YES IN CAPS
    tst = raw_input ()
    if tst == "YES":
        print "Erasing all libraries and data. Entering recovery mode"
    import boot
def recover ():
    print "RECOVERY MODE"
    print "Running Recovery Scripts. Generating the system file may take a little while"
    execfile ("F:/RECOVERY/SYS.SET/BOOT.py")
