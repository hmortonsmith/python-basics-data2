# if statements work by analysing conditions

age = 1

while True:
    print('happy birthday')
    print('here is some money')
    print('you are', age)
    age += 1
    response = input('> continue? (y/n)')
    if response == 'n':
        break
    elif response == 'egg':
        print('EGGS!')
    else:
        print('cool,cool')