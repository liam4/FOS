ull = raw_input ("Hit the enter key to install")
print "Downloading and installing FOS..."
print "do NOT close this window"
import os
os.chdir('F:/')
import urllib2
url = "http://whco.ga/.FOS/fos/install/Term.zip"
file_name = url.split('/')[-1]
u = urllib2.urlopen(url)
f = open(file_name, 'wb')
meta = u.info()
file_size = int(meta.getheaders("Content-Length")[0])
print "Downloading: %s Bytes: %s" % (file_name, file_size)

file_size_dl = 0
block_sz = 8192
while True:
    buffer = u.read(block_sz)
    if not buffer:
        break

    file_size_dl += len(buffer)
    f.write(buffer)
    status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
    status = status + chr(8)*(len(status)+1)
    print status,
f.close()
import zipfile
with zipfile.ZipFile('Term.zip', "r") as z:
    z.extractall("F:/")
import ctypes  # An included library with Python install.
ctypes.windll.user32.MessageBoxA(0, "The system needs to shutdown!", "FOS Notification", 1)
print "installation complete"
import shutil
shutil.rmtree('F:/RECOVERY')
shutil.move ("F:/Term/RECOVERY", "F:/")
execfile ("F:/Term/cmdrun/stop.py")
