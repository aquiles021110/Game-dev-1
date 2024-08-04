list=[120,55,350,380,111,55,787]
s1=set(list)
print(type(s1))
s1.add('Aircraft')
print(s1)
s1.remove(55)
s1.discard(55)
#set operations
#union
a={2,4,5,1,3}
b={6,4,8,5,7}
print(a.union(b))
print(a|b)
#intersection
print(a.intersection(b))
print(a&b)
#difference
print(a.difference(b))
print(a-b)
#symmetric diff
print(a.symmetric_difference(b))
print(a^b)
