inventory=dict()

while True:
        try:
            weight = input('Input max inventory weight: ')
            weight = float(weight)
            if (weight<0):
                raise ValueError
            break
        except ValueError:
            print('weight must be non-negative digit!')

while True:
   
    while True:
        try:
            command = input('\nTo exit input "e", to add item input "a", to list items input "l": ')
            if not(['e', 'l', 'a'].__contains__(command)):
                raise ValueError
            break
        except ValueError:
            print('incorrect command')  


    if (command=='a'):
        name=input('Input item name: ')
        while True:
            try:
                itemWeight = input('Input item weight: ')
                itemWeight = float(itemWeight)
                if (itemWeight<0):
                    raise ValueError
                break
            except ValueError:
                print('weight must be non-negative digit!')    
        if ( (sum(inventory.values()))+itemWeight ) <= weight:
            inventory[name]=itemWeight   
        else:
            print('Owerweight!')
    elif (command=='l'):
        print(inventory)
    else:
        break
