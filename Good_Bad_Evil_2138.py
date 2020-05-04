def translate(type_computer, number):
    if type_computer == 'GOOD':
        sequence = []
        for i in range(3, -1, -1):
            if number < 256**i:
                sequence.append(0)
            else:
                multiplier = number//(256**i)
                sequence.append(multiplier)
                number -= (256**i)*multiplier
        res = 0
        for i in range(len(sequence)):
            res += sequence[i] * (256 ** i)
        return res

    elif type_computer == 'BAD':
        sequence = []
        for i in range(3, -1, -1):
            if number < 256 ** i:
                sequence.append(0)
            else:
                multiplier = number // (256 ** i)
                sequence.append(multiplier)
                number -= (256 ** i) * multiplier
        res = 0
        for i in range(len(sequence)):
            res += sequence[i] * (256 ** i)
        return res


print(translate(input(), int(input())))