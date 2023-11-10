# ismlar = []

#  print("Yaqin do'stlaringiz ro'yxatini tuzamiz.")
#  n=1
# while True:
#      savol = f"{n}-do'stingiz ismini kiriting:"
#      ism = input(savol)
#      ismlar.append(ism)
#      javob = input("Yana ism qo'shasizmi? (./yo'q)")
#      if javob =='.':
#         n+=1
#          continue
#      else:
#          break
#
#
#
#

# """  UY  ISHI  """


# sevimli_taom={
#     'dadam':'osh',
#     'onam':'somsa',
#     'opam':'honim',
#     'akam':'shashlik',
#     'men':'lavash'
# }
#
# print(f"\nDadamning savmli taomi {sevimli_taom['dadam']}.\
#          \nOnamning sevmli taomi {sevimli_taom['onam']}.\
#          \nAkamning sevli taomi {sevimli_taom['akam']}.")




#
# malumot={
#     'ismi':'imomaddin',
#     'familiasi':'iskandarov',
#     'kasbi':'maktab oquvchisi',
#     '1-patqursi':'Beckend dasturlash',
#     '2-patqursi':"IELTS",
#     'tug`ilgan yili':'2008',
#     'tug`ilgan oyi':"8-sentabr",
#     'yashash xonodoni':'xonqa ko`chasi 63-uy',
#     'dadasining ismi':"Umid 'shrbekjon' ",
#     'onasining ismi':'go`zal',
#     'ukasining ismi':'Samandar'
# }
#
# # print(python_i_lugat)
# malumot=input("imomaddin haqida malumot: ")
# if malumot.lower() == 'ismi':
#     berk='imomaddin'
# elif malumot.lower() == 'familiasi':
#     berk='iskandarov'
#
#     elif malumot.lower() == 'kasbi':
#         berk='maktab oquvchisi'
#
#     elif malumot.lower() == '1-patqursi':
#         berk='Backent dasturlash'
#
#     elif malumot.lower() == '2-patqursi':
#         berk="IELTS"
#
#     elif malumot.lower() == 'tug`ilgan yili':
#         berk='2008'
#
#     elif malumot.lower() == 'tug`ilgan oyi':
#      berk="8- sentabir"
#
#     elif malumo.lower() == 'yashash xonadoni':
#         berk='xonqa ko`chasi 63-uy'
#
#     elif malumot.lower() == 'dadasinig ismi':
#         berk="Umid 'sherbekjon' "
#
#     elif malumot.lower() == 'onasining ismi':
#         berk='Gozal'
#
#     elif malumot.lower() == 'ukasining ismi':
#         berk='samandar'
#
# else:
#     print("Bunday atama mavjud emas.")
# print(berk)
# ismlar = []
#
# print("Yaqin do'stlaringiz ro'yxatini tuzamiz.")
# n=1 # ismlarni sanash uchun o'zgaruvchi
# while True:
#     savol = f"{n}-do'stingiz ismini kiriting:"
#     ism = input(savol)
#     ismlar.append(ism)
#     javob = input("Yana ism qo'shasizmi? (ha/yo'q)")
#     if javob =='ha':
#         n+=1
#         continue
#     else:
#         break
#
# def salom_ber(ism):
#     """Foydalanuvchi ismini qabul qilib unga salom beruvchi funksiya"""
#     print(f"Assalomu alaykum, hurmatli {ism.title()}!")
#
# salom_ber('imomaddin')
# salom_ber('joxongir')
# salom_ber('abdulatif')
# salom_ber('anvar')
#
# print(salom_ber.__doc__)
# def toliq_ism(ism,familia):
#     """Foydalanuvchini ism familiasini jamlab jqaruvchi funksia"""
#     print(f"Foydalanuvchning ismi {ism.title()}\n"
#         f"Foydalanuvchning familiasi {familia.title()}")
# toliq_ism('olim','hakimov')
#
# def yosh_hisobla(tugilgan_yil,joriy_yil=2022):
#     """Foydalanuvchining tugilgan yilidan hisoblaydi"""
#     print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")
# yosh_hisobla(2008,2023)


# Ism_fam degan funksiya yarating. Funksiya parametrlari ism, familiya bo'lsin. Familiyaga deaulft qiymat berib keting.
# Funksiyaga bir agrumentli  hamda ikki argumentli qilib yuklab javobni chiqaring ikkala holatda

