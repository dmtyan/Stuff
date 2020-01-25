W, n = map(int, input().split())
weights = list(map(int, input().split()))
costs = list(map(int, input().split()))

D = [[0 for _ in range(W+1)] for __ in range(n+1)]

for i in range(W+1):
    D[0][i] = 0

for i in range(n+1):
    D[i][0] = 0

for i in range(1, n+1):
    for w in range(0, W+1):
        D[i][w] = D[i-1][w]
        if weights[i-1] <= w:
            D[i][w] = max(D[i][w], D[i-1][w-weights[i-1]]+costs[i-1])

print(D[n][W])