import random

def level1():
    num1 = random.randrange(-50,51,1)
    num2 = random.randrange(-50,51,1)
    add_sub = random.randrange(0,2,1)
    if add_sub == 0:
        realans = num1 + num2
        function = str(num1) + ' + ' + str(num2) + ' = '
    else:
        realans = num1 - num2
        function = str(num1) + ' - ' + str(num2) + ' = '
    
    correct = False
    while correct == False:
        done = False
        while done == False:
            print(function,end = '')
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
    
for i in range(10):
    level1()