# def ism_fam(ism,familiya='iskandarov'):
#     """Foydalanuvchining ism familiyasin hisoblaydi"""
#     print(f"{ism.title()}"
#           f"{familiya.title()}")
#
# ism_fam("imomanddin")
# ism_fam("ghfghfh","fhyfhfhfy")
#
# print('salom')
# def masalani_ishlash(son):
#     a=son**2
#     b=son**3
#     print(a,b)
#
# masalani_ishlash(1)
# masalani_ishlash(2)
# masalani_ishlash(3)
# masalani_ishlash(4)
# masalani_ishlash(5)
# masalani_ishlash(6)
# masalani_ishlash(7)
# masalani_ishlash(8)
# masalani_ishlash(9)
# masalani_ishlash(10)

# def toliq_ism_yasa(ism,familya):
#     """toliq ismni qaytaruvchi funksiya"""
#     toliq_ism = f"{ism},{familya}"
#     return toliq_ism
#
# tеalaba1=toliq_ism_yasa('olim','hakimov')
# talaba2=toliq_ism_yasa('hakim','olimov')
# print(f"darska kelmagan talabalar {talaba1} {talaba2}")
# def toliq_ism_yasa(ism,familya,otasining_ismi=''):
#     """toliq ismni qaytaruvchi funksiya"""
#     if otasining_ismi:
#         toliq_ism = f"{ism} {otasining_ismi} {familya}"
#     else:
#         toliq_ism=f"{ism} {familya}"
#     return toliq_ism.title()
# talaba1=toliq_ism_yasa('olim','hakimov')
# talaba2=toliq_ism_yasa('hakim','olimov','abrorovich')
# print(f"Darsga kelmagan oquvchilar {talaba1} va {talaba2}")
#
# def avto_kompaniya(kompaniya, model, rangi, korobka, yili, narxi=None):
#     avto = {'kompaniya':kompaniya,
#             'model':model,
#             'rangi':rangi,
#             'korobka':korobka,
#             'yili':yili,
#             'narxi':narxi}
#     return avto
# avto1=avto_kompaniya('BMW','BMW 8','qora','afto','2022','110.000$')
# avto2=avto_kompaniya('Mercides','mercides E 200','oq','afato','2020','75.000$')
# avtolar=[avto1, avto2]
# print('onlayn bozorda mavjud avtomobillar:')
# for avto in avtolar:
#     if avto['narx']:
#
# def oraliq(min, max):
#     sonlar = []
#     while min<max:
#         sonlar.append(min)
#         min += 1
#     return sonlar
# print(oraliq(0,11))
# print(oraliq(10,21))
# print("Saytmizdagi avtolar royixati.")
# avtolar=[]
# while True:
#     print("\n Quydagi malumotlarni kriting")
#     kompaniya = input("ishlab chqaruvchi: ")
#     model = input("Modeli:")
#     rangi = input("rangi:")
#     karobka = input("karobka")
#     yili= input("yili")
#     narxi =input("narxi")
#
#
#     avtolar.append(avto_kompaniya(kompaniya, model, rangi, karobka, yili, narxi))
#
#     javob= input("yana avto qoshasizmi? (ha/yoq): ")
#     if javob == 'yoq':
#         break
#
# print(avtolar)

# def toliq_ism_yasa(ism, familiya):
#     """Toliq isma qaytaruvchi funksiya"""
#     toliq_ism = f"{ism} {familiya}"
#     return toliq_ism
#
# talaba1 = toliq_ism_yasa('olim','hakimov')
# talaba2 = toliq_ism_yasa('hakim','olimov')
#
# print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")
#
# def toliq_ism_yasa(ism, familiya, otasining_ismi=''):
#      """Toliq isma qaytaruvchi funksiya"""
#      if otasining_ismi: # otasining_ismi mavjudligini tekshiramiz
#          toliq_ism = f"{ism} {otasining_ismi} {familiya}"
#      else:
#          toliq_ism = f"{ism} {familiya}"
#      return toliq_ism.title()
#
#
# def a(ism, familiya, otasining_ismi=''):
#     """Toliq isma qaytaruvchi funksiya"""
#     if otasining_ismi: # otasining_ismi mavjudligini tekshiramiz
#         toliq_ism = f"{ism} {otasining_ismi} {familiya}"
#     else:
#         toliq_ism = f"{ism} {familiya}"
#     return toliq_ism.title()
#
# talaba1 = toliq_ism_yasa('olim','hakimov') #otasining_ismi kiritilmadi
# talaba2 = toliq_ism_yasa('hakim','olimov','abrorovich')
# print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")

# fibonacbhi_a=[1]
# def fibonacci(n):
#     sonlar = []
#     for x in range(n):
#         if x == 0 or x == 1:
#             sonlar.append(1)
#         else:
#             sonlar.append(sonlar[x - 1] + sonlar[x - 2])
#     return sonlar
#
#
# print(fibonacci(100))


