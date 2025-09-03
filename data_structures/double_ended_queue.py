from __future__ import annotations
from typing import Optional

from double_node import Node


class Deque:
    def __init__(self):
        self.head = None

    def __iter__(self):
        current = self.head
        while current:
            yield current.val
            current = current.next

    def __eq__(self, deque: Deque) -> bool:
        if self.size() != deque.size():
            return False
        f_head = self.head
        s_head = deque.head
        while f_head and s_head:
            if f_head.val != s_head.val:
                return False
            f_head, s_head = f_head.next, s_head.next
        return True

    def __str__(self) -> str:
        return f'Deque: {[str(x) for x in self]}'

    def __repr__(self) -> str:
        return f'Deque: {[str(x) for x in self]}'

    def create_new_node(
            self,
            val: int,
            next=None,
            prev=None
            ) -> Node:
        return Node(val=val, prev=prev, next=next)

    def get_last(self) -> Optional[Node]:
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            return current
        return None

    def append_left(self, val: int) -> None:
        old_head = self.head
        self.head = self.create_new_node(val=val, next=old_head)
        if old_head:
            old_head.prev = self.head

    def append_right(self, val: int) -> None:
        if not self.head:
            self.head = self.create_new_node(val)
        else:
            last = self.get_last()
            new_node = self.create_new_node(val, prev=last)
            last.next = new_node

    def pop_left(self) -> Optional[Node]:
        if self.head:
            first_node = self.head
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            return first_node
        return None

    def pop_right(self) -> Optional[Node]:
        last = self.get_last()
        if not last:
            return last
        elif last is self.head:
            prev_node = self.head
            self.head = None
        elif last.prev:
            prev_node = last.prev
            prev_node.next = None
        return last

    def peek_left(self) -> Optional[Node]:
        if self.head:
            return self.head
        return None

    def peek_right(self) -> Optional[Node]:
        last = self.get_last()
        return last

    def size(self) -> int:
        counter = 0
        current = self.head
        while current:
            counter += 1
            current = current.next
        return counter

    def is_empty(self) -> bool:
        return self.head is None
