number = int(input())
summ = 0
a = 0
for r in range(1, number):
    for i in range(1, r):
        if r % i == 0:
            summ += i
    if r == summ:
        a+=1
    summ = 0
print(a)
