capital={'France':'Paris','Russia':'Moscow','England':'London','Ireland':'Dublin','Italy':'Rome','Argentina':'Buenos Aires'}
while True:
    print('Select a option')
    print('1. Insert')
    print('2. Display all countries')
    print('3. Display all capitals')
    print('4. Get Capital')
    print('5. Delete')
    print('6. Exit')
    menu=input()
    if menu=='1':
        print('Type in what you want to add. First the key')
        key=input()
        print('Now the info.')
        info=input()
        capital[key]=info   
    elif menu=='2':
        print(capital.keys())   
    elif menu=='3':
        print(capital.values())
    elif menu=='4':
        print('What contrys capital do you need?')
        cap=input()
        print(capital.get(cap))
    elif menu=='5':
        print('Which country do you want to delete?')
        dele=input()
        del capital[dele]
    elif menu=='6':
        break