# def tub_sonlarni_top(min, max):
#     tub_sonlar = []
#     for n in range(min, max + 1):
#         tub = True
#         if n == 1:
#             tub = False
#         elif n == 2:
#             tub = True
#         else:
#             for x in range(2, n):
#                 if n % x == 0:
#                     tub = False
#         if tub:
#             tub_sonlar.append(n)
#
#     return tub_sonlar
#
# oraliq1 = int(input("Birinchi oraliq: "))
# oraliq2 = int(input("Ikkinchi oraliq: "))
# tub_oraliq = tub_sonlarni_top(oraliq1,oraliq2)
# print(tub_oraliq)

# def bahola(ismlar):
#     baholar = {}
#     while ismlar:
#         ism = ismlar.pop()
#         baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
#         baholar[ism]=baho
#     return baholar
#
# talabalar = ['ali', 'vali', 'hasan', 'husan']
# baholar = bahola(talabalar)
# print(baholar)
#
# def katta_harf(matnlar):
#     for i in range(len(matnlar)):
#         matnlar[i]= matnlar[i].title()
#
# ismlar = ['ali','vali','hasan','husan']
# katta_harf(ismlar)
# print(ismlar)

# def katta_harf(matnlar):
#     matnlar=matnlar[:]
#     for i in range(len(matnlar)):
#         matnlar[i]=matnlar[i].title()
#     return matnlar
# ismlar = ['ali','vali','hasan','husan']
# yangi_ismlar = katta_harf(ismlar)
# print(ismlar)
# print(yangi_ismlar)

# talabalar =['ali','vali','hasan','husan']
#
# def bahola(ismlar):
#     baholar={}
#     for ism in ismlar:
#         baho=input(f"Talaba {ism.upper()}ning bahosini kriting: ")
#         baholar[ism]= baho
#     return baholar
#
# baholar = bahola (talabalar)
# print(baholar)
# print(talabalar[1].title())
#
# # Funkiyaga ro'yhat uzatib ro'yhatda uchragan vali ismini
# # birinchi harfini katta harf bilan, qolgan elementlarini hamma harfini
# # katta harf bilan chiqaring.Hamda ali ismli odamga salom yo'llang!
# #
# # a=input('ulkan daraxt binodan xam ulkan: xa/yoq')
# # while True:
# #     if a == 'xa':
# #         break
# #         print('javob togri')
#
# ismlar =['ali','vali','hasan','husan']
# def a(ismlar):
#     for ism in  ismlar

# def katta_harf(matnlar):
#     for i in range(len(matnlar)):
#         if matnlar[i] == 'vali':
#             matnlar[i] = matnlar[i].title()
#             print(f"Salom, {matnlar[i]} ")
#         else:
#             matnlar[i] = matnlar[i].upper()
#
#
# ismlar = ['ali', 'vali', 'hasan', 'husan']
# katta_harf(ismlar)
# print(ismlar)

# def summa(*sonlar):
#     """kritilagan sonlar yigingisini hisoblaydigan funnksiya"""
#     yigindi=0
#     for son in sonlar:
#         yigindi+= son
#     return yigindi
# print(summa(1,2,))
# print(summa(1,2,3,4,5,6,7,8,9,10))

# def summa(x,y,*sonlar):
#     """kritilagan sonlar yigingisini hisoblaydigan funnksiya"""
#     return x+y+sum(sonlar)
#
# print(summa(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14))

# def summa(*sonlar):
#     """kritilagan sonlar yigingisini hisoblaydigan funnksiya"""
#     return sum(sonlar)
#
# print(summa(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14))

# def avto_info(kompaniya,model,**malumotlar):
#     """Avto xaqidagi malumotlarni lugat korinishida qaytaruvchi funksiya"""
#     malumotlar[kompaniya]='kompaniya'
#     malumotlar[model]='model'
#     return malumotlar
#
# avto1 =avto_info("Tayota","SUPRA",rangi='sargich',yili='2023',)
# avto2=avto_info('BMW','BMW m8',rangi='qora')
# print(f"{avto1} \n {avto2}")

# def katta_harf(matnlar):
#     for i in range(len(matnlar)):
#         if matnlar[i] == 'vali':
#             matnlar[i] = matnlar[i].title()
#             print(f"Salom, {matnlar[i]} ")
#         else:
#             matnlar[i] = matnlar[i].upper()
#
# ismlar=['ali','vali','hasan','husan']
# katta_harf(ismlar)
# print(ismlar)

# _________________________________________________________________________________________________________
# def summa(*sonlar):
#     """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
#     yigindi = 1
#     for son in sonlar:
#         yigindi *= son
#     return yigindi
#
# print(summa(1,2))
# print(summa(1,2,3,4,5))

