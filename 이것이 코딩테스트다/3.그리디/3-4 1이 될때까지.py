n, k = map(int, input().split())  # n : 숫자, k : 나눌 숫자
count = 0

while n != 1:
    if n % k == 0:
        n //= k
        count += 1
    else:
        n -= 1
        count += 1

print(count)