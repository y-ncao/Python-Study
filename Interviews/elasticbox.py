string = '7 + 8 - 19 - 5 + 10'

8 - 19 - 5

def get_result(str):
  N = len(str)
  ret = 0
  num = [0,1,2,3,4,5,6,7,8,9,]
  for i in range(N):
    if str[i] == ' ':
      continue
    if str[i] in num
    
-/+
str.split('+')

# 1. digit, check previous char, 1. digit, add it to new one   2. stop, this is a num
# 2. space, continue, don't care
# 3. operator, -, -num, +, +num
     sum(all number)

def get_result(str):
  plus = str.split('+')
  sum = 0
  minus = []
  for el in plus:
    try:
      num = int(el)
    except Error:
      minus.append(el)
    else:
      sum += num
      
  for el in minus:
    piece = el.split('-')
    result = piece[0]
    for i, num in enumerate(piece, 1):
      result 
      if i == 0:
        sum += int(num)
      else:
        sum -= int(num)
        
  return sum
  
  
+8 
find_next_num()
