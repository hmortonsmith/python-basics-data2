import time
# while loops
# while loops keep iterating until a condition is broken (becomes false)
# or a control flow of IF takes you to a break clause

# syntax
# while <condition> :
    # block of code

age = 1
# while iterator with a counter
# counter must be outside loop otherwise it would reset to
while age < 18:
    print(f'you are {age}')
    print('happy birthday')
    print('here is some money')
    age += 1

# while iterator with break condition
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
