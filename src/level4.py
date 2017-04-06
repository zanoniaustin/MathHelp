import random

def add_sub_mul(num1, num2):
    switch = random.randrange(0,3,1)
    if switch == 0:
        print(num1, ' + ', num2,end = '')
        return num1 + num2
    elif switch == 1:
        print(num1, ' - ', num2,end = '')
        return num1 - num2
    else:
        print(num1, ' * ', num2,end='')
        return num1*num2

def option1(num1,num2,num3):
    switch = random.randrange(0,3,1)
    if switch == 0:
        print(num1,' + ( ', end = '')
        realans = add_sub_mul(num2,num3)
        print(') = ', end = '')
        realans = num1 + realans
    elif switch == 1:
        print(num1,' - ( ', end = '')
        realans = add_sub_mul(num2,num3)
        print(') = ', end = '')
        realans = num1 - realans
    else:
        print(num1,' * ( ', end = '')
        realans = add_sub_mul(num2,num3)
        print(') = ', end = '')
        realans = num1 * realans
    ans = int(input())
    if ans == realans:
        print('correct')
    else:
        print('incorrect')


def option2(num1,num2,num3):
    switch = random.randrange(0,3,1)
    if switch == 0:
        print('( ', end = '')
        realans = add_sub_mul(num1,num2)
        print(') + ',num3, ' = ', end = '')
        realans = realans + num3
    elif switch == 1:
        print('( ', end = '')
        realans = add_sub_mul(num1,num2)
        print(') - ',num3, ' = ', end = '')
        realans = realans - num3 
    else:
        print('( ', end = '')
        realans = add_sub_mul(num1,num2)
        print(') * ',num3, ' = ', end = '')
        realans = realans * num3     
    ans = int(input())
    if ans == realans:
        print('correct')
    else:
        print('incorrect')

def option3(num1,num2,num3,num4):
    switch = random.randrange(0,3,1)
    switch1 = random.randrange(0,3,1)        
    if switch == 0:
        print(num1, ' + ( ', end = '')
        realans = add_sub_mul(num2,num3)
        if switch1 == 0 or switch1 == 1:
            realans = num1 + realans
    elif switch == 1:
        print(num1, ' - ( ', end = '')
        realans = add_sub_mul(num2,num3)
        if switch1 == 0 or switch1 == 1:
            realans = num1 - realans
    else:
        print(num1, ' * ( ', end = '')
        realans = add_sub_mul(num2,num3)
        realans = num1 * realans
        
    if switch1 == 0:
        print(') + ',num4,' = ', end = '')
        realans = realans + num4
    elif switch1 == 1:
        print(') - ',num4,' = ', end = '')
        realans = realans - num4
    else:
        print(') * ',num4,' = ', end = '')
        if switch == 0:
            realans = num1 + (realans * num4)
        elif switch == 1:
            realans = num1 - (realans * num4)
        else:
            realans = realans * num4  
    ans = int(input())
    if ans == realans:
        print('correct')
    else:
        print('incorrect')
    


def level4():
    option = random.randrange(1,4,1)
    num1 = random.randrange(0,11,1)
    num2 = random.randrange(0,11,1)
    num3 = random.randrange(0,11,1)
    num4 = random.randrange(0,11,1)
    option = 3
    if option == 1:
        option1(num1,num2,num3)
    elif option == 2:
        option2(num1,num2,num3)
    else:
        option3(num1,num2,num3,num4)


for i in range(20):
    level4()


