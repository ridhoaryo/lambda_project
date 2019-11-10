from functools import reduce

num_list = list(range(1,101))
mantap = reduce(lambda x,y:x+y, map(lambda x:x*2, filter(lambda x:x%2==0, num_list)))
print(num_list)
print(mantap)