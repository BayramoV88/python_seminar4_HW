# Вычислить число π c заданной точностью d

d = int(input('Введите число: '))
pi = sum(1/16**i*(4/(8*i + 1) - 2/(8*i + 4) - 1/(8*i + 5) - 1/(8*i + 6)) for i in range(d))
print(pi)