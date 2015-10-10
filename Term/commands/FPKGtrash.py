import shutil
import time
import os
def mtc (dor):
    os.chdir ("F:/Trash")
    os.mkdir ("Contents")
    shutil.move (dor, "F:/Trash/Contents")
    ertime = time.strftime('%Y-%m-%d_%H-%M-%S')
    os.mkdir (ertime)
    spec = ("F:/Trash/" + ertime)
    print spec
    shutil.move ("F:/Trash/Contents", spec)
def cls ():
    shutil.rmtree('F:/Trash')
    os.chdir ("F:/")
    os.mkdir ("Trash")
