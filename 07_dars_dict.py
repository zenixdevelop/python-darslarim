# talaba_0 = {
# 	'ism':"muxriddin",
# 	'fam':'amanbayev',
# 	'yosh':18
# }

# talaba_0["kurs"] = 4

# del talaba_0['kurs']

# print(talaba_0)
# print(f"Talaba {talaba_0['ism'].title()} {talaba_0["fam"].title()} "
# 	f"{2025-talaba_0['yosh']}-yil tug'ilgan, yoshi {talaba_0['yosh']} da")

# familys = {
# 	'father':{
# 	'ism':'salohiddin',
# 	'fam':'hudayqulov',
# 	'yil':1976
# 	},
# 	'mother':{
# 	'ism':'matlyuba',
# 	'fam':'hudayqulova',
# 	'yil':1982
# 	},
# 	'me':{
# 	'ism':'muxriddin',
# 	'fam':'amanbayev',
# 	'yil':2007
# 	},
# 	'brother':{
# 	'ism':'zuxriddin',
# 	'fam':'amanboyev',
# 	'yil':2009
# 	}
# }

# for kalit, qiymat  in familys.items():
# 	print(kalit.title())
# 	print(f"{qiymat['ism'].title()} {qiymat['fam'].title()}\n"
# 		f"{qiymat['yil']}-yil tug'ilgan, yoshi {2025-qiymat['yil']} da!\n")


# famliys_eat = {
# 	'father':'somsa',
# 	'mother':'honim',
# 	'brother':'shashlik',
# 	'little_bro':'norin',
# 	'me':'lavash'
# }

# for ism, eat in famliys_eat.items():
# 	print(f"{ism.title()}ning sevimli taomi {eat}")


# python_lugati = {
#     'print': 'Ekranga maʼlumot chiqarish funksiyasi',
#     'for': 'Takrorlanish (sikl) operatori',
#     'if': 'Shart operatori, agar biror narsa rost bo‘lsa ishlaydi',
#     'else': 'Agar if rost bo‘lmasa bajariladigan kod qismi',
#     'elif': 'Qo‘shimcha shart tekshirish uchun ishlatiladi',
#     'input': 'Foydalanuvchidan maʼlumot olish funksiyasi',
#     'int': 'Butun son maʼlumot turi',
#     'str': 'Matn (string) maʼlumot turi',
#     'list': 'Elementlar to‘plami, tartiblangan ro‘yxat',
#     'dict': 'Kalit-qiymat juftligidan iborat lug‘at',
#     'def': 'Funksiya eʼlon qilish kalit so‘zi',
#     'return': 'Funksiyadan qiymat qaytaradi',
#     'import': 'Tashqi modul yoki kutubxonani chaqirish',
#     'len': 'Elementlar sonini aniqlovchi funksiyasi (masalan, listda)',
#     'type': 'O‘zgaruvchining turini ko‘rsatadi'
# }


# x = input("Kalit sozni kiriting... (toliq lug'atni korish uchun 'x' ni bosing!)\n>>>").lower()
# if x == 'x':
# 	for kalit, qiymat in python_lugati.items():
# 		print(f"Kalit: {kalit}\nQiymat: {qiymat}\n")

# elif x in python_lugati:
# 	print(f"{x} sozining manosi: {python_lugati[x]}")

# else:
# 	print("Bu so'z mavjud emas!")


# kalit = input("Kalit sozni kiriting: ")

# qiymat = python_lugati.get(kalit)

# if qiymat:
# 	print(f"{kalit} sozini manosi: {qiymat}")
# elif qiymat == None:
# 	print("Bu soz lugatda mavjud emas!")


# mahsulotlar = {
# 	'olma':10000,
# 	'anor':20000,
# 	'uzum':40000,
# 	'anjir':25000,
# 	'shaftoli':30000
# }

# bozorlik = ['anor', 'uzum', 'non', 'baliq']


# for mahsulot in mahsulotlar:
# 	if mahsulot in bozorlik:
# 		print(f"{mahsulot} narxi {mahsulotlar[mahsulot]}")


# for buyum in bozorlik:
# 	if buyum not in mahsulotlar:
# 		print(f"Iltimos, dokoninggizga {buyum} ham olib keling")


# print(talaba_0.items())


# for kalit, qiymat in talaba_0.items():
#     print(f"Kalit: {kalit}\n"
#           f"Qiymat: {qiymat}\n")


# telefonlar = {
#     'ali':'iphone x',
#     'vali':'galaxy s9',
#     'olim':'mi 10 pro',
#     'orif':'nokia 3310'
# }

# for user, phone in telefonlar.items():
#     print(f"{user.title()}ning telefoni {phone}")

# malibus = []

# for x in range(10):
#     new_car = {
#         'model':'malibu',
#         'rang':None,
#         'yil':2020,
#         'narx':None,
#         'km':0,
#         'korobka':'avto'
#     }

#     malibus.append(new_car)

# for malibu in malibus[:3]:
#     malibu['rang'] = 'qizil'

# for malibu in malibus[3:6]:
#     malibu['rang'] = 'qora'

# for malibu in malibus[6:]:
#     malibu['rang'] = 'oq'
#     malibu['korobka'] = 'mehanika'

# for malibu in malibus:
#     if malibu['korobka'] == 'avto':
#         malibu['narx'] = 40000
#     else:
#         malibu['narx'] = 35000

# for malibu in malibus:
#     print(malibu)


# dastutrchilar = {
#     'ali':['python', 'css'],
#     'vali':['html', 'python', 'java'],
#     'hasan':['php', 'sql'],
#     'husan':['python', 'php'],
#     'maryam':['css', 'c#']
# }

# for ism, tillar in dastutrchilar.items():
#     print(f"\n{ism.title()} quyudagi dasturlash tillarini biladi: {tillar}")
#     for til in tillar:
#         print(f"{til.upper()}", end=" ")