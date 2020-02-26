import re
import os

content = '''
64964425.0      leizh           02/22 08:12     1+01:43:30      R  0   29.0 xboss /scratchfs/bes/leizh/opp/sima/omeganpw/2.9500_05.txt
64964426.0      leizh           02/22 08:12     1+01:43:30      R  0   26.0 xboss /scratchfs/bes/leizh/opp/sima/omeganpw/2.0000_03.txt

'''
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
