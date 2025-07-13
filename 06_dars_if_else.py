avtolar = ['audi', 'bmw', 'volvo', 'kia', 'hyundai']

# for avto in avtolar:
#     if avto == 'bmw':
#         print(avto.upper())
#     else:
#         print(avto.title())

# ism = 'muxriddin'

# ism = input("ismingiz nima? >>>")
# if ism.lower() != 'muxriddin':
#     print(f"Uzur {ism.title()}, biz Muxriddinni kutyapmiz!")
# else:
#     print("Assalomu aleykum Muxriddin xush kelibsiz!")


# javob = int(input("9 x 8 = "))

# if javob != 72:
#     print("Xato javob qaytadan urunib koring!")
# else:
#     print("Barakalla!")


# yosh = int(input("Yoshingizni kiriting: "))

# if yosh >= 18:
#     print("Xush kelibsiz!")
# else:
#     print("Sizga kirish mumkin emas!")

# login = input("Yangi login kiriting: (login 5 ta belgidan oshmasin!) >>>")
# if len(login) <= 5:
#     print("login 5 ta belgidan kop bolishi kerak")

# yil = int(input("Tugilgan yilingizni kiriting: "))

# if 2025 - yil <= 18:
#     print(f"Siz {2025-yil}-yoshda ekansiz")
#     print("Sizga kirish mumkin emas!")
# else:
#     print("Xush kelibsiz!")


# x, y = 1, 2
# print("X > Y") if x > y else print("X < Y")


cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']

# for car in cars:
#     print(car.upper()) if car == 'gm' else print(car.title())


# ism = input("Ismingizni kiriting: ")

# print("Xush kelibsiz, Admin. Foydalanuvchilar royhatini korasizmi?") if ism == 'admin' else print("Xush kelibsiz", ism.title())


# x, y = int(input("1-sonni kiriting: ")), int(input("2-sonni kiriting: "))
# if x == y: print("Sonlar teng ekan!") 

# x = float(input("Istalgan son kiriting: "))

# print("Son manfiy") if x < 0 else print("Son musbat")
# print(x**(1/2)) if x > 0 else print("Musbat son kiriting!")


# for i in list(range(1, 10)):
#     print(f"{i} ning kv {i**2} ga teng!")

# sonlar = [5, -3, 7, 0, -1, 9]

# for son in sonlar:
#     if son >= 0: print(son)


# x, y = int(input("1-son: ")), int(input("2-son: "))

# print(f"{x} > {y}") if x > y else print(f"{x} < {y}") if x < y else print(f"{x} = {y}")


# 1-mashq
# sonlar = []
# toq_sonlar = []
# juft_sonlar = []

# print("10 ta ixtiyoriy sonlarni kiriting!")
# for i in range(10):
#     sonlar.append(int(input(f"{i+1}-sonni kiriting: ")))

# for son in sonlar:
#     toq_sonlar.append(son) if son % 2 else juft_sonlar.append(son)
# print(f"Juft sonlar: {juft_sonlar}\n",f"Toq sonlar: {toq_sonlar}")


# 2-mashq
# sonlar = [-5, 3, -2, 0, 7, 1, -8]

# for son in sonlar:
#     if son > 0:
#         print(son**2)


# 3-mashq
# ismlar = []

# print("5-ta ism kiriting!")
# for x in range(5):
#     ismlar.append(input(f"{x+1}-ismni kiriting: "))

# for ism in ismlar:
#     print(f"A harf bilan boshlanadigan ismlar: {ism.title()}") if ism.lower().startswith('a') else None
        

# 4-mashq    elif ball < 88:
        # print("88 ball --> B baho")
# for i in range(1, 51):
#     print(f"{i} soni 15 ga qoldiqsiz bolinadi") if i % 15 == 0 else \
#     print(f"{i} soni 5 ga qoldiqsiz bolinadi") if i % 5 == 0 else \
#     print(f"{i} soni 3 ga qoldiqsiz bolinadi") if i % 3 == 0 else None


# 5-mashq   
# ballar = [95, 67, 88, 45, 76, 59]

# for bal in ballar:
#     if bal >= 95:
#         baho = 'A'
#     elif bal >= 88:
#         baho = 'B'
#     elif bal >= 70:
#         baho = 'C'
#     elif bal >= 60:
#         baho = 'D'
#     else:
#         baho = 'F'
#     print(f"{bal} bali - {baho} baho")




