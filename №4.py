number = int(input())
newnumber = ''
while(number > 0):
    newnumber= str(number % 2) + newnumber
    number = number // 2
print(newnumber)    