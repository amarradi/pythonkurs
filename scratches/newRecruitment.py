#new recruitment


'''
1. Abgang in höhere Altersklasse als feste Variable drei mal hintereinander einfacher weg
'''
var_cops_sum = int(24000)
var_cops_20_to_30 = float((var_cops_sum * 0.17).__round__(2))
var_cops_30_to_40 = float((var_cops_sum * 0.23).__round__(2))
var_cops_40_to_50 = float((var_cops_sum * 0.25).__round__(2))
var_cops_50_to_60 = float((var_cops_sum * 0.35).__round__(2))
print("=====Stand 2017=====")
print("Gesamt:",var_cops_sum)
print("20 - 30 Jahre:",var_cops_20_to_30)

print("30 - 40 Jahre:",var_cops_30_to_40)

print("40 - 50 Jahre:",var_cops_40_to_50)

print("50 - 60 Jahre:",var_cops_50_to_60)

print("=====Stand 2018=====")

print("20 - 30 Jahre Wechsel:",(var_cops_20_to_30 * 0.10))
var_cops_20_to_30_d = var_cops_20_to_30 - var_cops_20_to_30 * 0.10
print("30 - 40 Jahre:",var_cops_30_to_40 + (var_cops_20_to_30 * 0.10))

print("40 - 50 Jahre Wechsel:",(var_cops_30_to_40 * 0.10))
print("40 - 50 Jahre:",var_cops_40_to_50 + (var_cops_30_to_40 * 0.10))

print("50 - 60 Jahre Wechsel:",(var_cops_40_to_50 * 0.08))
print("50 - 60 Jahre:",var_cops_50_to_60 + (var_cops_40_to_50 * 0.08))
var_retirees = float((var_cops_50_to_60 * 0.11).__round__(2))
print("Pensionäre:",var_retirees)