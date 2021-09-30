array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i  # 가장 작은 원소의 인덱스
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:  # 정렬되지 않은 부분에서 최소값 찾아내기
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]  # swap
    print(array)

print(array)