#-------Generator--------------
def show(n):
    for i in range(1,n+1):
        yield i*i

a = show(3)
print(next(a))
print(next(a))

print("----------------------------------")
#------Iterator--------------------------
l1 = [1,2,3,4]
b= iter(l1)
print(next(b))
print(next(b))
