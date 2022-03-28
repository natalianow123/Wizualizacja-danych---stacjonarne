# zad1
a = [x * 2 for x in range(0, 31)]


# plik = open('zad1.txt', 'w')
# for b in a:
#     plik.write(str(b))
#     plik.write('\n')
# plik.close()
# print(a)
# zad2
# plik = open('zad1.txt')
# zawartosc = plik.readlines()
# plik.close()
# print(zawartosc)
# zad3
# with open('zad3.txt', 'w') as plik:
#     for b in a:
#         plik.write(str(b))
#         plik.write('\n')
# with open('zad3.txt', 'r') as plik:
#     for a in plik:
#         print(a)

# zad4
# class NaZakupy():
#     def __init__(self, nazwa_produktu, ilosc, jednostka_miary, cena_jed):
#         self.nazwa_produktu = nazwa_produktu
#         self.ilosc = ilosc
#         self.jednostka_miary = jednostka_miary
#         self.cena_jed = cena_jed
#
#     def wyswietl_produkt(self):
#         print("{}, {} {} w cenie {}".format(self.nazwa_produktu, self.ilosc, self.jednostka_miary, self.cena_jed))
#
#     def ile_produktu(self):
#         print("{} {}".format(self.ilosc, self.jednostka_miary))
#
#     def ile_kosztuje(self):
#         return self.ilosc * self.cena_jed
#
#
# mleko = NaZakupy('mleko', 2, 'sztuki', 2.50)
# mleko.wyswietl_produkt()
# mleko.ile_produktu()
# print(mleko.ile_kosztuje())
# zad5

# class CiagArytmetyczny:
#     def __init__(self):
#         self.a1 = None
#         self.r = None
#         self.n = None
#         self.ciag = []
#
#     def wyswietl_dane(self):
#         for element in self.ciag:
#             print(element)
#
#     def pobierz_elementy(self):
#         while True:
#             wejscie = input("Podaj liczbę lub wpisz 'koniec'\n")
#             if wejscie != 'koniec':
#                 self.ciag.append(int(wejscie))
#             else:
#                 break
#
#     def pobierz_parametry(self):
#         self.a1 = int(input("Podaj pierwszy wyraz ciągu: "))
#         self.r = int(input('Podaj różnicę ciągu arytmetycznego: '))
#         self.n = int(input('Podaj ilość wyrazów ciągu arytmetycznego: '))
#
#     def policz_sume(self):
#         return sum(self.ciag)
#
#     def policz_elementy(self):
#         if (self.a1 is not None) & (self.r is not None) & (self.n is not None):
#             licznik = 0
#             suma = self.a1
#             while licznik != self.n:
#                 self.ciag.append(suma)
#                 suma += self.r
#                 licznik += 1
#
#
#
# ciag2 = CiagArytmetyczny()
# ciag2.wyswietl_dane()
# ciag2.pobierz_parametry()
# ciag2.policz_elementy()
# ciag2.wyswietl_dane()

class Robaczek:
    def __init__(self, x, y, krok):
        self.x = x
        self.y = y
        self.krok = krok

    def idz_w_gore(self, ile_krokow):
        self.x = self.x
        self.y = self.y + self.krok * ile_krokow

    def idz_w_dol(self, ile_krokow):
        self.x = self.x
        self.y = self.y - self.krok * ile_krokow

    def idz_w_lewo(self, ile_krokow):
        self.x = self.x - self.krok * ile_krokow
        self.y = self.y

    def idz_w_prawo(self, ile_krokow):
        self.x = self.x + self.krok * ile_krokow
        self.y = self.y

    def pokaz_gdzie_jestes(self):
        print("x = {}, y= {}".format(self.x, self.y))


robaczek = Robaczek(0, 0, 2)
robaczek.idz_w_gore(3)
robaczek.pokaz_gdzie_jestes()
robaczek.idz_w_lewo(3)
robaczek.pokaz_gdzie_jestes()
robaczek.idz_w_dol(3)
robaczek.pokaz_gdzie_jestes()
robaczek.idz_w_prawo(3)
robaczek.pokaz_gdzie_jestes()