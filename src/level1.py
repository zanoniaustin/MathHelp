import random

def level1():
    num1 = random.randrange(-10,11,1)
    num2 = random.randrange(-10,11,1)
    add_sub = random.randrange(0,2,1)
    done = False
    while done == False:
        if add_sub == 0:
            realans = num1 + num2
            print(num1, ' + ', num2, ' = ',end = '')
        else:
            realans = num1 - num2
            print(num1, ' - ', num2, ' = ',end = '')
        
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
    



