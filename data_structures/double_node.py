from __future__ import annotations
from typing import Optional


class Node:
    def __init__(
            self,
            val: int,
            next: Optional[Node] = None,
            prev: Optional[Node] = None
            ) -> None:
        self.val = val
        self.next = next
        self.prev = prev

    def __str__(self) -> str:
        return str(self.val)

    def __repr__(self) -> str:
        return f'Current node value: {self.val}.\n'
