import random

def printfun(nume, deno):
    realans = nume / deno
    done = False
    while done == False:
        print(nume,' / ',deno,' = ',end = '')
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

def level2():
    mul_div = random.randrange(0,2,1)
    if mul_div == 0:
        deno = random.randrange(2,11)
        if deno == 2:
            nume = random.randrange(-50,50,2)
            printfun(nume,deno)            
        elif deno == 3:
            nume = random.randrange(-45,45,3)
            printfun(nume,deno)
        elif deno == 4:
            nume = random.randrange(-44,44,4)
            printfun(nume,deno)
        elif deno == 5:
            nume = random.randrange(-100,100,5)
            printfun(nume,deno)
        elif deno == 6:
            nume = random.randrange(-66,66,6)
            printfun(nume,deno)
        elif deno == 7:
            nume = random.randrange(-77,77,7)
            printfun(nume,deno)
        elif deno == 8:
            nume = random.randrange(-88,88,8)
            printfun(nume,deno)
        elif deno == 9:
            nume = random.randrange(-99,99,9)
            printfun(nume,deno)
        elif deno == 10:
            nume = random.randrange(-1000,1000,10)
            printfun(nume,deno)
    else:
        num1 = random.randrange(-10,10,1)
        num2 = random.randrange(-10,10,1)
        realans = num1 * num2
        done = False
        while done == False:
            print(num1, ' * ', num2, ' = ',end = '')
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

for i in range(10):
    level2()
