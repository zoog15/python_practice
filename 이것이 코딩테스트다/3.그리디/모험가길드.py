n = int(input())  # 모험가의 수
a = list(map(int, input().split()))  # 공포도

a.sort()  # 정렬
count = 0

while len(a) != 0:
    max_x = a[-1]  # 최대 공포도를 가진 사람
    if len(a) >= max_x:  # 남은사람의 수가 최대 공포도를 가진 사람의 수보다 많을때만
        for i in range(max_x):  # 그 수만큼 그룹결성!
            a.pop()
    else:  # 남은사람 수가 공포도보다 작으면 그룹결성 불가능
        break
    count += 1

print(count)