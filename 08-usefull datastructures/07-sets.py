#Sets :- collection of uniqu elements 
#Union "|" #intersection "^" #diffrence "-"
my_set = set(['one','two','three','one'])
#print(my_set)
my_set1 = set(['two','three','four'])

a = my_set - my_set1

print(a <= my_set) #subset


my_set1.add('five')
print(my_set1)
#print(my_set|my_set1) #Union
#print(my_set ^ my_set1) #intersection
#print(my_set - my_set1) #Diffrence
