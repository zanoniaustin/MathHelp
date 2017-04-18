import random

def printfun(realans, function):
    correct = False
    while correct == False:
        done = False
        while done == False:
            print(function, end = '')
            ans = input()
            if ans[:1] == '-' and ans[1:].isnumeric():
                done = True
                ans = int(ans)
                if ans == realans:
                    print("correct")
                    correct = True
                else:
                    print("incorrect")
            elif ans.isnumeric():
                done = True
                ans = int(ans)
                if ans == realans:
                    print("correct")
                    correct = True
                else:
                    print("incorrect")
            else:
                print("Must input numbers only.")
    

def level3():
    num1 = random.randrange(-10,11,1)
    if num1 <= 5 and num1 >= -5:
        expo1 = random.randrange(0,4,1)
    else:
        expo1 = random.randrange(0,3,1)
    
    num2 = random.randrange(-10,11,1)
    if num2 <= 5 and num2 >= -5:
        expo2 = random.randrange(0,4,1)
    else:
        expo2 = random.randrange(0,3,1)
    switch = random.randrange(0,3,1)
    
    if switch == 0:
        realans = pow(num1,expo1)
        function = str(num1) + '^' + str(expo1) + ' = '
    elif switch == 1:
        realans = pow(num1,expo1) + pow(num2,expo2)
        function = str(num1) + '^' + str(expo1) + ' + ' + str(num2) + '^' + str(expo2) + ' = '
    else:
        realans = pow(num1,expo1) - pow(num2,expo2)
        function = str(num1) + '^' + str(expo1) + ' - ' + str(num2) + '^' + str(expo2) + ' = '
    printfun(realans, function)

for i in range(10):
    level3()
