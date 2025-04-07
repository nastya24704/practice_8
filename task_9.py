N = int(input())
a = [i for i in range(N + 1)]
a[1]=0
i = 2
while i <= N:
    if a[i] != 0:
        j = i + i
        while j <= N:
            a[j] = 0
            j = j + i
    i += 1
a = [i for i in a if i != 0]
print(a)
