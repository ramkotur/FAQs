from typing import Generator

def evn_no(limit: int) -> Generator[int, None, None]:
    n = 0
    while n <= limit:
        yield n
        n += 2

l = int(input("Enter a number: "))
for m in evn_no(l):
    print(m)
