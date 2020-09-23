#cantfindaclvername

import random

def check(x,y):
    if x in range(0,10) and y in range(0,10):
        return True
    else:
        return False

x=0
y=0
counter = 0
sum=0
while counter<100:
    rand=random.randint(1,4)
    if rand==1:
        if(check(x-1,y)):
            x=x-1
            y=y
            sum=sum+rand
    elif rand==2:
        if (check(x+1, y )):
            x = x+1
            y = y
            sum = sum + rand
    elif rand==3:
        if (check(x, y + 1)):
            x = x
            y = y +1
            sum = sum + rand
    elif rand==4:
        if (check(x, y - 1)):
            x = x
            y = y - 1
            sum = sum + rand
    counter=counter+1

print(counter)
print(sum/counter)


