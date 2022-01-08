field = []
for y in range(22):
    sub = []
    for x in range(12):
        if x==0 or x==11 or y==21 :
            sub.append(8)
        else :
            sub.append(7)
    field.append(sub)

print(field)