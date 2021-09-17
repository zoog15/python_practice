s = list(input())  # 숫자로만 이루어진 문자열 바로 리스트화

answer = 0
#  0이랑 1일때는 더하는게 수가커짐
for i in s:
    if int(i) == 0:  # 0일때는 계산할 필요 없음
        continue
    else:
        if answer == 0:  # 아직 answer가 0일때
            if int(i) == 1:  # 1은 1 더해주기
                answer += 1
            else:  # 곱하기는 1부터 시작해야하니 1로 만들어주고 곱하기
                answer = 1
                answer *= int(i)
        else:
            if int(i) == 1:
                answer += 1
            else:
                answer *= int(i)

print(answer)