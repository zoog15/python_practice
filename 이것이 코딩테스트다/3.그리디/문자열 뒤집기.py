s = list(input())  # 문자열 입력받기

count1 = 0
count0 = 0

# 입력받은 문자열 복사배열 2개 생성
s1 = s.copy()
s0 = s.copy()

# 전부 1로 바꿔줄때
for i in range(len(s)-1):
    if s1[i] == '0':
        s1[i] = '1'
        if s1[i+1] == '1':
            count1 += 1
if s1[-1] == '0':
    s1[-1] = '1'
    count1 += 1

# 전부 0으로 바꿔줄때
for i in range(len(s)-1):
    if s0[i] == '1':
        s0[i] = '0'
        if s0[i+1] == '0':
            count0 += 1
if s0[-1] == '1':
    s0[-1] = '0'
    count0 += 1

# 두 상황중 더 작은걸 출력
print(min(count1,count0))
