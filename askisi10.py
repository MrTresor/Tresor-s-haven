#bombomastoras


import random
rows = int(input("dwse grammes"))
cols = int(input("dwse sthles"))
while True:
    bombs = int(input("dwse arithmo gia bombes mikrotero h iso apo rows*cols"))
    if bombs > ((rows-1)*(cols-1)):
        print("i said mikrotero")
    else:
        print("ok!")
        break
array=[]
for i in range(0,cols):
    col=[]
    for j in range(0,rows):
        col.append("block")
    array.append(col)
x=0
y=0
if bombs==cols*rows:
    for i in range(rows):
        for j in range(cols):
            array[i][j]="BomB"
else:
    while bombs>0:

        x=random.randint(0,rows)-1
        y=random.randint(0,cols)-1
        if array[x][y]=="block":
            array[x][y]="BomB"
            bombs=bombs-1
            print("bomb")

for i in range(0,len(col)):
    print(array[i])

