n = 1000
number = [False,False] + [True] * (n-1)

primes = []

for i in range(2,n+1) :
    if number[i] :
        primes.append(i)
        for j in range(2*i,n+1,i) :
            number[j] = False

print(primes)
