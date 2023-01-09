list = input().split()
sum = 0
for i in range(1,len(list), 2): 
    sum += int(list[i]) 
print(sum)    