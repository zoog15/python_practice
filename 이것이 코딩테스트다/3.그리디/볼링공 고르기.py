N, M = map(int, input().split())  # N : 공의 갯수, M : 공의 최대 무게
a = list(map(int, input().split()))
count = 0  # 경우의 수 세기

for i in range(N):
    for j in range(i, N):
        if a[i] != a[j]:  # 서로 무게가 같지 않을때는 다 고를 수 있음
            count += 1

print(count)