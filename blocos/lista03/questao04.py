gplays = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
length = len(gplays)

for n in range(length):
    temp = int(input())
    gplays.insert(n, temp)
media = sum(gplays)/length
print(media)

for n in gplays:
    if n > media:
        print(n)
