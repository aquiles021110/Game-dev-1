import string
print('Write your sentence')
sentence=(input())
letters=[]
for i in string.ascii_lowercase:
    letters.append(i)
a=set(letters)
panagram=False
for i in a:
    if i in sentence:
        panagram=True
    else:
        panagram=False
    
if panagram:
    print('This is a panagram')
else:
    print('This is not a panagram')