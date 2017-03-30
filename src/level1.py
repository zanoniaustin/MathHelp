import random

def level1(n):
    a = random.randrange(0,10,1)
    b = random.randrange(0,10,1)
    c = a + b
    print(a, ' + ', b, ' = ',end = '')
    
    ans = int(input())
    if ans == c:
        print("correct")
        n += 1
    else:
        print("incorrect")

n = 0;
for i in range(11):
    level1(n)

print(n,'/',i)
