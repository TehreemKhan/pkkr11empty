l = list()
for num in range(1, 251):
    for x in range(2, num):
        if num % x == 0:
            break
    else:
        l.append(num)

with open("prime.txt","w") as f:
    f.write(str(l))