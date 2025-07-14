# yosh = int(input("Yoshingiz nechida??\n>>>"))

# if yosh <= 4 or yosh >= 55:
#     narx = 0
# elif yosh <= 12:
#     narx = 5000
# else:
#     narx = 10000

# print(f"Sizga kirish narxi: {narx} so'm")



# kun = input("Bugun nima kun?\n>>>")

# if kun.lower() == 'shanba' or kun.lower() == 'yakshanba':
#     print("Bugun dam olish kuni!")
# else:
#     print("Bugun ish kuni!")



# kun = input("Bugun nima kun?\n>>>")
# temp = float(input("Havo harorati qanday?\n>>>"))

# if (kun.lower() == 'yakshanba' or kun.lower() == 'shanba') and temp >= 30:
#     print("Ketdik cho'milgani")
# elif (kun.lower() == 'yakshanba' or kun.lower() == 'shanba') and temp < 30:
#     print("Uyda dam olamiz!")


# narx = 15000
# choy = True
# salat = False

# if choy and salat:
#     narx =narx + 10000
# elif choy or salat:
#     narx =narx + 5000
# print(f"Jami narx: {narx} so'm")

# narx = 0
# choy = True
# salat = False
# non = False
# kompot = True
# assorti = False

# if choy:
#     narx += 5000
# if salat:
#     narx += 10000
# if non:
#     narx += 2500
# if kompot:
#     narx += 6000
# if assorti:
#     narx += 12000

# print(f"Jami: {narx} so'm")


# taomlar = ['osh', 'qazonkabob', 'shashlik', 'norin', 'somsa', 'manti']
# # print('manti' in taomlar)

# buyurtma = input("Nima ovqat yeysiz?\n>>>")
# if buyurtma.lower() in taomlar:
#     print("Buyurtma qabul qilindi!")
# else:
#     print("Afsuski bizda bu taom yo\'q!")



taomlar = ['osh', 'qazonkabob', 'shashlik', 'norin', 'manti']
buyurtmalar = ['osh', 'somsa', 'manti', 'shashlik']

# for buyurtma in buyurtmalar:
#     if buyurtma in taomlar:
#         print(f"Menuda {buyurtma} bor")
#     else:
#         print(f"Kechirasiz, menuda {buyurtma} yo'q")


# x = int(input("Juft son kiriting: "))

# if x % 2 == 0:
#     print("Raxmat!")
# else:
#     print("Bu juft son emas!")


# yosh = int(input("Yoshingiz nechida?\n>>>"))

# if yosh < 4 or yosh > 60:
#     narx = 0
# elif yosh < 18:
#     narx = 10000
# else:
#     narx = 20000
# print(f"Sizga kirish narxi: {narx} so\'m")


# x, y = float(input("1-sonni kiriting: ")), float(input("2-sonni kiriting: "))
# print(f"{x} > {y}") if x > y else print(f"{x} < {y}") if x < y else print(f"{x} = {y}")


# mahsulotlar = ['un', 'yog\'', 'sovun', 'tuxum', 'piyoz',
#                'kartoshka', 'olma', 'banan', 'uzum', 'qovun']

# savat = []
# for x in range(5):
#     savat.append(input(f"{x+1}-mahsulotni qoshing: "))
# mavjud = []
# mavjud_emas = []

# for mahsulot in savat:
#     mavjud.append(mahsulot) if mahsulot in mahsulotlar else mavjud_emas.append(mahsulot)

# print(f"Bizda bu mahsulotlar mavjud emas: {mavjud_emas}")
# print(f"Bizda bu mahsulotlar bor: {mavjud}")

# users = ['umar', 'abdulloh', 'alisher', 'ulugbek', 'bekpolat']

# login = input("Yangi login tanlang: ")

# for user in users:
# 	if login in user:
# 		xabar = ("Login band, login tanlang!")
# 		break
# 	else:
# 		xabar = (f"Xush kelibsiz, {login}")

# print(xabar)

