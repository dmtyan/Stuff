def simple_calculator(num):
    D = [float('inf') for _ in range(num+1)]
    paths = {}
    D[num] = 0
    D[num-1] = 1
    paths[num-1] = 1
    for i in range(2, num):
        min_val = D[num-(i-1)]+1
        flag = 1
        if (num-i)*2 <= num:
            if D[(num-i)*2]+1 < min_val:
                min_val = D[(num-i)*2]+1
                flag = 2
        if (num-i)*3 <= num:
            if D[(num-i)*3]+1 < min_val:
                min_val = D[(num-i)*3]+1
                flag = 3
        D[num-i] = min_val
        paths[num-i] = flag

    print(D[1])
    curr = 1
    while curr < num:
        print(curr, end=' ')
        path = paths[curr]
        if path == 1:
            curr = curr+1
        elif path == 2:
            curr = curr*2
        elif path == 3:
            curr = curr*3
    print(num)


number = int(input())
simple_calculator(number)