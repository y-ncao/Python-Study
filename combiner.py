#!/usr/bin/env python

from os import listdir
from os.path import isfile, join

#file_list = [ f for f in listdir('./Leetcode') if isfile(join('./Leetcode',f)) ]
import glob
file_list = glob.glob('./Leetcode/*.py')
file_list.remove('./Leetcode/__init__.py')

f = open('Combine.md', 'wb')

for answer in file_list:
    with open(answer) as file:
        title = ' '.join(answer.split('/')[-1].strip('.py').split('_'))
        content = file.read()
        sections = content.split("\"\"\"")
        f.write('##%s\n' % title)
        f.write(sections[1])
        f.write('```python\n')
        f.write(''.join(sections[2:]))
        f.write('```\n')
        f.write('-----\n\n')
f.close()
