num = 12
prime = []

for i in range(1,num):
    for j in range(2, i): 
        if i % j == 0:
            prime.append(j)
print(prime)
