cars = ['bmw', 'mersdes benz', 'volvo', 'general motors', 'tesla', 'audi']
# print(len(cars))

sonlar = list(range(1, 10))
# print(max(sonlar))


countrys = ['ozbekiston', 'rossiya', 'turkiya', 'afgoniston', 'xitoy', 'falastin', 'iroq', 'amerika']

# print(len(countrys))
# print(sorted(countrys))
# print(sorted(countrys, reverse=True))
# countrys.sort()
# print(countrys)
# countrys.sort(reverse=True)
# print(countrys)

sonlar = list(range(120, 1200, 2))

# print(sum(sonlar))
# x = min(sonlar)
# y = max(sonlar)
# z = y - x
# print(z)
# print(len(sonlar))
# print(sonlar[:20])
# print(sonlar[-20:])
# print(sonlar[530:550])

taomlar = ['somsa', 'osh', 'norin', 'honim', 'chuchvara']
nonushta = taomlar[:]
nonushta.remove('somsa')
nonushta.remove('osh')
nonushta.remove('honim')
nonushta.append("non va qaymoq")
nonushta.append("issiq non")

# print(nonushta)

nonushta = tuple(nonushta)
nonushta[0] = "qaymoq va non"

# print(nonushta)
# print(taomlar)