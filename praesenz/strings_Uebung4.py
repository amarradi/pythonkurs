'''
Uebung 4

Oeffnen Sie die Datei films.txt. Erstellen Sie eine neue filmliste=[], fuegen Sie die Ueberschrift Filmtitel, Jahr, Sprache ein und importieren Sie die sortierten Eintrage aus films.txt.
Speichern Sie die neue filmliste in die Datei films_sortiert.txt.
'''
filmliste = 'Filmtitel, Jahr, Sprache'
output = open("output.txt", 'w', encoding="utf-8")
print(filmliste,file=output)
with open("films.txt","r",encoding="utf-8") as var_f:
    var_data = var_f.readlines()
    for index, element in enumerate(var_data):
        tmp = var_data[index].strip().split(',')
        print(tmp[2], tmp[1], tmp[0], sep=',', file=output)