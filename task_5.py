number = input()
summ = 0
for i in range(1, len(number)+1):
    summ += int(number)%10
    number = int(number)//10
if number % summ ==0:
    print('совершенное')
else:
    print('несовершенное')
