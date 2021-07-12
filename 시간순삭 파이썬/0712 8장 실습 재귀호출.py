def fact(n) :
    if n == 1:
        return 1
    else :
        return n * fact(n-1)

n = int(input("n의 값은? : "))

result = fact(n)

print(result)

