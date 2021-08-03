# 버블 정렬 알고리즘 구현하기

from typing import MutableSequence


def bubble_sort(a: MutableSequence) -> None:
    """버블 정렬"""
    n = len(a)
    for i in range(n-1):  # 패스의 과정, 앞뒤 숫자 대소를 비교해 위치 바꾸기
        for j in range(n-1, i, -1):  # 뒤에서부터 확인
            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]


if __name__ == '__main__':
    print("버블 정렬을 수행합니다.")
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num  # 원소 수가 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    bubble_sort(x)

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')
