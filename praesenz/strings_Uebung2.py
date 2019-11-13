"""
Uebung 2

Achten Sie ausserdem auf die Groß- und Kleinschreibung, nutzen Sie Strings-Methoden.
"""

string2 = 'tEILE EINeS coMPUter DIE hardware NENNt Man DIE MAN TretEN KANN'
print(string2)

string2 = string2.lower().split()
string2[0] = string2[0].capitalize()
string2[2] = string2[2].capitalize()
string2[4] = string2[4].capitalize()

print(string2)
