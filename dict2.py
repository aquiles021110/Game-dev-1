'''print('Type a sentance')
sentence=input()
vowels={'a':0,'e':0,'i':0,'o':0,'u':0} 
for i in sentence:
    if i in vowels:
        vowels[i]+=1
print(vowels)'''
#pangram check
'''import string
letter={}
for i in string.ascii_lowercase:
    letter[i]=0
print('Type a scentence')
sentence=input()
for i in sentence:
    if i in letter:
        letter[i]+=1
switch=True
for i in letter.values():
    if i==0:
        switch=False
print(letter)
if switch:
    print('This scentence is a panogram')
else:
    print('This is not a panagram')
'''
#Most used word
word='This is cool but other things are also very cool'
listwords=word.split()
print(listwords)
times={}.fromkeys(listwords,0)
print(times)
for i in listwords:
    if i in times:
        times[i]+=1
m=max(times.values())
print(m)
for k,v in times.items():
    if v==m:
        key=k
print('the most repeated word is',key)