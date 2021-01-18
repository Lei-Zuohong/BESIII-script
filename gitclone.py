# -*- coding: UTF-8 -*-
import os
import sys
import headpy.hfile as hfile

# help
if(sys.argv[1] in ['-H', '-h', '-help']):
    output = '\n'
    output += '--u : remote git url\n'
    output += '--o : old folder\n'
    output += '--n : new folder\n'
    print(output)
    exit(0)
# option
option_list, option_dict = hfile.argv()
old_folder = option_dict['o']
new_folder = option_dict['n']
url = option_dict['u']

print('Step 1: Clone')
os.system('git clone %s' % (url))
print('Step 2: Copy')
os.system('rm -rf %s/.git' % (old_folder))
os.system('cp -r %s/* %s' % (old_folder, new_folder))
config = hfile.txt_read('%s/.git/config' % (new_folder))
config += '''
[user]
    name = Leizuohong
    email = lzh791397845@gmail.com
[credential]
    helper = store
'''
hfile.txt_write('%s/.git/config' % (new_folder), config)
os.chdir('%s' % (new_folder))
print('Step 3: Add')
os.system('git add .')
print('Step 4: Commit')
os.system('git commit -m "123"')
print('Step 5: Push')
os.system('git branch -M main')
os.system('git push -u origin main')
os.chdir('..')
os.system('mv %s %s_new' % (new_folder, old_folder))
