array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1):  # 인덱스 i부터 1까지 감소하며 반복
        if array[j] < array[j-1]:  # 왼쪽으로 한 칸씩 이동
            array[j], array[j-1] = array[j-1], array[j]  # 왼쪽에 있는게 더 큰값이면 스왑 진행
        else:  # 왼쪽에 있는게 더 작은 값이면 스왑 중단
            break
    print(array)

print(array)