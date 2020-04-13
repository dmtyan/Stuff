
my_str = input()


def get_longest_palindrome(string):
    n = len(string)
    cache = [[None] * n for _ in range(n)]

    def is_palindrome(lo, hi):
        if cache[lo][hi] is not None:
            return cache[lo][hi]

        if lo == hi:
            return True
        elif lo + 1 == hi:
            return string[lo] == string[hi]

        ans = False if string[lo] != string[hi] else is_palindrome(lo + 1, hi - 1)
        cache[lo][hi] = ans
        return ans

    def generate_palindromes():
        res = []
        if not string:
            return ['']

        for l in range(n, 0, -1):
            found = False
            for s in range(n-l+1):
                if is_palindrome(s, s+l-1):
                    found = True
                    res.append(string[s:s + l])
            if found:
                break
        return res

    lst = generate_palindromes()
    return lst[0]


print(get_longest_palindrome(my_str))



