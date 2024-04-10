# class Animal:
#     def __init__(self, specie, an):
#         self.specie = specie
#         self.an = an
#         print(f"S-a nascut  {self.specie} în anul {self.an}.")
#
# class AnimalDomestic(Animal):
#     def __init__(self, specie, an, rasă):
#         super().__init__(specie, an)
#         self.rasă = rasă
#         print(f"Clasa părinte: Animal cu specia {self.specie}, anul {self.an}.")
#         print(f"Speciea de nefor este: {self.rasă}.")
#
#     def sunet(self):
#         raise NotImplementedError("Metoda trebuie implementată în subclasa specifică!")
#
# class Caine(AnimalDomestic):
#     def __init__(self, an, rasă):
#         super().__init__("Mamifer", an, rasă)
#
#     def sunet(self):
#         return "Ham-ham"
#
# # Adăugăm un câine în subclasa noastră
# caine = Caine(2024, "Labrador")
# print(f"Sunetul pe care îl face : {caine.sunet()}")





# class Calculator:
#     def __init__(self, numar1, numar2):
#         self.numar1 = numar1
#         self.numar2 = numar2
#
#     def efectueaza_impartire(self):
#         try:
#             rezultat = self.numar1 / self.numar2
#             print(f"Rezultatul împărțirii este: {rezultat}")
#         except TypeError as e:
#             print(f"Eroare de tip: {e}")
#         except ZeroDivisionError as e:
#             print(f"Eroare de împărțire la zero: {e}")
#
# # Exemple de utilizare a clasei Calculator
# calc = Calculator(10, 'a')  # Exemplu cu TypeError
# calc.efectueaza_impartire()
#
# calc = Calculator(10, 0)  # Exemplu cu ZeroDivisionError
# calc.efectueaza_impartire()
#
# calc = Calculator(10, 2)  # Exemplu cu împărțire reușită
# calc.efectueaza_impartire()




# class Numarator:
#     def __init__(self, start, sfarsit):
#         self.start = start
#         self.sfarsit = sfarsit
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.start <= self.sfarsit:
#             numar = self.start
#             self.start += 1
#             return numar
#         else:
#             raise StopIteration
#
# numere = Numarator(1, 5)
# for numar in numere:
#     print(numar)

# class Clasa:
#     def __init__(self, nume_clasa):
#         self.nume_clasa = nume_clasa
#         self.elevi = {}
#
#     def adauga_elevi(self, **kwargs):
#         for nume, varsta in kwargs.items():
#             self.elevi[nume] = varsta
#
#     def afiseaza_elevi(self):
#         print(f"Elevii din clasa {self.nume_clasa}:")
#         for nume, varsta in self.elevi.items():
#             print(f"Nume: {nume}, Varsta: {varsta}")
#
# # Exemplu de utilizare
# clasa_12 = Clasa("Clasa 12")
# clasa_12.adauga_elevi(John=18, Maria=17, Alex=16)
# clasa_12.afiseaza_elevi()


