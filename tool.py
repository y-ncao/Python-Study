#!/usr/bin/env python

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
            if '\\' in sections[1]:
                new_section = sections[1].split('\n')
                min_index = len(new_section) - 1
                max_index = 0
                for i, line in enumerate(new_section):
                    if '\\' in line or '/' in line:
                        min_index = min(min_index, i)
                        max_index = max(max_index, i)
                new_section.insert(min_index - 1, '```')
                new_section.insert(max_index + 3, '```')
                f.write('\n'.join(new_section))
            else:
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

# type 1 == Data Structure, 2 == Algorithms
def type_searchor(target, type):
    book = open_workbook('Leetcode Order by Frequency.xlsx')
    sheet = book.sheet_by_index(0)
    if type == 1:
        col_index = 4
    else:
        col_index = 5
    for row_index in range(sheet.nrows):
        if target in str(sheet.cell(row_index, col_index).value):
            print str(sheet.cell(row_index, 1).value)


if __name__ == '__main__':
    file_list = glob.glob('./Leetcode/*.py')
    file_list.remove('./Leetcode/__init__.py')
    file_list.sort()
    interview_list = glob.glob('./Interviews/*.py')
    interview_list.sort()
    file_list.extend(interview_list)

    combiner(file_list)
    frequency_creator(file_list)
    #type_searchor('dp', 2)
