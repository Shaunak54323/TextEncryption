z = 110
m = 9
for i in range(1000000):
    if z * i % 9 == 1:
        print(i)
        break