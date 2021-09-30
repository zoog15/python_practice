n = int(input())

arr = []
for i in range(n):
    data = input().split()  # 이름과 점수를 저장
    # 이름은 문자열 그대로, 점수는 int로 바꿔서 저장
    arr.append((data[0], int(data[1])))

# 키(key)를 이용해, 점수를 기준으로 정렬
arr = sorted(arr, key=lambda x: x[1])

# 정렬이 수행된 결과 출력
for student in arr:
    print(student[0], end=' ')