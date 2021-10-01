# N(가게의 부품 개수)을 입력받기
n = int(input())
array = [0] * 1000001

# 가게에 있는 전체 부품 번호를 입력받아 저장
for i in input().split():
    array[int(i)] = 1

# M 입력받기
m = int(input())
# 손님이 확인 요정한 전체 부품 번호를 공백으로 구분하여 입력
want = list(map(int, input().split()))

# 손님이 확인 요청한 부품 확인하기
for i in want:
    if array[i] == 1:
        print("yes", end=' ')
    else:
        print("no", end=' ')