# ________________________________________________________________________________________
# def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
#     """Avtomobil haqidagi ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
#     avto = {'kompaniya':kompaniya,
#             'model':model,
#             'rang':rangi,
#             'korobka':korobka,
#             'yil':yili,
#             'narh':narhi}
#     return avto

# def avto_kirit():
#     """Foydalanuvchiga avto_info funksiyasi yordamida bir nechta avtolar haqida ma'lumotlarni bitta ro'yxatga joylash imkonini beruvchi funksiya"""
#     avtolar=[] # salondagi avtolar uchun bo'sh ro'yxat
#     while True:
#         print("\nQuyidagi ma'lumotlarni kiriting",end='')
#         kompaniya=input("Ishlab chiqaruvchi: ")
#         model=input("Modeli: ")
#         rangi=input("Rangi: ")
#         korobka=input("Korobka: ")
#         yili=input("Ishlab chiqarilgan yili: ")
#         narhi=input("Narhi: ")
#         #Foydalanuvchi kiritdan ma'lumotlardan avto_info yordamida
#         #lug'at shakllantirib, har bir lug'atni ro'yxatga qo'shamiz:
#         avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narhi))
#         # Yana avto qo'shish-qo'shmaslikni so'raymiz
#         javob = input("Yana avto qo'shasizmi? (yes/no): ")
#         if javob=='no':
#             break
#     return avtolar
#
# def info_print(avto_info):
#     """Avtomobillar haqida ma'lumotlar saqlangan lug'atni konsolga chiqaruvchi funksiya"""
#     print(f"{avto_info['rang'].title()} {avto_info['kompaniya'].upper()} "
#           f"{avto_info['model'].upper()}, {avto_info['korobka']} korobka, "
#           f"{avto_info['yil']}-yil, {avto_info['narh']}$")


#
# import random as r
#
# ismlar = ['olim','anvar','hasan','husan']
# ism = r.choice(ismlar) # ismlar dan tasodifiy ism tanlaymiz
# print(ism)
# print(r.choice(ism)) # ismdan tasodifiy harf tanlaymiz

# ismlar = ['hasan','husan','olim','umid']
# print(list(map(lambda matn:matn.upper(),ismlar)))

# mevalar =['olma','anor','anjir','shaftoli',"o'rik","tarvuz","qovun","banan"]
#
# mevalar_b = list(filter(lambda meva:meva.startswith('o'),mevalar))
# print(mevalar_b)
#
# mevalar2 = list(filter(lambda meva:len(meva)<=5, mevalar))
# print(mevalar2)
#

# import random as r
#
# son = r.randint(1,100)
# print(son)
# _______________________________________________________________________________________________________________
# import random as r,
#
# print("Omad show o'yiniga xush kelibsiz!")
#
# mijozlar = []
#
# print("Yaqin do'stlaringiz ro'yxatini tuzamiz.")
# n=1 # ismlarni sanash uchun o'zgaruvchi
# while True:
#     savol = f"{n}-mahsulot xarid qilgan odam raqamini kiriting: "
#     mijoz = input(savol)
#     mijozlar.append(mijoz)
#     javob = input("Yana ism qo'shasizmi? (ha/yo'q)")
#     if javob =='ha':
#         n+=1
#         continue
#     else:
#         break
#
# print(mijozlar)
#
# print(f"Hurmatli {r.choice(mijozlar)} raqam egasi sizni keyingi ko'rsatuvga taklif qilamiz!")

# ismlar = ['hasan','husan','olim','umid']
# print(list(map(lambda matn:matn.upper(),ismlar)))

# import random as r
#
# sonlar = r.sample(range(100),10)
# juft_sonlar
# def juftmmi(x):
#     """x juft bolsa True, aks holda False qaytaruvchi funksiya"""
#     return x%2==0
#
# juft_sonlar=list(filter(juftmi,sonlar))
# print(sonlar)
# print(juft_sonlar)

#
# import random as r
#
# sonlar = r.sample(range(100),10)
#
# juft_sonlar=list(filter(lambda son:son%2==0,sonlar))
#
# print(sonlar)
# print(juft_sonlar)
#
# mevalar=['olma','anor','anjir','shaftoli','orik','tarvuz','qovun','tarvuz']
# mevalar_b=list(filter(lambda meva:meva.('b'),mevalar))
# print(mevalar_b)
#
# mevalar2 = list(filter(lambda meva:len(meva)<=5,mevalar))
# if print(mevalar2)


