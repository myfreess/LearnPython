from typing import TypeVar
from enum import Enum, unique

@unique
class OutCome(Enum):
    """剪刀石头布中可用的输出策略"""
    SCISSOR = 1
    STONE   = 2
    PAPER   = 3

@unique
class Ordering(Enum):
    """定义大于，等于，小于关系"""
    EQ = 0
    GT = 1
    LT = -1

# 类型定义
Ordering = TypeVar("Ordering", Ordering)
OutCome  = TypeVar("OutCome",OutCome)





