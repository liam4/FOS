print "Please enter a username. This cannot be changed later"
usn = raw_input ()
import os
os.chdir ("F:/Users/")
os.mkdir (usn)
print "User account file made"
os.chdir ("F:/Users/" + usn)
print "Making system directories"
os.mkdir ("Desktop")
os.mkdir ("Documents")
os.mkdir ("Downloads")
os.mkdir ("Photos")
os.mkdir ("Special")
os.chdir ("F:/Users/" + usn + "/Special")
os.mkdir ("~")
