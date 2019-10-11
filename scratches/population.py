#Marcus Radisch#

var_egg = float(40)
var_grub = float(40)
var_bug = float(40)
#Test
print(var_bug,var_egg, var_grub)
var_populations = int(input("Bitte geben Sie die Anzahl der Populationen ein, die Sie berechnen möchten: "))

for x in range (1, var_populations):

    var_egg = x * (var_egg + 8)
    var_grub = x * (0.25 * var_egg)
    var_bug = x * (0.5 * var_grub)

    print("Es sind",var_egg,"Eier und",var_grub,"Larven sowie",var_bug,"Käfer")