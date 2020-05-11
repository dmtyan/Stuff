
n = int(input())

degrees_of_two = []
q = 1
while q <= 10e9:
    degrees_of_two.append(q)
    q *= 2

if n in degrees_of_two:
    res = []
    while n > 1:
        res.append(str(int(n//2)))
        n/=2
    print(len(res))
    print(' '.join(res))

else:
    closest_degree = max(filter(lambda x: x <=n, degrees_of_two))
    delta = n-closest_degree
    res = [str(delta)]
    n = closest_degree

    while n > 1:
        res.append(str(int(n//2)))
        n/=2
    print(len(res))
    print(' '.join(res))