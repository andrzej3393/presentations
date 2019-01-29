from typing import List, Optional

a: int = 3
z = []


def f(b: str, c: Optional[List[int]]) -> None:
    return b


print(__annotations__)  # type: ignore
print(f.__annotations__)
