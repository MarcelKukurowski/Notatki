import sys
"""
n = '2'
print(type(n))
nn = int(n)
print(type(nn))
print(nn)
"""

"""
i = input("Podaj Imie: ")
w = input("Podaj Wiek: ")

print(i,w)
print(type(i))
print(type(w))

"""

#print(sys.argv)
"""
lista = ["Marcel", 17, True, None, 12, 14, 15, 16, [1, 2]]
del lista[0]
print(len(lista))
"""

"""
slownik = {'a': 1,'b': 2,'c': 3}
print(slownik['a'])
slownik['d'] = [1, 2, 3]
print(slownik)
slownik['b'] = 4
print(slownik)"""

'''
slownik_1 = {'a': 1,'b': 2,'c': 3}
slownik_2 = {'d': 4,'e': 5,'f': 6}

print(slownik_1.get('d','Nie ma wartości'))

slownik_1.update(slownik_2)
print(slownik_1)'''


'''
krotka = ()
krotka = ('a',)
print(krotka)

krotka = (1, 'a', True, 2.39)
print(krotka)'''

'''
zbior_1 = {1, 2, 3}
zbior_2 = {2, 3, 4, 5}

print(zbior_1.intersection(zbior_2))
print(zbior_1.union(zbior_2))
print(zbior_1.difference(zbior_2))
'''

'''
for i in 'Adam':
    print(i)

for index, value in enumerate([2,5,6]):
    print(index, value)
else:
    print("Koniec")
'''

'''slownik_1 = {'a': 1,'b': 2,'c': 'x','d': 4}

for x, y in slownik_1.items():
    print(x, y)'''

'''klucze_i_wartosci = [(1, 'a'), (2, 'b'), (3, 'c')]

slownik = {klucz: wartosc for (klucz, wartosc) in klucze_i_wartosci}

print(slownik)'''

import string
letter_count = dict(zip(string.ascii_lowercase, [0]*26))
print(letter_count)






