##### 10/1 Interview with Amazon

def find_odd_num(A):
    N = len(A)
    counter = 0
    for i in range(1, N):
        if A[i] < 0:
            raise ''
        elif A[i] == 0:
            counter += 1
        A[0] ^= A[i]
    
    if counter % 2 == 1:
        return 0
    if A[0] == 0:
        raise 'Invalid inpu: Array'
    
    extra_num
    counter = 0
    for num in A:
        if num == extra_num:
            counter += 1
    
    
    return odd_occur_num



def find_odd_num(A):
    N = len(A)
    zero_counter = 0
    maybe_odd = A[0]
    for i in range(1, N):
        if A[i] == 0:
            zero_counter += 1
        maybe_odd ^= A[i]
    
    count_maybe = 0
    for i in range(N):
        if A[i] == maybe_odd:
            count_maybe += 1
    
    if count_maybe % 2 == 1:
        if zero_counter % 2 == 1:
            return (0, maybe_odd) # more than one odd number input. (0, maybe_odd)
        else:
            return maybe_odd
    else:                # More than one odd number input
        return 

1 2 2 3 
01    11


10

array = [0 for i in range(32)]
[0,1] 1 2 2
[1,0]

[2,2]
         [1,2,5,2,1,1,1]
         [0,0,0,0,0,0,0]

0 ^ 0 = 0
1 ^ 0 = 1