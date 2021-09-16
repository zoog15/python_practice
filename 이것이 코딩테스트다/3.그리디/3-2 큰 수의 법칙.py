# n: 배열의 크기, m : 숫자가 더해지는 횟수, k : 특정 인덱스가 더해질수 있는 최대 횟수

n, m, k = map(int, input().split())
num_list = list(map(int, input().split()))

ans_sum = 0   # 정답을 넣을 변수
count = 0

num_list.sort()  # 일단 오름차순 정렬

for i in range(m):
    if count != k:
        ans_sum += num_list[n-1]
        count += 1
    else:
        ans_sum += num_list[n-2]
        count = 0

print(ans_sum)
