from __future__ import annotations
from typing import Optional


class Node:
    def __init__(self, val: int, next: Optional[Node] = None) -> None:
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return f'Node value: {self.val}'

    def __repr__(self) -> str:
        return f'Node value: {self.val}.'
