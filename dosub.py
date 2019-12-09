# -*- coding: UTF-8 -*-
# Public package
import sys
import os

# 读取文件路径
filename = sys.argv[1]
filestring = sys.argv[2]
# 生成该文件sh
filesh = '%s.sh' % (filename)
with open(filesh, 'w') as outfile:
    output = '%s' % (filestring)
    outfile.write(output)
# 更改文件属性并提交
os.system('chmod u=rwx,go=rx %s' % (filesh))
os.system('hep_sub %s' % (filesh))
