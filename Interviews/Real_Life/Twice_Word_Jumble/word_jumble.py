#!/usr/bin/env python

import glob
from sets import Set

def get_dict(file_list):
    dict_set  = Set([])
    for file_name in file_list:
        with open(file_name) as file:
            content = file.read()
            for word in content.split('\n'):
                if word:
                    dict_set.add(word)
    return dict_set

def get_jumble(input_string, dict_set, ret, res):
    if ''.join(res) in dict_set:
        ret.append(''.join(res))

    # Nothing left, no need to proceed
    if not input_string:
        return

    for i, char in enumerate(input_string):
        # Remove the duplicate case
        if i > 1 and char == input_string[i-1]:
            continue
        res.append(char)
        get_jumble(input_string[:i] + input_string[i+1:], dict_set, ret, res)
        res.pop()

if __name__ == '__main__':
    file_list = glob.glob('./dict/*')
    dict_set = get_dict(file_list)
    ret = []
    input_string = raw_input("Enter a jumble:").lower()

    # Sort the string to avoid duplicate
    input_string = sorted(input_string)
    get_jumble(input_string, dict_set, ret, [])
    print ret

    # The work below is irrelevant to the answer.
    print '-' * 20
    print 'This dictionary has so many single character that making me doubt my solution'
    print "So here's the proof:"

    import sh # You may need to sudo pip install sh
    import os

    cur_path = os.getcwd()
    for result in ret:
        print sh.grep('^%s$' % result, os.getcwd(), '-r')