# import random as r
#
# print("Omad show o'yiniga xush kelibsiz!")
#
# mijozlar = []
#
# print("Yaqin do'stlaringiz ro'yxatini tuzamiz.")
# n=1 # ismlarni sanash uchun o'zgaruvchi
# while True:
#     savol = f"{n}-mahsulot xarid qilgan odam raqamini kiriting: "
#     mijoz = input(savol)
#     mijozlar.append(mijoz)
#     javob = input("Yana ism qo'shasizmi? (ha/yo'q)")
#     if javob =='ha':
#         n+=1
#         continue
#     else:
#         break
#
# print(mijozlar)
#
# print(f"Hurmatli {r.choice(mijozlar)} raqam egasi sizni keyingi ko'rsatuvga taklif qilamiz!")

# class Avto:
#     __num__avto =0
#     """avti klasi"""
#     def __init__(self,make,model,rang,yil,narx):
#         self.make= make
#         self.model=model
#         self.rang=rang
#         self.yil=yil
#         self.narx=narx
#         Avto.__num__avto +=1

# avto1 = Avto("BMW","BMW m8","Qora",2020,40.000)
#
#x = 10
#
# print(type(x))
# matn = "salom"
# print(type(matn))

# def salom_ber():
#     print("Assalom alaykum")
#
# print(type(salom_ber))

# class Talaba:
#     """Klass nomli funksiya yaratamiz"""
#     def __init__(self,ism,familya,tyil):
#         """talabaning xususiyatlari"""
#         self.ism=ism
#         self.familya=familya
#         self.tyil=tyil
#
# talaba1=Talaba("imomaddin","iskqandarov",2008)
#
# print(talaba1.ism)
# print(talaba1.familya)
# print(talaba1.tyil)


# class Talaba:
#     """Klass nomli funksiya yaratamiz"""
#     def __init__(self,ism,familya,tyil):
#         """talabaning xususiyatlari"""
#         self.ism=ism
#         self.familya=familya
#         self.tyil=tyil
#
#     def tanishtir(self):
#         print(f"Ismim {self.ism} {self.familya}. {self.tyil} yilda tugilganman")
#
# talaba4 = Talaba("Imomaddin","Iskandarov",2008)
# talaba4.tanishtir()

# class Talaba:
#     """Klass nomli funksiya yaratamiz"""
#     def __init__(self,ism,familya,tyil):
#         """talabaning xususiyatlari"""
#         self.ism=ism
#         self.familya=familya
#         self.tyil=tyil
#
#     def ismini_chqar(self):
#         return f"{self.ism} "
#
#     def get_age(self,yil):
#         return yil - self.tyil
#
#     def familiasini_chqar(self):
#         return f"{self.familya}"
#
#     def ism_familaya(self):
#         return f"{self.ism} {self.familya}"
#
#     def tanishtir(self):
#         print(f"Ismim {self.ism} {self.familya}. {self.tyil} yilda tugilganman")
#
#
# taltalaba4 = Talaba("Imomaddin","Iskandarov",2008)
# print(taltalaba4.familiasini_chqar())
# # _____________________________________________________________________________________________________________
# class User:
#     def __init__(self, name, username, email):
#         self.ismingiz = name
#         self.login = username
#         self.parol = email
#
#     def get_name(self):
#         return f"sizning ismingiz{self.name}"
#
#     def get_mail(self):
#         return f"sizning emailingiz{self.mail}"
#
#     def get_uname(self):
#         return f"sizning unamemiz {self.uname}"
#
# Malumot = User(f"Imomaddin", "imomaddiniskandarov@gmail.com", "imomaddin08")
#
# print(f"ismi: {Malumot.ismingiz}. login: {Malumot.login}. login parolio: {Malumot.parol}")
# print(Malumot.login)
# print(Malumot.parol)
#
# class Talaba:
#     """Talaba nomli klass yaratamiz"""
#     def __init__(self,ism,familiya,tyil):
#         """Tqlabalarning xususiyatlari"""
#         self.ism=ism
#         self.familiya=familiya
#         self.tyil=tyil
#         self.bosqich=1
#
#     def get_info(self):
#         return f"{self.ism} {self.familiya}. {self.tyil} {self.bosqich}-bosqich talabasi"
#
# talaba1=Talaba(f"imomaddin","iskandarov","2008",)
# print(talaba1.get_info())
#
# talaba1.bosqich=2
# print(talaba1.bosqich)

