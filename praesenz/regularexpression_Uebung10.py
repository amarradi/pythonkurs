'''
Schreiben Sie ein Python-Skript, dass...
10. ...eine Liste von Kreditkartennummern nach den folgenden Kriterien überprüfen
kann:
• Die Ziﬀernfolge beginnt mit einer 4,5 oder 6,
• besteht aus exakt 16 Ziﬀern,
• enthält nur Zahlen (0 bis 9),

• kann zu einer Gruppe von 4 Ziﬀern zusammengefasst werden, getrennt durch
einen Bindestrich,
• keinen anderen Trenner verwendet,
• sich keine Zahl häuﬁger als vier Mal wiederholt.
'''

import re

var_suchausdruck = r'^[4-6][9-0]{3}-?[0-9]{4}-?[0-9]{4}-?[0-9]{4}'

credit_card_nos = '''4539879182878578
4555993229951659
4556568609311652233
MasterCard:
2221001797446710
5438564231462058
2221001413232288
American Express (AMEX):
348780432251013
370357411388578
349528834169013
Discover:
6011426978300094
6011677972206741
6011062386705324555
JCB:
3543671374078505
3541167956618356
3528081514229528277
Diners Club - North America:
5456647986862122
5567309341161650
5443857703235603
Diners Club - Carte Blanche:
30348229482721
30507416862512
30029414310477
Diners Club - International:
36306238322068
36458041519040
36249555305623
Maestro:
0604986189014871
6759280774941809
0604243781004763
Visa Electron:
4508896074101247
4175-0023-7244-4684
491-70457-9761-1059
InstaPayment:
6396 4424 4495 2397
6381884537202890
6382934057115409'''

# sich keine Zahl häuﬁger als vier Mal wiederholt.

list_cc = re.findall(r'[4-6][0-9]{3}-?[0-9]{4}-?[0-9]{4}-?[0-9]{4}', credit_card_nos)
print(list_cc)
for element in list_cc:
    for i in range(0, 10):
        if len(re.findall(str(i), element)) > 4:
            list_cc.remove(element)
print(list_cc)
