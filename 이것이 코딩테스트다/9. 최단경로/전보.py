import heapq

INF = int(1e9)

# n: 도시수, m: 통로수, c: 시작지점(start)
n, m, c = map(int, input().split())

# 현 도시들의 연결상황 표현 그래프
graph = [[] for i in range(n+1)]
# 각 도시간 최단거리 테이블
distance = [INF] * (n+1)

# 각 도시 연결상황 입력
for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(c)

# 몇개의 도시가 전보를 받는지
city_count = 0

for i in range(n+1):
    if i == c or distance[i] == INF:
        distance[i] = -1
    else:
        city_count += 1

print(city_count, max(distance))


