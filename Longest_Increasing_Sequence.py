def longest_increasing_sequence(arr):

    pointers = [None for _ in range(len(arr))]
    increasing_subsequence = [0 for _ in range(len(arr)+1)]
    length = 0

    for i in range(len(arr)):
        low = 1
        high = length
        while low <= high:
            medium = (low+high)//2
            if arr[increasing_subsequence[medium]] < arr[i]:
                low = medium + 1
            else:
                high = medium - 1

        place = low

        pointers[i] = increasing_subsequence[place-1]
        increasing_subsequence[place] = i

        if place > length:
            length = place


    ans = [None for _ in range(length)]
    k = increasing_subsequence[length]

    for i in range(length-1, -1, -1):
        ans[i] = arr[k]
        k = pointers[k]

    return ans

n = int(input())
arr = list(map(int, input().split()))

print(longest_increasing_sequence(arr))
