# 세 정수를 입력받아 중앙값 구하기 2

def med3(a, b, c):
    if b >= a >= c or b <= a <= c:
        return a
    elif a > b > c or a < b < c:
        return b
    else:
        return c


print("세 정수의 중앙값을 구합니다.")
a = int(input("정수 a의 값을 입력하세요.: "))
b = int(input("정수 b의 값을 입력하세요.: "))
c = int(input("정수 c의 값을 입력하세요.: "))

print(f"중앙값은 {med3(a,b,c)}입니다.")