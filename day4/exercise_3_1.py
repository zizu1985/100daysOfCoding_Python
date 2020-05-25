primes = []
primes.append(2)

for i in range(2, 999):
    next = i + 1
    iter = 0
    for j in primes:
        if (next % j) == 0:
            break;
        if iter == len(primes) - 1:
            primes.append(next)
            break
        iter += 1

print(primes)