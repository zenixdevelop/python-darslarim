uzunlik = int(input("Boyingiz:(sm da kiriting)>>>"))
vazn = float(input("Vazningizni kiriting: (kg da kiriting)>>>"))

uzunlik_m = uzunlik / 100
bmi = vazn / (uzunlik_m*2)

if bmi < 18.5:
    print("Siz ozg'insiz!")
elif bmi < 25:
    print("Sizning vazninggiz normal!")
elif bmi < 30:
    print("Sizda ortiqcha vazn bor!")
else:
    print("Sizda semizlik mavjud!")