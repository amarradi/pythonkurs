#new recruitment


'''
1. Abgang in höhere Altersklasse als feste Variable drei mal hintereinander einfacher weg
'''
var_cops_sum = int(24000)
var_verteilung_20_to_30 = float(0.17)
var_verteilung_30_to_40 = float(0.23)
var_verteilung_40_to_50 = float(0.25)
var_verteilung_50_to_60 = float(0.35)

var_cops_20_to_30 = float((var_cops_sum * var_verteilung_20_to_30).__round__(2))
var_cops_30_to_40 = float((var_cops_sum * var_verteilung_30_to_40).__round__(2))
var_cops_40_to_50 = float((var_cops_sum * var_verteilung_40_to_50).__round__(2))
var_cops_50_to_60 = float((var_cops_sum * var_verteilung_50_to_60).__round__(2))
print("=====Stand 2017=====")
print("Gesamt:",var_cops_sum)
print("20 - 30 Jahre:",var_cops_20_to_30)

print("30 - 40 Jahre:",var_cops_30_to_40)

print("40 - 50 Jahre:",var_cops_40_to_50)

print("50 - 60 Jahre:",var_cops_50_to_60)
var_retirees = float((var_cops_50_to_60 * 0.11).__round__(2))

print("Pensionäre:", var_retirees)
var_cops_50_to_60 = var_cops_50_to_60 - (var_cops_50_to_60 * 0.11)

print("=====Stand 2018=====")
var_cops_20_to_30 = (var_cops_50_to_60 * 0.11)+ var_cops_20_to_30
print("Neueinstellung:" , var_cops_20_to_30)

print("20 - 30 Jahre Wechsel wegen Alter:", (var_cops_20_to_30 * 0.10))
var_cops_30_to_40 = var_cops_30_to_40 + (var_cops_20_to_30 * 0.10).__round__(2)
print("30 - 40 Jahre:", var_cops_30_to_40)

print("40 - 50 Jahre Wechsel wegen Alter:", (var_cops_30_to_40 * 0.10))
var_cops_40_to_50 = var_cops_40_to_50 + (var_cops_30_to_40 * 0.10).__round__(2)
print("40 - 50 Jahre:",var_cops_40_to_50)

print("50 - 60 Jahre Wechsel wegen Aler:", (var_cops_40_to_50 * 0.08))
var_cops_50_to_60 = var_cops_50_to_60 + (var_cops_40_to_50 * 0.08).__round__(2)
print("50 - 60 Jahre:",var_cops_50_to_60 )
var_retirees = float((var_cops_50_to_60 * 0.11).__round__(2))

print("Pensionäre:", var_retirees)
var_summe = float(var_cops_20_to_30+var_cops_30_to_40+var_cops_40_to_50+var_cops_50_to_60)
print("Summe Jahresstand:" ,var_summe)
print("=====Stand 2019=====")
var_cops_20_to_30 = var_retirees
print("Neueinstellung:", var_cops_20_to_30)
print("20 - 30 Jahre Wechsel wegen Alter:", (var_cops_20_to_30 * 0.10))
var_cops_30_to_40 = var_cops_30_to_40 + (var_cops_20_to_30 * 0.10).__round__(2)
print("30 - 40 Jahre:", var_cops_30_to_40)

print("40 - 50 Jahre Wechsel wegen Alter:", (var_cops_30_to_40 * 0.10))
var_cops_40_to_50 = var_cops_40_to_50 + (var_cops_30_to_40 * 0.10).__round__(2)
print("40 - 50 Jahre:",var_cops_40_to_50)

print("50 - 60 Jahre Wechsel wegen Aler:", (var_cops_40_to_50 * 0.08))
var_cops_50_to_60 = var_cops_50_to_60 + (var_cops_40_to_50 * 0.08).__round__(2)
print("50 - 60 Jahre:",var_cops_50_to_60 )
var_retirees = float((var_cops_50_to_60 * 0.11).__round__(2))

print("Pensionäre:", var_retirees)
var_summe = float(var_cops_20_to_30+var_cops_30_to_40+var_cops_40_to_50+var_cops_50_to_60)
print("Summe Jahresstand:" ,var_summe)
print("=====Stand 2020=====")
var_cops_20_to_30 = var_retirees
print("Neueinstellung:", var_cops_20_to_30)
var_cops_20_to_30 = var_cops_20_to_30 + var_retirees
print("20 - 30 Jahre Wechsel wegen Alter:", (var_cops_20_to_30 * 0.10))
var_cops_30_to_40 = var_cops_30_to_40 + (var_cops_20_to_30 * 0.10).__round__(2)
print("30 - 40 Jahre:", var_cops_30_to_40)

print("40 - 50 Jahre Wechsel wegen Alter:", (var_cops_30_to_40 * 0.10))
var_cops_40_to_50 = var_cops_40_to_50 + (var_cops_30_to_40 * 0.10).__round__(2)
print("40 - 50 Jahre:",var_cops_40_to_50)

print("50 - 60 Jahre Wechsel wegen Aler:", (var_cops_40_to_50 * 0.08))
var_cops_50_to_60 = var_cops_50_to_60 + (var_cops_40_to_50 * 0.08).__round__(2)
print("50 - 60 Jahre:",var_cops_50_to_60 )
var_retirees = float((var_cops_50_to_60 * 0.11).__round__(2))

print("Pensionäre:", var_retirees)
