# Fibonacci

def fib():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b
for index,x in enumerate(fib()):
    if index == 10:
        break
    print(" %s " % x)
