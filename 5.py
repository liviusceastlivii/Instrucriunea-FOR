n=int(input("dati n:"))
s=0
for e in range(1,n):
    if(e%3==0) and (e%5==0):
        s+=e
print(s) 