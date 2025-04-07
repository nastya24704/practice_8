number = int(input())
summ = 0
for i in range(1, number):
    if number % i == 0:
        summ +=i
if number == summ:
    print('совершенное')
else:
    print('несовершенное')
