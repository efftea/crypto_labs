def enum(n):
    div = []
    for i in range(1, n):
        count = 0
        for j in range(1, i+1):
            if i % j == 0 and n % j == 0:
                count += 1
        if count == 1:
            div.append(i)
    return div

n = 11
f = enum(n)
print(f"Найдём все взаимнопростые для нашего числа: {f}")
print(f"Найдём колличество первообразных кореней: {len(enum(len(f)))}")
res = []
for num in f:
    count = 0
    for i in range(1, n):
        x = pow(num,i) % n
        if x == 1:
            count += 1

    if count == 1:
        res.append(num)

print(f"Все первообразные корни по заданному простому модулю: {res}")