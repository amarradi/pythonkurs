VAR_BUF = 4096

var_f = open('afile.txt','r',encoding='utf-8')

while True:
    var_inhalt = var_f.read(VAR_BUF)
    if not var_inhalt.isdigit():
        break
    print (var_inhalt)

