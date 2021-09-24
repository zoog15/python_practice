chess = [[0]*8 for _ in range(8)]  # 8x8 크기의 체스판

x = ['a','b','c','d','e','f','g','h']
y = ['1','2','3','4','5','6','7','8','9']

s = list(input())
cnt = 0

start_x = x.index(s[0])
start_y = y.index(s[1])

dx = [-1,1,2,2,1,-1,-2,-2]  # 좌우
dy = [-2,-2,-1,1,2,2,1,-1]  # 위아래

for i in range(8):
    if 0 <= start_x + dx[i] < 8 and 0 <= start_y + dy[i] < 8:
        cnt += 1

print(cnt)

