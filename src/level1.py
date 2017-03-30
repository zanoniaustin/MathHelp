import random

def level1():
    a = random.randrange(-10,10,1)
    b = random.randrange(-10,10,1)


    s = random.randrange(0,2,1)
    done = False
    while done == False:
        if s == 0:
            c = a + b
            print(a, ' + ', b, ' = ',end = '')
        else:
            c = a - b
            print(a, ' - ', b, ' = ',end = '')
        
        ans = input()
        if ans.isnumeric():
            done = True
            ans = int(ans)
            if ans == c:
                print("correct")
            else:
                print("incorrect")
        else:
            print("Must input numbers only.")
            done = False
    

n = 0;
for i in range(11):
    level1()


