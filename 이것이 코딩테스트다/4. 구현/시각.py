import sys

n = int(sys.stdin.readline())
cnt = 0

for i in range(n+1):  # 시
    for j in range(60):  # 분
        for k in range(60):  # 초
            if '3' in str(i) + str(j) + str(k):  # 만약 3이 시,분,초중에 들어가있다면
                cnt += 1
print(cnt)