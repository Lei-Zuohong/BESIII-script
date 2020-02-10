# -*- coding: UTF-8 -*-
# Public package
import os
import sys
# Private package
import headpy.hbes.hopp as hopp

# 帮助说明
if(sys.argv[1] == '-help'):
    helptext = '''
    输入 dohadd -1 整合所有能量点的root文件
    输入 dohadd ? 整个单个能量点的root文件
    '''
    print(helptext)
# 程序运行
else:
    inenergy_list = hopp.energy_list()
    # 处理所有能量点
    if(sys.argv[1] == '-1'):
        for i in inenergy_list:
            os.system('rm %1.4f.root' % (i))
            os.system('hadd %1.4f.root %1.4f_*.root' %
                      (i, i))
    elif(float(sys.argv[1]) in inenergy_list):
        i = float(sys.argv[1])
        os.system('rm %1.4f.root' % (i))
        os.system('hadd %1.4f.root %1.4f_*.root' %
                  (i, i))
    else:
        print('能量点错误')
