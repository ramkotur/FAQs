
a=int(input("Enter a number..."))
d=x=0
b= str(bin(a)[2:])
print(b)
for c in b:
    if c=="0":
        d=d+1
    else:
        x= max(d,x)
        d=0
print (x)