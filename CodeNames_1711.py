
n = int(input())
codenames = {}

for i in range(n):
    cnms = input().split()
    cnms.sort()
    codenames[i+1] = cnms
order = list(map(int, input().split()))

def get_list():
    res = []
    prev = ''
    for i in order:
        word = codenames[i][0]
        if word < prev:
            word = codenames[i][1]
        if word < prev:
            word = codenames[i][2]
        if word < prev:
            return False
        else:
            prev = word
            res.append(prev)
    return res

x = get_list()
if x:
    for elem in x:
        print(elem)
else:
    print('IMPOSSIBLE')