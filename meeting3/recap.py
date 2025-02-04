def foo(num1, num2, *args, action='mul'):
    print('args', args)
    print('inside foo')
    if action == 'mul':
        return num1 * num2
    else:
        return num1 + num2

num = foo(5, 6, 't', 5, action='sum')
print(num)

# num = foo()

# result = print("hello")


d = {
    "name": "Valeria",
    "year": 1987,
    1: "ttt"
}

print(d["name"])
print(d.get("name"))

grades = {
    "Valeria": [90, 98, 97],
    "Sagi": [100, 100, 99]
}

name = input("insert name: ")
# if name in grades:
#     print(max(grades[name]))
# else:
#     print("")

print(len(grades.get(name, [])))