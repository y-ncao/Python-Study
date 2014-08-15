#!/usr/bin/env python

from os import listdir
from os.path import isfile, join
import glob

file_list = glob.glob('./Leetcode/*.py')
file_list.remove('./Leetcode/__init__.py')
file_list.sort()

f = open('Combined_Solutions.md', 'wb')

for i, answer in enumerate(file_list):
    with open(answer) as file:
        title = ' '.join(answer.split('/')[-1].split('.py')[0].split('_'))
        content = file.read()
        sections = content.split("\"\"\"")
        f.write('##%d. %s\n' % (i+1,title))
        f.write(sections[1])
        f.write('\n```python')
        f.write(''.join(sections[2:]))
        f.write('```\n')
        f.write('-----\n\n')
f.close()
