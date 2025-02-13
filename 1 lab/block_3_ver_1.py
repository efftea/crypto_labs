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

def p(num):
    if num <= 1:
        return False
    for i in range(2, int(num/2) + 1):
        if num % i == 0:
            return False
    return True

def find_divs(n):
    div = []
    for i in range(2, n + 1):
        if n % i == 0 and p(i):
            div.append(i)
        if len(div) == 2:
            break
    return div

def euler(n, div_m):
    div = find_divs(n)
    result = n * (1 - 1/div[0]) * (1 - 1/div[1])
    return result

def per(n):
    div_m = find_divs(f)
    for i in range(2, n - 1):
        x = pow(i, div_m[0]) % (n+1)
        y = pow(i, div_m[1]) % (n+1)
        if x != 1 and y != 1:
            return i

n = 23
res = []

f = len(enum(n))

q = enum(f)
print(f"Число первообразных кореней: {len(q)}")

first = per(f)
print(f"Первый первообразный корень: {first}")

for st in q:
    res.append(pow(first, st) % (n))
res.sort()

print(f"Все первообразные корни по заданному простому модулю: {res}")