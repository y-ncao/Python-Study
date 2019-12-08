#!/usr/bin/env python

import json
import glob
import os

from question_names import LARGE_JSON_STRING

"""
This is a script that I used to rename the filenames from no index to with index.
"""

if __name__ == '__main__':
    leetcode_data = json.loads(LARGE_JSON_STRING)
    questions = leetcode_data['stat_status_pairs']
    name_to_num_dict = {}
    for q in questions:
        name_to_num_dict[q['stat']['question__title']] = q['stat']['question_id']

    file_list = glob.glob('./Leetcode/*.py')
    cannot_finish = []
    for file in file_list:
        filename = file.split('/')[-1].split('.')[0]
        question_name = filename.replace('_', ' ')
        if question_name in name_to_num_dict:
            num = name_to_num_dict[question_name]
            new_file_name = "./Leetcode/" + str(num) + '_' + filename + ".py"
            # print(new_file_name)
            # os.rename(file, new_file_name)
        else:
            cannot_finish.append(question_name)

    print('*'*100)
    print(cannot_finish)
