import random

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
    done = False

    if switch == 0:
        while done == False:
            realans = pow(num1,expo1)
            print(num1, '^', expo1, ' = ','')
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
                done = False
    elif switch == 1:
        while done == False:
            realans = pow(num1,expo1) + pow(num2,expo2)
            print(num1,'^',expo1,' + ',num2,'^',expo2,' = ','')
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
                done = False
    else:
        while done == False:
            realans = pow(num1,expo1) - pow(num2,expo2)
            print(num1,'^',expo1,' - ',num2,'^',expo2,' = ','')
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
                done = False



    
for i in range(11):
    level3()