# class Talaba:
#     """Talaba nomli klass yaratamiz"""
#     def __init__(self,ism,familiya,tyil):
#         """Tqlabalarning xususiyatlari"""
#         self.ism=ism
#         self.familiya=familiya
#         self.tyil=tyil
#         self.bosqich=1
#
#     def get_info(self):
#         return f"{self.ism} {self.familiya}. {self.tyil} {self.bosqich}-bosqich talabasi bolishi mumkun"
#
#     def get_name(self):
#         """Talabaning ismini qaytaradi"""
#         return self.ism
#
#     def get_lastname(self):
#         """Talabaning familiyasini qaytaradi"""
#         return self.familiya
#
#     def get_fullname(self):
#         """Talabaning ism-familiyasini qaytaradi"""
#         return f"{self.ism} {self.familiya}"
#
#     def get_age(self, yil):
#         """Talabaning yoshini qaytaradi"""
#         return yil - self.tyil
#
#
# talaba1 = Talaba(f"imomaddin", "iskandarov", "2008", )
#
# print(talaba1.get_info())

# talaba1.update_bosqich()
# print(talaba1.get_info())
#
# talaba1.update_bosqich()
# print(talaba1.get_info())
#
# class Fan():
#     def __init__(self,nomi):
#         self.nomi=nomi
#         self.talabalar_soni=0
#         self.talabalar=[]
#
#     def add_student(self,talaba):
#         self.talabalar.append(talaba)
#         self.talabalar_soni += 1
#
#     def get_name(self):
#         """Fan nomi"""
#         return self.nomi
#
#     def get_students(self):
#         """Fanga yozilgan talabalar haqida ma'lumot"""
#         return [x.get_info() for x in self.talabalar]
#
#     def get_students_num(self):
#         """Fanga yozilgan talabalar soni"""
#         return self.talabalar_soni
#
# matematika = Fan("Oliy matematika")
# talaba1 =Talaba('Alijon','Valiyev',2000)
# talaba2=Talaba('Hasan','Alimov',2001)
# talaba3=Talaba('Akrom',"Boriyev",2001)
#
# matematika.add_student(talaba1)
# matematika.add_student(talaba2)
# matematika.add_student(talaba3)
#
# mat_talabalar = matematika.get_students()
# print(mat_talabalar)

# class Avto:
#     def __init__(self,model,rang,karopka,narx):
#         self.model=model
#         self.rang=rang
#         self.karopka=karopka
#         self.narx=narx
#         self.kilometr=0
#
#     def get_info(self):
#         return f"{self.model} {self.rang} rangli {self.karopka}-karobkali {self.narx} {self.kilometr}-kilometr yurgan"
#
#     def set_kilometr(self,kilometr):
#         self.kilometr=kilometr
#
#     def update_kilometr(self):
#         self.kilometr +=10
#
# avto_salon=Avto('BMW',"qora","avtomat","110.000$")
# print(avto_salon.get_info())
#
# avto_salon.update_kilometr()
# print(avto_salon.get_info())
#
# avto_salon.update_kilometr()
# print(avto_salon.get_info())
#
# avto_salon.update_kilometr()
# print(avto_salon.get_info())
#
#
# avto_salon.update_kilometr()
# print(avto_salon.get_info())
#
#
# avto_salon.update_kilometr()
# print(avto_salon.get_info())
#
#
# avto_salon.update_kilometr()
# print(avto_salon.get_info())
#
#
# avto_salon.update_kilometr()
# print(avto_salon.get_info())
#
#
# avto_salon.update_kilometr()
# print(avto_salon.get_info())
#
# class Shaxs:
#     """shaxslar xaqida malumot"""
#     def __init__(self,ism,familiya,pasport,tyil):
#         self.ism=ism
#         self.familiya=familiya
#         self.pasport=pasport
#         self.tyil=tyil
#
#     def get_info(self):
#         """shaxs xaqida malumot"""
#         info =f"{self.ism} {self.familiya}."
#         info +=f"passport:{self.pasport}, {self.tyil}-yilda tugilgan"
#         return info
#
#     def get_age(self,yil):
#         return yil- self.tyil
#
# # Inson = Shaxs("Hasan","Alimov","IO08092008",2008)
# # print(f"{Inson.get_info()}. {Inson.get_age(2023)} yoshda")
#
# class Talaba(Shaxs):
#     """Talaba klassi"""
#     def __init__(self,ism,familiya,pasport,tyil,idraqam,manzil):
#         """Talabani xususiyatlari"""
#         super().__init__(ism,familiya,pasport,tyil)
#         self.idraqam=idraqam
#         self.bosqich=1
#         self.manzil=manzil
#
#     def get_bosqich(self):
#         """talabaning oqish bosqichi"""
#         return self.bosqich
#
#     def get_info(self):
#         """talaba xaqida malumot"""
#         info =f"{self.ism} {self.familiya}."
#         info+=f"{self.get_bosqich()}-bosqich.ID raqami:{self.idraqam}"
#         return  info

# talaba=Talaba('imomaddin','iskandarov','CI6513665','2008',65312136565)
# print(talaba.get_info())

