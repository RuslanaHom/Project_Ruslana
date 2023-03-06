N = int(input('Введите количество строк '))
probel = ''
for i in range(1, N + 1):
    words = input('Введите слово ')
    probel = probel + words + ' '
print(probel)