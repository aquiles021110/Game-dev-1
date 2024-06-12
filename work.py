capital={'Math book':10,'English book':8,'Science book':25,'Calculators for dummies':30,'Shakespeare':14,'Chemistry':13}
while True:
    print('Select a option')
    print('1. Insert')
    print('2. Display all books')
    print('3. Display all prices')
    print('4. Get price')
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
        for i,j in capital.items():
            print(i,j)
    elif menu=='4':
        print('What book price do you need?')
        cap=input()
        print(capital.get(cap))
    elif menu=='5':
        print('Which book do you want to delete?')
        dele=input()
        del capital[dele]
    elif menu=='6':
        break