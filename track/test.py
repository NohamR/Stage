f = open("track/points.txt")
l = f.readlines().replace('\n', '')
a = []
b = []
for i in (0, len(l)-1):
    if i/2 == 0:
        b+=[l[i]]
    else:
        a+=[l[i]]

print(l)