# class Manzil:
#     """Manzil saqlash uchun klass"""
#
#     def __init__(self, uy, kocha, tuman, viloyat):
#         """Manzil xususiyatlari"""
#         self.uy = uy
#         self.kocha = kocha
#         self.tuman = tuman
#         self.viloyat = viloyat
#
#     def get_manzil(self):
#         """Manzilni ko'rish"""
#         manzil = f"{self.viloyat} viloyati, {self.tuman} tumani, "
#         manzil += f"{self.kocha} ko'chasi, {self.uy}-uy"
#         return manzil
# talaba_manzil= Manzil(12,"olmazor","bogbon","xorazm")
# talaba = Talaba("Valijon","Aliyev","JK6146351",2000,"62363143636814",talaba_manzil)
#
# print(talaba.manzil.get_manzil())
#
#
#
#
# class Foydalanuvchi:
#     def __init__(self,ism,familiya,tyil):
#         self.ism=ism
#         self.familiya=familiya
#         self.tyil=tyil
#
#     def get_info(self):
#         info=f"{self.ism} {self.familiya}, {self.tyil}-yil"
#         return info
#
# foydalanuvchi=Foydalanuvchi('Imomaddin','Iskandarov',2008)
# print(foydalanuvchi.get_info())
#
# class Admin(Foydalanuvchi):
#     def __init__(self,ism,familiya,tyil,teshkiruvchi):
#         super().__init__(ism,familiya,tyil)
#         self.teshkiruvchi=teshkiruvchi
#
#     def ban_user(self):
#         return f"Foydalanuvchi {foydalanuvchi.get_info()} bloklandi."
#
# admin=Admin('Vali','Aliyev','2003','internet admini')
# print(admin.get_info())
# print(admin.ban_user())

#
#
# class Foydalanuvchi:
#     def __init__(self,ism,familiya,tyil):
#         self.ism=ism
#         self.familiya=familiya
#         self.tyil=tyil
#
#     def get_info(self):
#         info=f"{self.ism} {self.familiya}, {self.tyil}-yil"
#         return info
#
# foydalanuvchi=Foydalanuvchi('Imomaddin','Iskandarov',2008)
# print(foydalanuvchi.get_info())
#
# class Admin(Foydalanuvchi):
#     def __init__(self,ism,familiya,tyil,teshkiruvchi):
#         super().__init__(ism,familiya,tyil)
#         self.teshkiruvchi=teshkiruvchi
#
#     def ban_user(self):
#         return f"Foydalanuvchi {foydalanuvchi.get_info()} bloklandi."
#
# admin=Admin('Vali','Aliyev','2003','internet admini')
# print(admin.get_info())
# print(admin.ban_user())
# 1

# print(talaba.manzil.get_manzil())

# class Foydalanuvchi:
#     def __init__(self,ism,familiya,tyil):
#         self.ism=ism
#         self.familiya=familiya
#         self.tyil=tyil
#
#     def get_info(self):
#         info=f"{self.ism} {self.familiya}, {self.tyil}-yil"
#         return info
#
# foydalanuvchi=Foydalanuvchi('Imomaddin','Iskandarov',2008)
# print(foydalanuvchi.get_info())
#
# class Admin(Foydalanuvchi):
#     def __init__(self,ism,familiya,tyil,teshkiruvchi):
#         super().__init__(ism,familiya,tyil)
#         self.teshkiruvchi=teshkiruvchi
#
#     def ban_user(self):
#         return f"Foydalanuvchi {foydalanuvchi.get_info()} bloklandi."
#
# admin=Admin('Vali','Aliyev','2003','internet admini')
# print(admin.get_info())
# print(admin.ban_user())

#
# from uuid import uuid4

# class Avto:
#
#     def __init__(self,make,model,rang,yil,narx,km=0):
#         self.make=make
#         self.model=model
#         self.rang=rang
#         self.yil=yil
#         self.narx=narx
#         self.__km=km
#         self.__id=uuid4()
#
#     def get_km(self):
#         return self.__km
#
#     def get_id(self):
#         return self.__id
#
#     def add_km(self,km):
#         if km >= 0:
#             self.__km += km
#         else:
#             print("mashina km ozgartirib bolmaydi")
#
#
# avto1= Avto('GM','Tahoye','qora',2022,52000,100)
# avto1.add_km(15000)
# # print(f"ID:{avto1.get_id()}")
# print(f"KM:{avto1.get_km()}")

# class Avto:
#     """Avbur"""
#     num_avto=0
#     def __init__(self,make,model,rang,yil,narx,km=0):
#         self.make=make
#         self.model=model
#         self.rang=rang
#         self.yil=yil
#         self.narx=narx
#         self.__km =km
#         self.__id=uuid4()
#         Avto.num_avto += 1

