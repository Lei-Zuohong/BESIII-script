import os
import sys
import headpy.omega as ana

# 帮助说明
if(sys.argv[1] == '-help'):
    helptext = '''
    输入 dohadd -1 整合所有能量点的root文件
    输入 dohadd ? 整个单个能量点的root文件
    '''
    print(helptext)
# 程序运行
else:
    inenergy_list = ana.energy_list()
    inname = ana.name()
    # 处理所有能量点
    if(sys.argv[1] == '-1'):
        for i in inenergy_list:
            os.system('rm %s_%s.root' % (inname, str(i)))
            os.system('hadd %s_%s.root %s_%s_*.root' %
                      (inname, str(i), inname, str(i)))
    elif(float(sys.argv[1]) in inenergy_list):
        i = float(sys.argv[1])
        os.system('rm %s_%s.root' % (inname, str(i)))
        os.system('hadd %s_%s.root %s_%s_*.root' %
                  (inname, str(i), inname, str(i)))
    else:
        print('能量点错误')
