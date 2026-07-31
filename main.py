lister = ["b","a","d","g","e","g","f","h","l"]
id = []

for i in range(len(lister)):
    id.append(ord(lister[i]))


id.sort()
for i in range(len(id)):
    lister[i] = chr(id[i])

print(lister)


