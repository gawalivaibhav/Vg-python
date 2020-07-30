#Data Structure
#Dictionaries : key - value

my_dictionary = {'key':  'Value', ('K', 'E','Y'):5}
print(my_dictionary)

my_dictionary1 = {x: x+y for x in range(10)  for y in range(4)}
print(my_dictionary1)

try:
    print(my_dictionary[1])
except Exception as e:
    print(e)

my_dictionary[1] = 3
print(my_dictionary)

print(my_dictionary.skeys())
print(my_dictionary.values())

my_dictionary.clear()
#del my_dictionary[1]
print(my_dictionary)


