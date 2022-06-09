num = int(input('n: '))
factors = []

for i in range(2, num):
    while num % i == 0:
        factors.append(i)
        num //= i

print(*factors, sep=' x ')
