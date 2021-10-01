def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        # 값을 찾았으면
        if array[mid] == target:
            return 1
        # 찾으려는 값이 중간값보다 크면
        elif array[mid] < target:
            start = mid + 1
        # 찾으려는 값이 중간값보다 작으면
        else:
            end = mid - 1
    # 다 찾아봤는데 없을 경우
    return None


N = int(input())  # 부품의 개수
have = list(map(int, input().split()))

M = int(input())  # 확인 받으려는 부품의 개수
want = list(map(int, input().split()))

have.sort()  # 이진 탐색을 위해 미리 정렬

for i in want:
    result = binary_search(have, i, 0, N-1)
    if result != None:
        print('yes', end=' ')
    else:
        print('no',end=' ')