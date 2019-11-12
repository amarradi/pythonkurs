'''Gegeben ist die liste=[a,b] mit den Werten a=15, b=4.
Es soll folgende Listeerzeugt werden:
liste=[a,b,a*b,a/b,a^b,a%b] (Anmerkung: % = Modulo).
1. Hängen Sie die fehlenden Listenwerte an.
2. Ersetzen Sie die 3. Listenstelle mit einer Addition von a + b und die 4.Listenstelle mit einer Subtraktion von a - b.
3. Ermitteln Sie die Listenstelle mit der Modulo Rechung.
4. Entfernen Sie das letzte Element der Liste.'''
a = int(15)
b = int(4)
liste = [a,b]
liste.append(a*b)
liste.append(a/b)
liste.append(a**b)
liste.append(a%b)
print(liste)
liste[2] = a+b
liste[3] = a-b
print(liste)

print(liste.index(a%b))
liste.pop()
print(liste)