my_dict = {1: 1}
max_position = 2 ** 31
j = 1
k = 1
l = 1

while l < max_position:
    my_dict[k + j] = 1
    k += j
    j += 1
    l += j

rez = ''
for _ in range(int(input())):
    if int(input()) in my_dict.keys():
        rez = rez + '1 '
    else:
        rez = rez + '0 '

print(rez.rstrip())