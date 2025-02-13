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

def euler(n, one, two):
    result = n * (1 - 1/one) * (1 - 1/two)
    return result

n = 24
divs = find_divs(n)
res = int(euler(n, divs[0], divs[1]))
print(f"Два простых делителя числа {n}: {divs}")
print(f"Итоговое значение по Формуле Эйлера {res}")