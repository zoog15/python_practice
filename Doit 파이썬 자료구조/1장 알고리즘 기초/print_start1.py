# *를 n개 출력하되 w개마다 줄바꿈하기 1

print("*를 출력합니다.")
n = int(input("몇 개를 출력할까요?: "))
w = int(input("몇 개마다 줄바꿈 할까요?: "))

for i in range(n):
    print("*", end='')
    if i % w == w - 1:  # n번 판단
        print()

if n % w:  # 1번 판단
    print()  # 나머지가 있으면 출력 한번 더해줌