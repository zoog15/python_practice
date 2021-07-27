# 체인법으로 해시 함수 구현하기

from __future__ import annotations
from typing import Any, Type
import hashlib


class Node:
    """해시를 구성하는 노드"""

    def __init__(self, key: Any, value: Any, next: Node) -> None:
        """초기화"""
        self.key = key  # 키
        self.value = value  # 값
        self.next = next  # 뒤쪽 노드를 참조


class ChainedHash:
    """체인법으로 해시 클래스 구현"""

    def __init__(self, capacity: int) -> None:
        """초기화"""
        self.capacity = capacity  # 해시 테이블의 크기를 지정
        self.table = [None] * self.capacity  # 해시 테이블(리스트)를 선언

    def hash_value(self, key: Any) -> int:
        """해시값을 구함"""
        if isinstance(key, int):
            return key % self.capacity
        return(int(hashlib.sha256(str(key).encode()).hexdigest(), 16) % self.capacity)

    def search(self, key: Any) -> Any:
        """키가 key인 원소를 검색하여 값을 반환"""
        hash = self.hash_value(key)  # 검색하는 키의 해시값, hash_value(해시함수)에 넣어서 처리
        p = self.table[hash]  # 노드를 주목

        while p is not None:  # 노드가 뒤에가 비어질때까지
            if p.key == key:
                return p.value  # 검색 성공
            p = p.next  # 다음 노드 주목

        return None  # 검색 실패

    def add(self, key: Any, value: Any) -> bool:
        """키가 key이고 값이 value인 원소를 추가"""
        hash = self.hash_value(key)  # 추가하는 key의 해시값
        p = self.table[hash]  # 노드를 주목

        while p is not None:
            if p.key == key:
                return False  # 추가 실패
            p = p.next  # 뒤쪽 노드를 주목

            temp = Node(key, value, self.table[hash])  # 위의 과정을 지나면 해시 테이블에 값이 없다는걸 알 수 있기에 노드를 만들어줌
            self.table[hash] = temp  # 노드를 추가
            return True  # 추가 성공

    def remove(self, key: Any) -> bool:
        """키가 key인 원소를 삭제"""
        hash = self.hash_value(key)  # 삭제할 key의 해시값
        p = self.table[hash]  # 해시값에 해당하는 노드를 주목
        pp = None  # 바로 앞의 노드를 주목

        while p is not None:
            if p.key == key:  # key를 발견하면
                if pp is None:
                    self.table[hash] = p.next
                else:
                    pp.next = p.next
                return True  # 삭제 성공
            pp = p # 값을 발견하지 못하면 pp가 p를 가리키고
            p = p.next  # p는 뒤쪽 노드를 주목하여 뒤로 넘어감

        return False  # 삭제 실패

    def dump(self) -> None:
        """해시 테이블을 덤프"""
        for i in range(self.capacity):
            p = self.table[i]
            print(i, end='')
            while p is not None:
                print(f' ->{p.key}({p.value})',end='')
                p = p.next
            print()