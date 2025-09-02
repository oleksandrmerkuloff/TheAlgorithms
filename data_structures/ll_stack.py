from __future__ import annotations
from typing import Optional

from node import Node


class LinkedListStack:
    def __init__(self) -> None:
        self.head = None

    def __str__(self) -> str:
        if self.head:
            size = self.size()
            return f'Stack with first num: {self.head.val} and length: {size}'
        return 'Stack is empty'

    def __repr__(self) -> str:
        if self.head:
            size = self.size()
            return f'Stack with first num: {self.head.val} and length: {size}'
        return 'Stack is empty'

    def __eq__(self, stack: LinkedListStack) -> bool:
        if self.size() != stack.size():
            return False
        current = self.head
        guest = stack.head

        while current and guest:
            if current.val != guest.val:
                return False
            current = current.next
            guest = guest.next

        return True

    def push(self, val: int) -> None:
        self.head = Node(val=val, next=self.head)

    def pop(self) -> Optional[Node]:
        if not self.head:
            return None
        prev_head = self.head
        self.head = self.head.next
        return prev_head

    def peek(self) -> Optional[Node]:
        return None if not self.head else self.head

    def is_empty(self) -> bool:
        return True if not self.head else False

    def size(self) -> int:
        if not self.head:
            return 0

        counter = 0
        current = self.head

        while current:
            current = current.next
            counter += 1
        return counter
