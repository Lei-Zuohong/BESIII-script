# -*- coding: UTF-8 -*-
# Public package
import os
import re
# Private package


path = os.getcwd()
method = r'(.*)/(.*Alg)/((.*Alg)-(.*)-(.*)-(.*))'
check = re.match(method, path)
if(check):
    path1 = check.group(1)
    path2 = check.group(2)
    path3 = check.group(3)
    os.chdir(path1)
    os.system('cmt create %s %s' % (path2, path3))
    os.chdir('%s/cmt' % (path))
    os.system('cmt clean')
    os.system('cmt config')
    os.system('make')
    os.system('echo DONE')
else:
    print('路径不符合')
