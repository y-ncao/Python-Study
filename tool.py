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

def title_convert(title):
    title = str(title)
    title = title.translate(None, "()'")
    title = title.replace(', ', '-')
    return title.lower()

def frequency_creator(file_list):
    f = open('frequency.md', 'wb')
    f.write('##Leetcode Order by Frequency\n')
    book = open_workbook('Leetcode Order by Frequency.xlsx')
    sheet = book.sheet_by_index(0)

    titles = {}
    for file_name in file_list:
        title = ' '.join(file_name.split('/')[-1].split('.py')[0].split('_')).lower()
        titles[title] = file_name

    for row_index in range(sheet.nrows):
        if row_index == 1:
            f.write('|---|:---:|---:|---:|---|---|\n')
        f.write('| ')
        for col_index in range(sheet.ncols):
            if row_index != 0 and col_index in [0,2,3]:
                f.write(str(sheet.cell(row_index,col_index).value).split('.')[0])
            elif row_index != 0 and col_index == 1:
                name = str(sheet.cell(row_index, 1).value)
                file_name = titles.get(title_convert(name), None)
                link = '[%s](%s)' % (name, file_name)
                f.write(link)
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

    combiner(file_list)
    frequency_creator(file_list)
