books = []
topildi = False
books.append({
    "nomi": "Ufq",
    "muallif": "Abdulla Qodiriy",
    "narx": 35000
})

books.append({
    "nomi": "Alkimyogar",
    "muallif": "Paulo Coelho",
    "narx": 45000
})

books.append({
    "nomi": "Mehrobdan chayon",
    "muallif": "Tog'ay Murod",
    "narx": 30000
})


buydjet = int(input("Buydjetingizni kiriting: "))

print("Sizga mos kitoblar:")

for book in books:
    if book['narx'] <= buydjet:
        print(f" - Kitob nomi: {book['nomi']} \nMuallif: {book['muallif']} \nNarxi: {book['narx']} so'm\n\n")
        topildi = True
if not topildi:
    print("Sizga mos buydjetni kitob topa olmadik!")

    
