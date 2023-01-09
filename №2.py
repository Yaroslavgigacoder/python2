list1 = input().split()
list2 = []
if len(list1)%2==0:
    half = len(list1)//2
else:
    half = len(list1)//2+1     
for i in range(0,half): 
    list2.append(int(list1[i])*(int(list1[len(list1)-i-1]))) 
print(list2)    