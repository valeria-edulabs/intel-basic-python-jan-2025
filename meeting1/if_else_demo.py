# # questionnaire
# # in
# # constant list
# # empty list
# # creating and populating list
# # if - elif - else
#
# print("u" in "sun")
# print("U" in "sun")
#
# # l1 = list([1,2,3,5,6])
# l1 = [1, 2, 3, 56,2, 90, "Yulia", "Sagi", 4.5]
#
# print(100 in l1)
#
# l = []
# print(len(l))
# l.append(4)
# print(l)
# print(l1.count(2))
# print(l1.extend(l))
# print(l1)
# print(l1 + l)
#
#
# name = input("Insert your name: ")
# is_lower = input("Insert lower or upper:")
# name_to_be_printed = ""
# if is_lower == "l":
#     print("will be lower case")
#     name_to_be_printed = name.lower()
# elif is_lower == "u":
#     print("will be upper case")
#     name_to_be_printed = name.upper()
# else:
#     print("i don't know - printing capitalized")
#     name_to_be_printed = name.capitalize()
# print(f"Your name: {name_to_be_printed}")


# name = input("Insert your name: ")
# is_lower = input("Insert lower or upper:")
# name_to_be_printed = ""
# if is_lower == "l":
#     print("will be lower case")
#     name_to_be_printed = name.lower()
#     # exit()
# if is_lower == "u":
#     print("will be upper case")
#     name_to_be_printed = name.upper()
# # if is_lower != "l" and is_lower != "u":
# if is_lower not in "lu":
#     print("i don't know - printing capitalized")
#     name_to_be_printed = name.capitalize()
# print(f"Your name: {name_to_be_printed}")

name = input("Insert your name: ")
is_lower = input("Insert lower or upper:")
name_to_be_printed = ""
if is_lower == "l":
    print("will be lower case")
    name_to_be_printed = name.lower()
    # exit()
if is_lower == "u":
    print("will be upper case")
    is_star = input("Do you want start?")
    if is_star == "y":
        name_to_be_printed = f"***{name.upper()}***"
    else:
        name_to_be_printed = name.upper()
# if is_lower != "l" or is_lower != "u":
if is_lower not in "lu":
    print("i don't know - printing capitalized")
    name_to_be_printed = name.capitalize()
print(f"Your name: {name_to_be_printed}")