var=(12,)
print(type(var))
var1=tuple(['lala',True,23])
print(var1[1])
print(var+var1)#concatentaion of tuples
print(var,var1)
print(var*3)
print(var1[1:])
print(len(var1))
print(tuple('python',))
#packing
adress=('497','Rue','Cabirolet','02193','France')
num,road,name,code,country=adress
print(code)