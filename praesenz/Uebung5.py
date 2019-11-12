'''
Uebung 5

Gegeben ist ein verschlüsselter Text, bei welchem die Buchstaben um eine Stelle nach rechts verschoben sind (Caesar Chiffre)

Entschlüsseln Sie den Text mit Python:

Bei der Caesar Chiffre werden die Buchstaben eines Alphabetes auf ein Zahlenraster gemappt, danach kann um entsprechende Werte verschoben werden.
'''
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
cipherstring = "tvqfs ev ibtu ft hftdibggu ijfs jtu efs hfifjnufyu"
decipherstring = ""
for index, element in enumerate(cipherstring):
    if ord(element) != 32:
        pos = ord(element) - 1
        decipherstring = decipherstring + chr(pos)
    else:
        pos = ord(element)
        decipherstring = decipherstring + chr(32)

    print(decipherstring,"|",ord(decipherstring[index]))