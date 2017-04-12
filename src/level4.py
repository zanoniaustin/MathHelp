import random

def add_sub_mul(num1, num2,function,trigger):
    if trigger == 0:
        switch = random.randrange(0,3,1)
    else:
        switch = random.randrange(0,2,1)
    if switch == 0:
        function = function + str(num1) + ' + ' + str(num2)
        return num1+num2,function
    elif switch == 1:
        function = function + str(num1) + ' - ' + str(num2)
        return num1-num2,function
    else:
        function = function + str(num1) + ' * ' + str(num2)
        return num1*num2,function

def printfun(function,realans):
    done = False
    while done == False:    
        print(function, end = '')
        ans = input()
        if ans[:1] == '-' and ans[1:].isnumeric():
            done = True
            ans = int(ans)
            if ans == realans:
                print('correct')
            else:
                print('incorrect')
        elif ans.isnumeric():
            done = True
            ans = int(ans)
            if ans == realans:
                print('correct')
            else:
                print('incorrect')
        else:
            print("Must input numbers only.")

def option1(num1,num2,num3):
    switch = random.randrange(0,3,1)
    if switch == 0:
        function = str(num1) + ' + ( '
        realans,function = add_sub_mul(num2,num3,function,0)
        function = function + ' ) = '
        realans = num1 + realans
    elif switch == 1:
        function = str(num1) + ' - ( '
        realans,function = add_sub_mul(num2,num3,function,0)
        function = function + ' ) = '
        realans = num1 - realans
    else:
        function = str(num1) + ' * ( '
        realans,function = add_sub_mul(num2,num3,function,1)
        function = function + ' ) = '
        realans = num1 * realans
    printfun(function,realans)
            
def option2(num1,num2,num3):
    switch = random.randrange(0,3,1)
    if switch == 0:
        function = '( ' 
        realans,function = add_sub_mul(num1,num2,function,0)
        function = function + ' ) + ' + str(num3) + ' = '
        realans = realans + num3
    elif switch == 1:
        function = '( '
        realans,function = add_sub_mul(num1,num2,function,0)
        function = function + ' ) - ' + str(num3) + ' = '
        realans = realans - num3 
    else:
        function = '( '
        realans,function = add_sub_mul(num1,num2,function,1)
        function = function + ' ) * ' + str(num3) + ' = '
        realans = realans * num3     
    printfun(function,realans)

def option3(num1,num2,num3,num4):
    switch = random.randrange(0,3,1)
    switch1 = random.randrange(0,3,1)
    if switch == 0:
        function = str(num1) + ' - ( '
        realans,function = add_sub_mul(num2,num3,function,0)
        if switch1 == 0 or switch1 == 1:
            realans = num1 + realans
    elif switch == 1:
        function = str(num1) + ' - ( '
        realans,function = add_sub_mul(num2,num3,function,0)
        if switch1 == 0 or switch1 == 1:
            realans = num1 - realans
    else:
        function = str(num1) + ' * ( '
        realans,function = add_sub_mul(num2,num3,function,1)
        realans = num1 * realans
        
    if switch1 == 0:
        function = function + ' ) + ' + str(num4) + ' = '
        realans = realans + num4
    elif switch1 == 1:
        function = function + ' ) - ' + str(num4) + ' = '
        realans = realans - num4
    else:
        function = function + ' ) * ' + str(num4) + ' = '
        if switch == 0:
            realans = num1 + (realans * num4)
        elif switch == 1:
            realans = num1 - (realans * num4)
        else:
            realans = realans * num4  
    printfun(function,realans)
    


def level4():
    option = random.randrange(1,4,1)
    num1 = random.randrange(-10,11,1)
    num2 = random.randrange(-10,11,1)
    num3 = random.randrange(-10,11,1)
    num4 = random.randrange(-10,11,1)
    if option == 1:
        option1(num1,num2,num3)
    elif option == 2:
        option2(num1,num2,num3)
    else:
        option3(num1,num2,num3,num4)


for i in range(20):
    level4()


