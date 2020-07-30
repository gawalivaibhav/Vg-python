#Modules and Packages 
# import copy

# my_dict = {'key':'Value', ('K', 'E','Y'):5}

# my_dict1 = copy.deepcopy(my_dict)
# my_dict[1] = 1
# print(my_dict)
# print(my_dict1)
###############################################
import math as m
import cmath as cm
import random as ran
import sys
print(m.cos(m.pi))
print(m.exp(2))
print(m.ceil(1.6))

#print(dir(cm))
print(dir(ran))

print(ran.sample([1,2,3,4,5], 3))
print(ran.random()%10)
print(ran.randint(5,10))
# print(cm.sqrt(4))
# print(cm.polar(complex(0,1)))

#Sys

print(sys.getrecursionlimit())
print(sys.version)
print(sys.path)