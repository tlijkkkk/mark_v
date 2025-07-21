from abc import abstractmethod, ABC
from typing import List

class NestedInteger(ABC):
    @abstractmethod
    def isInteger(self) -> bool:
        pass

    @abstractmethod
    def getInteger(self) -> int:
        pass
    
    @abstractmethod
    def getList(self) -> List["NestedInteger"]:
        pass

class Solution:
    def nested_list_weight_sum(self, nested_integer: NestedInteger, level: int) -> int:
        if nested_integer.isInteger():
            return nested_integer.getInteger() * level
        
        tmp_sum = 0
        for ni in nested_integer.getList():
            tmp_sum += self.nested_list_weight_sum(ni, level + 1)

        return tmp_sum