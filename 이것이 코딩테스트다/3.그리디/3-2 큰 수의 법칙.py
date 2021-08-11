import sys

n, m, k = map(int, sys.stdin.readline().split())

num = list(map(int, sys.stdin.readline().split()))

num.sort()

max1 = num[n-1]
max2 = num[n-2]

# 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k+1)) * k
count += m % (k+1)

result = 0
result += (count) * max1  # 가장 큰 수 더하기
result += (m-count) * max2  # 두번째로 큰 수 더하기

print(result)