# 선형 검색 알고리즘(실습 3-1)을 보초법으로 수정

from typing import Any, Sequence
import copy


def seq_search(seq: Sequence, key: Any) -> int:
    """시퀀스 a에서 key와 값이 같은 원소를 선형 검색(보초법)"""
    a = copy.deepcopy(seq)  # seq를 복사
    a.append(key)  # 보초 key를 맨 뒤에 추가
    
    i = 0
    while True:
        if a[i] == key:
            break
        i += 1
    
    return -1 if i == len(seq) else i  # 배열의 맨 끝에 도달했으면 -1, 아니면 인덱스를 반환


if __name__ == '__main__':
    num = int(input("원소 수를 입력하세요. : "))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f"x[{i}] : "))

    ky = int(input("검색할 값을 입력하세요.: "))  # key를 입력받음
    idx = seq_search(x, ky)  # ky와 같은 값을 x에서 검색하여 그 인덱스를 반환

    if idx == -1:
        print("검색값을 갖는 원소가 존재하지 않습니다.")
    else:
        print(f"검색값은 x[{idx}]에 있습니다.")