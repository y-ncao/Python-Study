#!/usr/bin/env python

# Things really need to notice:
# range() function works in a triky way
# range(n) = range(0,n) = [0,1,2,...,n-1]
# but the second input is always -1, so if you want to count [n~0]
# it's range(n, -1, -1)
# NOT range(n,0,-1) or range(n-1,0,-1)

def unique_char(str):
    char_list = []
    for char in str:
        if char not in char_list:
            char_list.append(char)
        else:
            return False
    return True

def unique_char_no_list(str):
    for i in range(0, len(str)):
        for j in range(i+1, len(str)):
            if str[i] == str[j]:

                return False
    return True

def reverse_string(str):
    str_list = list(str)
    start = 0
    end = len(str)-1
    while start < end:
        tmp = str_list[end]
        str_list[end]= str_list[start]
        str_list[start] = tmp
        start += 1
        end -= 1

    return ''.join(str_list)

def permutation_1(str1, str2):
    if len(str1) != len(str2):
        return False

    if sorted(str1) != sorted(str2):
        return False

    return True

def permutation_2(str1, str2):
    char_count_1 = {}
    char_count_2 = {}
    for char in str1:
        counter = char_count_1.setdefault(char, 0)
        counter += 1
    for char in str2:
        counter = char_count_2.setdefault(char, 0)
        counter += 1
    if char_count_1 != char_count_2:
        return False
    return True

def replace_space(str):
    str_list = list(str)
    for i in range(0, len(str_list)):
        if str_list[i] == " ":
            str_list[i] = "%20"
    return ''.join(str_list)

def replace_space_back(str):
    str_list = list(str)
    for i in range(len(str_list)-1, -1, -1):
        if str_list[i] == " ":
            del str_list[i]
            str_list.insert(i ,"%20")

    return "".join(str_list)

def compress(input_str):
    str_list = []
    counter = 1
    pre = input_str[0]
    for i in range(1, len(input_str)):
        if input_str[i] == pre:
            counter += 1
            continue
        else:
            str_list.append(pre+str(counter))
            pre = input_str[i]
            counter = 1
    str_list.append(pre+str(counter))
    if len(str_list) >= len(input_str):
        return input_str
    else:
        return "".join(str_list)

def rotate_matrix(m):
    n = []
    for i in range(0, len(m[0])):
        l = []
        for row in m:
            l.append(row[i])
        n.append(l)
    return n

def zero_matrix(m):
    zero_i = []
    zero_j = []
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] == 0:
                zero_i.append(i)
                zero_j.append(j)

    for i in zero_i:
        m[i] = [0]*len(m[0])
    for j in zero_j:
        for row in m:
            row[j] = 0

    return m

def print_matrix(m):
    for i in range(0, len(m)):
        print "".join(str(m[i]))

def is_substring(s1, s2):
    if len(s1) != len(s2):
        return False

    if s2 in (s1+s1):
        return True
    else:
        return False

if __name__ == "__main__":
    string = "This is a fuckin shit"
    print unique_char(string)
    print unique_char_no_list(string)
    print 'Reverse'
    print reverse_string(string)

    print 'Permutation'
    print permutation_2('This','hsiT')

    print 'Replace Space'
    print replace_space_back(string)

    m = [ [1,0,3,4],
          [5,6,0,8],
          [9,10,11,12],
        ]
    print_matrix(m)
    print_matrix(rotate_matrix(m))

    print_matrix(zero_matrix(m))
    print 'compress'
    print compress('aabcccccaaa')

    print 'Is Substring'
    print is_substring('abcdefg', 'fgabdce')
