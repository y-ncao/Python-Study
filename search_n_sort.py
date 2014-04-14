#!/usr/bin/env python
def swap(data_list, i1, i2):
    temp = data_list[i1]
    data_list[i1] = data_list[i2]
    data_list[i2] = temp

def bubble_sort(data_list):
    flag = True
    for i in range( 1, len(data_list)):
        flag = True
        for j in range( 1, len(data_list)):
            if data_list[j-1] > data_list[j]:
                flag = False
                swap(data_list, j, j-1)
                print data_list

        if flag:
            break

def selection_sort(data_list):
    for i in range( len(data_list)-1):
        for j in range( i+1, len(data_list)):
            if data_list[j] < data_list[i]:
                swap(data_list, i, j)
                print data_list

def insertion_sort(data_list):
    for i in range( len(data_list) ):
        temp = data_list[i]
        k = i
        while data_list[k-1] > temp and k > 0:
            data_list[k] = data_list[k-1]
            k -= 1
        data_list[k] = temp
        print data_list

def merge_sort(data_list, low, high):
    if low < high:
        middle = (low + high) / 2
        merge_sort(data_list, low, middle)
        merge_sort(data_list, middle+1, high)
        merge(data_list, low, middle, high)

def merge(data_list, low, middle, high):
    helper = [None] * len(data_list)
    for i in range(low, high+1):
        helper[i] = data_list[i]

    helper_left = low
    helper_right = middle + 1
    current = low

    while helper_left <= middle and helper_right <= high:
        if helper[helper_left] < helper[helper_right]:
            data_list[current] = helper[helper_left]
            helper_left += 1
        else:
            data_list[current] = helper[helper_right]
        current += 1

    remaining = middle - helper_left
    for i in range(remaining+1):
        data_list[current+i] = helper[helper_left+i]


# These are adata_listdata_list for quick sort
def quick_sort(data_list):
    pass

def partition():
    pass

#def swap():
#   pass



if __name__ == '__main__':
    import random
    data_list = []
    while True:
        rand = random.randint(0,20)
        if rand not in data_list:
            data_list.append(rand)
            if len(data_list) == 21:
                break
    print data_list
    #selection_sort(data_list)
    #bubble_sort(data_list)
    #insertion_sort(data_list)
    merge_sort(data_list, 0, len(data_list)-1)
    print data_list
