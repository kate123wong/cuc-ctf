import zipfile
import sys
import os.path as op

name = 'OKMIlLVft'
while True:
    path = op.join(sys.path[0],name+'.tar.gz')
    zf = zipfile.ZipFile(path)
    zf.extractall(path = sys.path[0],pwd = bytes(name,"utf8"))
    name = zf.filelist[0].filename
    name = name.split(".tar.gz")[0]