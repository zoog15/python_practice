import sys

n, k = map(int, sys.stdin.readline().split())

cnt = 0

while True:
    if n%k == 0:
        n /= k
        cnt += 1
    else:
        n -= 1
        cnt += 1

    if n == 1:
        print(cnt)
        break
