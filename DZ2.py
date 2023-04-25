# Считываем данные из файла
with open('input.txt', 'r') as f:
    N = int(f.readline())
    a = list(map(int, f.readline().split()))

# Вычисляем суммы урожайностей ягод на двух соседних кустах
sums = [a[i-1] + a[i] + a[(i+1) % N] for i in range(N)]

# Находим максимальную сумму
max_sum = max(sums)

# Записываем результат в файл
with open('output.txt', 'w') as f:
    f.write(str(max_sum))
