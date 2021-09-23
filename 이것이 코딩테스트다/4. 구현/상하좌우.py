# import sys
#
# n = int(sys.stdin.readline())  # N x N 크기
# arr = [[0]*n for _ in range(n)]  # 지도 생성
#
# # 시작 지점의 좌표
# x = 0
# y = 0
#
# order = list(sys.stdin.readline().split())  # 움직임 명령
#
# for i in order:
#     if i == 'L' and x-1 >= 0:
#         x -= 1
#     if i == 'R' and x+1 < n:
#         x += 1
#     if i == 'U' and y-1 >= 0:
#         y -= 1
#     if i == 'D' and y+1 < n:
#         y += 1
#
# print(y+1, x+1)

# N을 입력받기
n = int(input())
x, y = 1, 1  # 시작 좌표
plans = input().split()  # 이동 계획

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어나는 경우는 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    # 이동 수행
    x, y = nx, ny

print(x,y)