import foslogging
def stop():
    import time
    time.sleep (2)
    foslogging.warn ("The system is shutting down NOW!")
    foslogging.close ()
def error(ty):
    print "ERROR: ", ty
def init():
    print "The system is turning on NOW!"
    
    
