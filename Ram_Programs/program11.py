
c=0
b=0

a = int(input("Enter a number... "))

while a != 0:
    b=a%10
    c=c*10+b
    a=a//10
print (c)
