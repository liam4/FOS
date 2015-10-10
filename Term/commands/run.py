import os
print "directory and filename:"
run1 = raw_input ()
print "running:", run1 
if os.path.isfile(run1):
    execfile (run1)
else:
    print "Directory doesn't exist...sorry"
