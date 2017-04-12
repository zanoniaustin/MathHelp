import random

def printfun1(num1, expo1):
    done = False
    while done == False:
        realans = pow(num1,expo1)
        print(num1, '^', expo1, ' = ',end ='')
        ans = input()
        if ans[:1] == '-' and ans[1:].isnumeric():
            done = True
            ans = int(ans)
            if ans == realans:
                print("correct")
            else:
                print("incorrect")
        elif ans.isnumeric():
            done = True
            ans = int(ans)
            if ans == realans:
                print("correct")
            else:
                print("incorrect")
        else:
            print("Must input numbers only.")

def printfun2(num1,num2,expo1,expo2,sym):
    done = False
    while done == False:
        if sym == '+':
            realans = pow(num1,expo1) + pow(num2,expo2)
            print(num1,'^',expo1,' + ',num2,'^',expo2,' = ',end='')
        else:
            realans = pow(num1,expo1) - pow(num2,expo2)
            print(num1,'^',expo1,' - ',num2,'^',expo2,' = ',end='')
        ans = input()
        if ans[:1] == '-' and ans[1:].isnumeric():
            done = True
            ans = int(ans)
            if ans == realans:
                print("correct")
            else:
                print("incorrect")
        elif ans.isnumeric():
            done = True
            ans = int(ans)
            if ans == realans:
                print("correct")
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
        printfun1(num1,expo1)
    elif switch == 1:
        printfun2(num1,num2,expo1,expo2,'+')
    else:
        printfun2(num1,num2,expo1,expo2,'-')

for i in range(10):
    level3()
