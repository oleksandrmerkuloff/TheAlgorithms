from __future__ import annotations
from typing import Optional


class Stack:
    def __init__(self) -> None:
        self.storage = []

    def __str__(self) -> str:
        return str(self.storage)

    def __repr__(self) -> str:
        return str(self.storage)

    def __eq__(self, stack: Optional[Stack | list]) -> bool:
        return self.storage == stack

    def push(self, new_item: int) -> None:
        self.storage = [new_item] + self.storage

    def power_push(self, *items: list[int]) -> None:
        self.storage = list(items) + self.storage

    def pop(self) -> Optional[int | bool]:
        if self.storage:
            head = self.storage[0]
            self.storage = self.storage[1:]
            return head  # type: ignore
        return False

    def peek(self) -> Optional[int | list]:
        return self.storage[0] if self.storage else []

    def is_empty(self) -> bool:
        return True if not self.storage else False

    def size(self) -> int:
        return len(self.storage)