#     @classmethod
#     def get_num_avto(cls):
#         return cls.num_avto
#
#
# avto1 = Avto('GM', 'Tahoye', 'qora', 2022, 52000, 100)
# avto2= Avto('GM','Tahoye','qora',2022,52000,100)
# avto3= Avto('GM','Tahoye','qora',2022,52000,100)
# avto4= Avto('GM','Tahoye','qora',2022,52000,100)
# avto5= Avto('GM','Tahoye','qora',2022,52000,100)
# avto6= Avto('GM','Tahoye','qora',2022,52000,100)
# avto9= Avto('GM','Tahoye','qora',2022,52000,100)
#
#
# print(f"{avto9.get_num_avto()} ta avtomobil bor")

# class Avto:
#     """Avbur"""
#     num_avto=0
#     def __init__(self,make,model,rang,yil,narx,km=0):
#         self.make=make
#         self.model=model
#         self.rang=rang
#         self.yil=yil
#         self.narx=narx
#         self.__km =km
#         self.__id=uuid4()
#         Avto.num_avto += 1
#
#     def __repr__(self):
#         return f"Avto: {self.rang} {self.make} {self.model}"
#
# avto1=Avto('GM','Tahoye','qora',2022,52000,100)
# print(avto1)

# Avvalgi darslarimizda yaratgan Shaxs va Talaba klasslariga yopiq xususiyatlar qo'shing va ularning qiymatini ko'rsatuvchi va o'zgartiruvchi metodlar yozing.
# Yuqoridagi klasslarga talabalar_soni va odamlar_soni degan klassga oid xususiyatlar qo'shing.
# Klassga oid xususiyatlar bilan ishlash uchun maxsus @classmethod lar yozing


from uuid import uuid4
# class Talaba:
#     """Talaba nomli klass yaratamiz"""
#     def __init__(self,ism,familiya,tyil,coraklik_foyizi):
#         """Tqlabalarning xususiyatlari"""
#         self.ism=ism
#         self.familiya=familiya
#         self.tyil=tyil
#         self.__choraklik_foyizi=coraklik_foyizi
#         self.__pasport_ID=uuid4()
#
#     def get_choraklik_foyizi(self):
#         return self.__choraklik_foyizi
#
#     def get_id(self):
#         return self.__pasport_ID
#
#     def add_choraklik_foyizi(self,choraklik_foyizi):
#         if choraklik_foyizi<=1000:
#             print("foyiz qabul qilindi")
#         else:
#             print("choraklik foyizini kopaytirib bolmaydi")
#
#
# talaba1 = Talaba("imomaddin", "iskandarov", "2008","")
#
# talaba1.add_choraklik_foyizi(459)
# print(talaba1.get_choraklik_foyizi())

class Shaxs:
    def __init__(self,ism,familiya,tyil,manzil):
        self.ism = ism
        self.familiya=familiya
        self.__pasport=uuid4()
        self.tyil=tyil
        self.__choraklik_foyizi=coraklik_foyizi
        self.__pasport_ID=uuid4()

    def get_choraklik_foyizi(self):
        return self.__choraklik_foyizi

    def get_id(self):
        return self.__pasport_ID

    def get_info(self):
        info=f"{self.ism} {self.familiya}, {self.tyil}-yil"
        return info
    def add_choraklik_foyizi(self,choraklik_foyizi):
        if choraklik_foyizi<=1000:
            print("foyiz qabul qilindi")
        else:
            print("choraklik foyizini kopaytirib bolmaydi")

print(foydalanuvchi.get_info())

class Admin(Foydalanuvchi):
    def __init__(self,ism,familiya,tyil,teshkiruvchi):
        super().__init__(ism,familiya,tyil)
        self.teshkiruvchi=teshkiruvchi
talaba1 = Talaba("imomaddin", "iskandarov", "2008","")

    def ban_user(self):
        return f"Foydalanuvchi {foydalanuvchi.get_info()} bloklandi."
talaba1.add_choraklik_foyizi(459)
print(talaba1.get_choraklik_foyizi())

admin=Admin('Vali','Aliyev','2003','internet admini')
print(admin.get_info())
print(admin.ban_user())
1        self.manzil=manzil


    def get_idraqam(self):
        return self.__idraqam

    def get_pasport(self):
        return self.__pasport

inson=Shaxs('imomaddin','iskandarov',2008,'xonqa63')
print(f"shaxsning  ID raqami{inson.get_idraqam()}")
print(f"pasport ID raqami{inson.get_pasport()}")