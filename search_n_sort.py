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
    pass

def merge_sort(data_list):
    pass

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
    bubble_sort(data_list)
    print data_list
