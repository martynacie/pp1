ar = [1, 2, 3, 4, 5]

ar[0]-=1
print(ar)

ar[-1]+=4
print(ar)

ar[len(ar)//2]*=2
print(ar)

for i in range(len(ar)):
    ar[i]+=3
print(ar)
 