#List fuction : 1) map 2) filters 3)reduce
import functools
#Map
print(list(map(lambda x: x**2 + 3*x + 1, [1,2,3,4])))

#Filter
print(list(filter(lambda x: x < 4, [1,2,3,4,5,4,3,2,1])))

#Reduce
print(functools.reduce(lambda x, y: x * y , [1,2,3,4]))

