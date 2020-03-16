def z_func(s):
    s += '$'
    l, r = 0, 0
    z = [0] * len(s)
    for i in range(1, len(s)):
        z[i] = max(0, min(z[i - l], r - i))
        while s[z[i]] == s[i + z[i]]:
          z[i] += 1
        if i + z[i] > r:
          l, r = i, i + z[i]
    return z[:-1]


def substringsearch(string, pattern):
    zf = z_func(pattern + '#' + string)
    for i in range(len(pattern)+1, len(string)+2):
        if zf[i] == len(pattern):
            print(i-len(pattern)-1, end=' ')


pattern = input()
string = input()

substringsearch(string, pattern)