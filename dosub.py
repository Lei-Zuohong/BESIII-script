# -*- coding: UTF-8 -*-
# Public package
import sys
import os
# Private package
import headpy.hscreen.hprint as hprint

# 读取文件路径
hprint.pstar()
filename = sys.argv[1]
filestring = sys.argv[2]
hprint.ppoint('run file', filename)
hprint.ppoint('run code', filestring)


# 生成该文件sh
filesh = '%s.sh' % (filename)
with open(filesh, 'w') as outfile:
    output = '%s' % (filestring)
    outfile.write(output)
# 更改文件属性并提交
hprint.pline('chmod u=rwx,go=rx %s' % (filesh))
os.system('chmod u=rwx,go=rx %s' % (filesh))
hprint.pline('hep_sub %s' % (filesh))
os.system('hep_sub %s' % (filesh))
hprint.pstar()
