# for elements
# range
# zip

# l = [1,2,3,44,55,6,7]
# for elem in l:
#     print(elem)

# for num in l[2::2]:
#     print(num)
#
# for char in "valeria":
#     print(char)

# l = list()
# num = int()

# r = range(10)
# for i in r:
#     print(i)
# l[2:10:2]
# max_num = int(input("insert max "))
# r = range(max_num, -1, -10)
# for i in r:
#     print(i)

# l = [1,2,3]
# r = range(1, 4)

# r = range(1, 1_000_000_000, 87)
# print(28745 in r)

# l = [90, 87, 67,44,55,60,77]
# for elem in enumerate(l):
#     print(elem)
#     print(f"index: {elem[0]}, grade: {elem[1]}")

# l = [1,2,3]
# t = (1,2,3)
#
# print(t[2])
# l[1] = 9
# t[1] = 9

# l = "05:34".split(":")
# h = l[0]
# m = l[1]

# h, m = ["05", "34"]
# h, m = "05:34".split(":")
# h, m = "05:34:38".split(":")

# print(h, m)

# l = ("a", "tt", 90, 87, 67,44,55,60,77)
# for i, num in enumerate(l):
#     print(f"index: {i}, num: {num}")
# for elem in l:
#     print(f"elem: {elem}")

# matrix = [
#     [1,2,3],
#     [11,22,33],
#     [111,222,333],
# ]

# for row in matrix:
#     print(row)
#
# for c1, c2, c3 in matrix:
#     print(c2)


# l = [1,2,3]
# l[0] = 4
# num = l[1]
# num = 6

# i, num = (0, 67)

cities = ["Jerusalem", "New York", "Paris"]
countries = ["Israel", "US", "France"]
temperature = [14, -3]
for city, country, temper in zip(cities, countries, temperature):
    print(city, country, temper)