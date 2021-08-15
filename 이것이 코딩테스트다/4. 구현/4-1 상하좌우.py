n = int(input())
a = list(map(str, input().split()))

# 상하 좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

x, y = 1, 1

for i in range(0, len(a)):
    if a[i] == 'U' and 0 < x+dx[0] <= n:
        x += dx[0]
        y += dx[0]
    if a[i] == 'D' and 0 < x+dx[1] <= n:
        x += dx[1]
        y += dy[1]
    if a[i] == 'L' and 0 < y+dy[2] <= n:
        x += dx[2]
        y += dy[2]
    if a[i] == 'R' and 0 < y+dy[3] <= n:
        x += dx[3]
        y += dy[3]

print(x,y)
