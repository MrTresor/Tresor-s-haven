#parta tretra-liza kai kanta korniza XD
import random
rows=10
cols=10
array=[]
returnlist=[]
eutheia=""
katheta=""
diagonia=""
choice=["0","1"]
list=[]
counter=0
for i in range(rows):
    col=[]
    for j in range(cols):
        col.append("x")
    array.append(col)
def check(phrase):
    if phrase=="1111" or phrase=="0000":
        return True
    else:
        return False
def occasion(i,j):
    i=i+3
    j=j+3
    if (i in range(10))and(j in range(10)):
        return "k1"
    elif(i in range(10))and(j not in range(10)):
        return "k2"
    elif (i not in range(10)) and (j in range(10)):
        return "k3"
    elif (i not in range(10)) and (j not in range(10)):
        return "k4"
def checkmove(array):
    for i in range(10):
        for j in range(10):
            case=occasion(i,j)

            if case=="k1":
                eutheia=array[i][j]+array[i][j+1]+array[i][j+2]+array[i][j+3]
                katheta=array[i][j]+array[i+1][j]+array[i+2][j]+array[i+3][j]
                diagonia=array[i][j]+array[i+1][j+1]+array[i+2][j+2]+array[i+3][j+3]
            elif case=="k2":
                katheta=array[i][j]+array[i+1][j]+array[i+2][j]+array[i+3][j]
                eutheia=""
                diagonia=""
            elif case=="k3":
                eutheia = array[i][j] + array[i][j + 1] + array[i][j + 2] + array[i][j + 3]
                katheta=""
                diagonia=""
            if check(eutheia)==True or check(katheta)==True or check(diagonia)==True:
                return True
            else:
                return False

end=False
while end==False:
    i = 0
    while i in range(10):
        j = 0
        while j in range(10):
            array[i][j] = random.choice(choice)
            counter=counter+1
            if checkmove(array)==True:
                end=True
                print("found")
                i=100
                j=200
                break
            j=j+1
        i=i+1

    if array[9][9]!="x" and end==False:
        array=[]
        for i in range(10):
            col=[]
            for j in range(10):
                col.append("x")
            array.append(col)

for i in range(cols):
    print(array[i])
print("χρειαστηκαν,",counter," αριθμοι για να βρεθει!")