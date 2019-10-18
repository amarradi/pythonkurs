# ROT 13

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
#var_cypher = var_decypher = ['p', 'l', 'c', 'u', 'r', 'e']
#var_cypher = var_decypher = ['m', 'a', 'r', 'c', 'u', 's']
var_cypher = var_decypher = ['z', 'n', 'e', 'p', 'h', 'f']
rot13 = int(13)
min = int(97)
max = int(122)
new = pos = int(97)
print(var_cypher)
count = int(0)
for index, i in enumerate(var_cypher):
    #print("i",count, "ist", ord(i))
    pos = ord(i) + rot13
    if  pos > max:
        new = min + (pos - max) - 1
     #   print(new, chr(new))
        var_decypher[index] = chr(new)
    else:
        var_decypher[index] = chr(pos)
    count += 1
print(var_decypher)
