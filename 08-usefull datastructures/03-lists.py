#Data Structur
# # List :- every boject has a index element

list1 = [1, 'abc', (2,3)]

print(list1)


print(list1[2][0])

print(list1 + ['4'])

print(list1 * 2)


print(2 in list1[2])

print(list1 == [1,'abc',(2,3)] )

list1.append(6)
print(list1)
print(len(list1))
list1[len(list1):] = [7]

print(list1)