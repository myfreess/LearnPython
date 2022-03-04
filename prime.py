from math import floor
from typing import List, TypeAlias, TypeVar


# 表类型
# memo[n - 1]表示第n个数的素性
# memo[0] 永远为false
Memo_t: TypeAlias = List[bool]

class PrimeF:
    table: Memo_t
    def __init__(self) -> None:
        pass
    # 暂时没想到初始化怎么做好


PrimeF = TypeVar("PrimeF", PrimeF)



