def get_Levenshtein_distance(string_1, string_2):
    matrix = [[float('inf') for _ in range(len(string_2)+1)] for __ in range(len(string_1)+1)]
    for i in range(len(string_1)+1):
        matrix[i][0] = i
    for j in range(len(string_2)+1):
        matrix[0][j] = j

    for i in range(1, len(string_1)+1):
        for j in range(1, len(string_2)+1):
            c = 0
            if string_1[i-1] != string_2[j-1]:
                c = 1
            matrix[i][j] = min(matrix[i-1][j] + 1, matrix[i][j-1] + 1, matrix[i-1][j-1] + c)

    return matrix, matrix[-1][-1]


string_1 = input()
string_2 = input()

print(get_Levenshtein_distance(string_1, string_2)[1])

