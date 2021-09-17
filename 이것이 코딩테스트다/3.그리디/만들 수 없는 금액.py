# n = int(input())  # 동전의 개수
# a = list(map(int, input().split()))  # 동전 종류
#
# a.sort()  # 내림차순으로 정렬
#
# num = 1  # 최소금액 체크용
# temp = 0  # 숫자 조작용 임시변수
#
# while True:
#     for i in range(len(a)):
#         temp = num
#         flag = 0  # 0이 만들어질때는 더 확인할 필요 없음
#         for j in range(i, len(a)):
#             temp -= a[j]
#             if temp == 0:
#                 flag = 1
#                 break
#         if flag == 1:
#             break
#     if temp != 0:
#         break
#     num += 1
#
# print(num)

# 책 풀이
n = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1
for x in data:
    # 만들 수 없는 금액을 찾았을 때 반복 종료
    if target < x:
        break
    target += x

# 만들 수 없는 금액 출력
print(target)



