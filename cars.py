# class Car:
#
#     def __init__(self,make,model,year,km=0,price=None):
#         self.make=make
#         self.model=model
#         self.year=year
#         self.price=price
#         self.__km=km
#
#     def set_price(self,price):
#         self.price=price
#
#     def add_km(self,km):
#         if km>=0:
#             self.__km+=km
#         else:
#             raise ValueError("km manfiy bolishi mumkun emas")
#
#     def get_info(self):
#         info=f"{self.make.upper()} {self.model} "
#         info += f"Narxi: {self.year} -yil, {self.__km} km yurgan"
#         if self.price:
#             info += f"Narxi:{self.price}"
#         return info
#
#     def get_km(self):
#         return self.__km


# Avvalgi darslarimizda Shaxs va Talaba klasslarini yaratgan edik.
# Shu ikki klassning xususiyatlari va metodlarini tekshiruvchi test dasturlar yoz

# class Talaba:
#     """Talaba nomli klass yaratamiz"""
#
#     def __init__(self, ism, familiya, tyil):
#         """Talabaning xususiyatlari"""
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil
#
#     def tanishtir(self):
#         print(f"Ismim {self.ism} {self.familiya}. {self.tyil} yilda tu'gilganman")
#
# talaba1=Talaba('imomaddin','iskandarov','2008')
# print(talaba1.tanishtir())

class Shaxs:
    """Shaxslar haqida ma'lumot"""

    def __init__(self, ism, familiya, passport, tyil):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil

    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
        return info

    def get_age(self, yil):
        """Shaxsning yoshini qaytaruvchi metod"""
        return yil - self.tyil

inson=Shaxs('imomaddin', 'iskandarov', 'pasport raqami MA65216169', '2008')
print(inson.get_info())
