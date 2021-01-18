# -*- coding: UTF-8 -*-
import re
import os
import sys

method1 = sys.argv[1]

if(method1 == '-help'):
    output = '\n'
    output += '按照如下格式输入：resub 选项1 选项2 选项3\n'
    output += '选项1：处理runnumber的判据(less, bigger, all)\n'
    output += '选项2：runnumber(int)\n'
    output += '选项3：处理结果(resub, delete)\n'
    print(output)
else:
    with os.popen(r'hep_q -u', 'r') as infile:
        content = infile.read()
    method2 = sys.argv[2]
    method3 = sys.argv[3]
    lines = content.splitlines()
    num = len(lines)
    for i in lines:
        method = r'(.*)      leizh(.*)xboss (.*)'
        check = re.match(method, i)
        if(check):
            deal = bool(0)
            if(method1 == 'less'):
                deal = float(check.group(1)) < float(method2)
            if(method1 == 'bigger'):
                deal = float(check.group(1)) > float(method2)
            if(method1 == 'all'):
                deal = 1 == 1
            if(deal):
                if(method3 == 'resub'):
                    os.system('hep_rm %s' % (check.group(1)))
                    os.system('boss.condor %s' % (check.group(3)))
                if(method3 == 'delete'):
                    os.system('hep_rm %s' % (check.group(1)))
