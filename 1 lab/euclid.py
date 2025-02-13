def euclid(a, b):
    x = max(a, b)
    y = min(a, b)
    g = 1

    while (y*g) <= x:
        g+=1
    g-=1

    if (x - y * g) == 0:
        return y
    else:
        q = x - y * g
        return euclid(q, y)

t = 27
y = 36
res = euclid(t, y)
print(f"Полученный алгоритмом Евклида НОД: {res}")