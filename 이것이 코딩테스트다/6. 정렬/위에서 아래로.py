n = int(input())  # 입력할 숫자의 개수

arr = [int(input()) for _ in range(n)]

arr.sort(reverse=True)

print(*arr, sep=' ')