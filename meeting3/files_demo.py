# r = open("data/alice_in_wonderland.txt", "r")
# print(r)
# content = r.read()
# print(type(content))
# print(content)
# r.close()

with open("data/alice_in_wonderland.txt", "r") as f:
    content = f.read()
    print(len(content))

print("done")
