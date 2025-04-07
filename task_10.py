number = int(input())
summ = 0
for r in range(1, number):
    for i in range(1, r):
        if r % i == 0:
            summ += i
    if r == summ:
        print(r)
    summ = 0
