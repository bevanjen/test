r = 3
c = 3
num = []  

for i in range(r):         
    a =[]
    for j in range(c):     
        a.append(int(input("請輸入數字： ")))
    num.append(a)

a = int(num[0][2])
b = int(num[1][1])
c = int(num[2][0])
d = a + b + c
d = int(d)
print(a, '+', b, '+', c, '=', d)