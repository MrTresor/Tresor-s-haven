#sos_game

import random as rn

choice=["S","O"]
rows, cols = (10,10)
array = []

#creating the random S n O filled 2d array
for i in range(cols):
    col = []
    for j in range(rows):
        col.append(rn.choice(choice))
    array.append(col)
for i in range(10):
  print(array[i])

def check(i,j):
    if (i in range (0,10)) and (j in range (0,10)):
        return True
    else:
        return False

counter = 0
for i in range(0,10):
    for j in range(0,10):
        if ((check(i,j+1)) and (check(i,j+2))):
            phrase = array[i][j]+array[i][j+1]+array[i][j+2]
            print(phrase)
            if phrase=="SOS":
                counter = counter +1

        if ((check(i+1,j)) and (check(i+2,j))):
            phrase = array[i][j]+array[i+1][j]+array[i+2][j]
            print(phrase)
            if phrase=="SOS":
                counter = counter +1
        if ((check(i+1,j+1)) and (check(i+2,j+2))):
            phrase = array[i][j]+array[i+1][j+1]+array[i+2][j+2]
            print(phrase)
            if phrase=="SOS":
                counter = counter +1


for i in range(10):
  print(array[i])

print(counter)