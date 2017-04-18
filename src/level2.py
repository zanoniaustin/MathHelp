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

def level2():
    mul_div = random.randrange(0,2,1)
    if mul_div == 0:
        deno = random.randrange(2,11)
        if deno == 2:
            nume = random.randrange(-50,52,2)            
        elif deno == 3:
            nume = random.randrange(-45,48,3)
        elif deno == 4:
            nume = random.randrange(-44,48,4)
        elif deno == 5:
            nume = random.randrange(-100,105,5)
        elif deno == 6:
            nume = random.randrange(-66,72,6)
        elif deno == 7:
            nume = random.randrange(-77,85,7)
        elif deno == 8:
            nume = random.randrange(-88,96,8)
        elif deno == 9:
            nume = random.randrange(-99,108,9)
        elif deno == 10:
            nume = random.randrange(-1000,1010,10)
        function = str(nume) + ' / ' + str(deno) + ' = '
        realans = nume / deno
        printfun(realans,function)
    else:
        num1 = random.randrange(-10,11,1)
        num2 = random.randrange(-10,11,1)
        realans = num1 * num2
        function = str(num1) + ' * ' + str(num2) + ' = '
        printfun(realans,function)
            

for i in range(10):
    level2()

