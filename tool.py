#!/usr/bin/env python

from os import listdir
from os.path import isfile, join
import glob

file_list = glob.glob('./Leetcode/*.py')
file_list.remove('./Leetcode/__init__.py')
file_list.sort()

f = open('solutions.md', 'wb')

for i, answer in enumerate(file_list):
    with open(answer) as file:
        title = ' '.join(answer.split('/')[-1].split('.py')[0].split('_'))
        address = title.lower().replace(' ', '-')
        content = file.read()
        sections = content.split("\"\"\"")
        f.write('##[%d. %s](https://oj.leetcode.com/problems/%s/)\n' % (i+1,title,address))
        f.write(sections[1])
        f.write('\n```python')
        f.write(''.join(sections[2:]))
        f.write('```\n')
        f.write('-----\n\n')
f.close()
