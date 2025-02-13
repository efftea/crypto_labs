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

n = 10
result = enum(n)
print(f"Числа меньше {n} с 1 общим делителем: {result}")