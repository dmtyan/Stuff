
n = int(input())
if n == 0:
    print(10)
elif n == 1:
    print(1)
else:
    factorization = {}
    i = 9
    while i > 1 and n > 1:
        if n % i == 0:
            if i not in factorization.keys():
                factorization[i] = 1
            else:
                factorization[i] += 1
            n /= i
        else:
            i -= 1
    if n > 1:
        print(-1)
    else:

        res = []
        for key in factorization:
            for _ in range(factorization[key]):
                res.append(str(key))
        res.sort()
        print(''.join(res))

