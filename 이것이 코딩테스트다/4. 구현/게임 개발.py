# 방향 : 0 - 북, 1 - 동, 2 - 남, 3 - 서
n, m = map(int, input().split())
x, y, p_dir = map(int, input().split())  # 시작 x,y 와 플레이어의 방향
game_map = [[] for _ in range(n)]  # 게임 맵 생성
isVisited = [[False] * m for _ in range(n)]
move = 1  # 방문한 칸, 처음 시작한 칸도 방문한것이니 1부터 시작

for i in range(n):  # 게임 지도 입력
    game_map[i] = list(map(int, input().split()))

for i in range(n):
    for j in range(m):
        if game_map[i][j] == 1:
            isVisited[i][j] = True

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

isVisited[x][y] = True  # 첫 시작좌표는 방문
turn_time = 0

while True:
    p_dir -= 1  # 왼쪽방향 확인
    if p_dir == -1: p_dir = 3

    nx = x + dx[p_dir]
    ny = y + dy[p_dir]
    print("바라보는 곳의 좌표 ",nx,ny)

    if game_map[nx][ny] == 0 and isVisited[nx][ny] == False:
        x = nx
        y = ny
        move += 1
        isVisited[x][y] = True
        turn_time = 0
        print("도착한 곳의 좌표는 ",x,y)
        continue
    else:
        turn_time += 1
    if turn_time == 4:  # 네 방향이 모두 이미 가본 칸이거나 바다일때
        nx = x - dx[p_dir]
        ny = y - dy[p_dir]
        if game_map[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0  # 뒤로 한칸 움직인다음에 다시 4방향을 살피면서 또 뒤로갈지 멈출지를 봐야하기 때문에 turn_time을 0으로 만들어줘야함

print(*isVisited, sep="\n")
print(*game_map, sep="\n")
print(move)
