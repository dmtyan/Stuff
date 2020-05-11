from math import factorial
from decimal import Decimal
n = int(input())


if n == 1:
    print(0)
elif n == 2:
    print(2)
else:
    count = Decimal('0')
    for i in range(2, n+1):
        count += Decimal(factorial(n))/Decimal(factorial(n-i))

    print(int(count))