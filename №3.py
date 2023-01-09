list = input().split()
maxx = 0
minn = 1
for el in list: 
    if float(el) % 1 != 0:
        if float(el) % 1 < minn:
            minn = float(el) % 1
        if float(el) % 1 > maxx:
            maxx = float(el) % 1    
print(round(maxx - minn, 2))            