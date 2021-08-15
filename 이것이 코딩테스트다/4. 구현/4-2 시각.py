h = int(input())

cnt = 0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            # 전부 문자열로 바꿔서 더한뒤 그 안에 3이 있는지 확인
            if '3' in str(i)+str(j)+str(k):
                cnt += 1

print(cnt)
