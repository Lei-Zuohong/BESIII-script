import re
import os

content = '''
60726917.0      leizh           01/13 20:24     0+02:04:08      R  0   732.0 xboss /scratchfs/bes/leizh/opp/mc/rec/omeganpt/2.2324_03.txt
60726918.0      leizh           01/13 20:24     0+02:04:08      R  0   732.0 xboss /scratchfs/bes/leizh/opp/mc/rec/omeganpt/2.0500_00.txt
60726989.0      leizh           01/13 20:24     0+17:55:40      R  0   732.0 xboss /scratchfs/bes/leizh/opp/mc/rec/omeganpt/2.1500_04.txt
60727001.0      leizh           01/13 20:24     0+17:55:39      R  0   976.0 xboss /scratchfs/bes/leizh/opp/mc/rec/omeganpt/3.0800_04.txt
'''
with open('resub.txt', 'w') as outfile:
    outfile.write(content)
with open('resub.txt', 'r') as infile:
    contents = infile.readlines()
for i in contents:
    method = r'(.*)      leizh(.*)xboss (.*)'
    check = re.match(method, i)
    if(check):
        os.system('hep_rm %s'%(check.group(1)))
        os.system('boss.condor %s'%(check.group(3)))
