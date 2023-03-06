count=0
Win=0
while True:
    import random
rnd_num1 = random.randint(0, 30)
rnd_num2 = random.randint(0, 30)
print(rnd_num1, '+' ,rnd_num2)
Result=int(input())
if rnd_num1 + rnd_num2 == Result:
    print('Ответ верный')
    Win+=1
else:
    print('Ответ неверный, попробуйте снова')
    count+=1
    if count == 3:
        print('Конец игры! Ваш счёт', Win)

