#Data structure
#Tuples :- sequence of immutable objects
tup = (1,'abc,', 2, 'cdd')
tup1 = 3, 'efs', True
tup2 = 'A' # tup2 = ('A',)

print(tup)
print(tup[0])
print(tup[0:2])

tup = tup[0:3] + (5,)
print(tup)

print(5 in tup)

print(tup2 * 4)


for x in ('a', 'b', 'c'):
    print(x)


def multiple_result():
    return(1,2,'a')

print(multiple_result())

print((1,2,3) == (1,2))
a = print( [1] == [2])

print(a)

try:
    tup[3] = 5
except Exception as e:
    print(e)
