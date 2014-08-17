#!/usr/bin/env python

from os import listdir
from os.path import isfile, join
import glob

from xlrd import open_workbook

def combiner(file_list):
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

def frequency_creator(file_list):
    f = open('frequency.md', 'wb')
    f.write('##Leetcode Order by Frequency\n')
    book = open_workbook('Leetcode Order by Frequency.xlsx')
    sheet = book.sheet_by_index(0)
    """
    print sheet.nrows
    print sheet.ncols
    for i in range(1, sheet.nrows):
        if sheet.cell(i, 1).value not in
        print
    """
    for row_index in range(sheet.nrows):
        if row_index == 1:
            f.write('|---|:---:|---:|---:|---|---|\n')
        f.write('| ')
        for col_index in range(sheet.ncols):
            #print cellname(row_index,col_index),'-',
            if row_index != 0 and col_index in [0,2,3]:
                f.write(str(sheet.cell(row_index,col_index).value).split('.')[0])
            else:
                f.write(str(sheet.cell(row_index,col_index).value))
            if col_index == 5:
                f.write(' |')
            else:
                f.write(' | ')
        f.write('\n')
    f.close()


if __name__ == '__main__':
    file_list = glob.glob('./Leetcode/*.py')
    file_list.remove('./Leetcode/__init__.py')
    file_list.sort()

    #combiner(file_list)

    frequency_creator(file_list)
