import re
import os

content = '''
80374418.0      leizh           06/10 13:19     0+06:08:14      R  0   21.0 xboss /scratchfs/bes/leizh/opp/backa/script/2.0500_007.txt
80374436.0      leizh           06/10 13:19     0+06:07:40      R  0   146.0 xboss /scratchfs/bes/leizh/opp/backa/script/2.1250_004.txt
80374437.0      leizh           06/10 13:19     0+06:07:09      R  0   122.0 xboss /scratchfs/bes/leizh/opp/backa/script/2.1250_005.txt
80374440.0      leizh           06/10 13:19     0+06:07:08      R  0   122.0 xboss /scratchfs/bes/leizh/opp/backa/script/2.1250_008.txt
80374544.0      leizh           06/10 13:20     0+06:05:17      R  0   146.0 xboss /scratchfs/bes/leizh/opp/backa/script/2.9000_003.txt
80374545.0      leizh           06/10 13:20     0+06:05:14      R  0   146.0 xboss /scratchfs/bes/leizh/opp/backa/script/2.9000_004.txt
80374608.0      leizh           06/10 13:20     0+06:04:39      R  0   146.0 xboss /scratchfs/bes/leizh/opp/backa/script/3.0800_009.txt'''
with open('resub.txt', 'w') as outfile:
    outfile.write(content)
with open('resub.txt', 'r') as infile:
    contents = infile.readlines()
for i in contents:
    method = r'(.*)      leizh(.*)xboss (.*)'
    check = re.match(method, i)
    if(check):
        os.system('hep_rm %s' % (check.group(1)))
        os.system('boss.condor %s' % (check.group(3)))
