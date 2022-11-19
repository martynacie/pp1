ar = [-15, 8, -31, 47, -2, 19]
mn = ar[0]
mx= ar[0]
for i in range(len(ar)):
    if ar[i]>mx:
        mx=ar[i]
    elif ar[i]<mn:
        mn=ar[i]
    else:
        continue
print("najmniejsza wartość ", mn)
print("najwieksza wartosc ", mx)