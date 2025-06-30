
def show(N) -> int:
    N=bin(N)[2:]
    print(N)
    b=0
    maxb=0
    for n in N:
        if int(n)==0:
            b=b+1
        elif int(n)==1:
            maxb=max(b,maxb)
            b=0
    return maxb
print(show(150))