



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

def avto_kirit():
    """Foydalanuvchiga avto_info funksiyasi yordamida bir nechta avtolar haqida ma'lumotlarni bitta ro'yxatga joylash imkonini beruvchi funksiya"""
    avtolar=[] # salondagi avtolar uchun bo'sh ro'yxat
    while True:
        print("\nQuyidagi ma'lumotlarni kiriting",end='')
        kompaniya=input("Ishlab chiqaruvchi: ")
        model=input("Modeli: ")
        rangi=input("Rangi: ")
        korobka=input("Korobka: ")
        yili=input("Ishlab chiqarilgan yili: ")
        narhi=input("Narhi: ")
        #Foydalanuvchi kiritdan ma'lumotlardan avto_info yordamida
        #lug'at shakllantirib, har bir lug'atni ro'yxatga qo'shamiz:
        avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narhi))
        # Yana avto qo'shish-qo'shmaslikni so'raymiz
        javob = input("Yana avto qo'shasizmi? (yes/no): ")
        if javob=='no':
            break
    return avtolar

def info_print(avto_info):
    """Avtomobillar haqida ma'lumotlar saqlangan lug'atni konsolga chiqaruvchi funksiya"""
    print(f"{avto_info['rang'].title()} {avto_info['kompaniya'].upper()} "
          f"{avto_info['model'].upper()}, {avto_info['korobka']} korobka, "
          f"{avto_info['yil']}-yil, {avto_info['narh']}$")





































