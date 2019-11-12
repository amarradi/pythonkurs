'''
Aufgabe 1
'''
var_liste = list(range(0,10))

for i in var_liste:
    if(i % 2 != 0):
        print("for:",i)


i=0
#Wieso wirft das Ding denn eine index out of range
while True:
    i = i + 1
    if len(var_liste) == i:
        break
    if var_liste[i] % 2 == 0:
        continue

    print("while", var_liste[i])


i = 0
while True:
    try:
        if var_liste[i] % 2 != 0:
            print(var_liste[i])
        i += 1
    except IndexError:
        pass

i = 0
while i < 10:
    if var_liste[i] % 2 != 0:
        print(var_liste[i])
    i += 1
