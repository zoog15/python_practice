n, m = map(int, input().split())

arr = []

for i in range(n):
    arr.append(list(map(int, input().split())))

answer = []

for i in range(n):
    answer.append(min(arr[i]))

print(max(answer))