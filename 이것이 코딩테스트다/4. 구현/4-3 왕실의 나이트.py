s = input()

# 시작 지점의 x,y 좌표 입력
x = ord(s[0])-96  # a일때 1부터 시작
y = int(s[1])

cnt = 0
dx = [-2, -2, -1, 1, 2, 2, -1, 1]
dy = [-1, 1, -2, -2, -1, 1, 2, 2]

for i in range(8):
    if 1 <= x+dx[i] <= 8 and 1 <= y+dy[i] <= 8:
        cnt += 1

print(cnt)