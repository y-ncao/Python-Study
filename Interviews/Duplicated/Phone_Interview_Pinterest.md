#####9/15/2014 Phone Interview with Pinterest

http error log:
[2014/09/25 14:41:22] FATAL www.pintere.com/test 500
[2014/09/25 14:42:22] FATAL www.pintere.com/test 500
[2014/09/25 14:43:22] FATAL www.pintere.com/test 500
[2014/09/25 14:43:32] Warning www.pintere.com/FATAL 500

[TS] FATAL/Warning url return_code

how many FATAL errors per min
out:
14:41 1
14:42 1
14:43 2

grep -5


target_time = given
wanted_log = {}

with open some_log as log_file:
    log_data = log_file.read()
    log_data[0] 
    log_data[-1]
    do_search
    
    for line in log_data:
        data = line.split()
        time = ':'.join(data[1].split(':')[:2])
        if data[2] not in wanted_log:
            wanted_log[data[2]] = 0
        wanted_log[data[2]] += 1


for time, counter in wanted_log.iteritems():
    print time, counter
    
    
    
calculate the highest frequent word in the given file. 
file:{cat, dog, act, cat} return 3 
cat, act, Cat as the same word, 
    
            
file = []

d = {}
highest_frequent = 0
for word in file:
    tmp = sorted(word)
    if tmp not in d:
        d[tmp] = 0
    d[tmp] += 1
    highest_frequent = max(highest_frequent, d[tmp])

print highest_frequent