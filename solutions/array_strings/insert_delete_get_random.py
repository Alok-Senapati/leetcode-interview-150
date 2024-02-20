from random import choice
from typing import List


class RandomizedSet:
    def __init__(self):
        self.elem_list = []
        self.index_dict = dict()

    def insert(self, val: int) -> bool:
        if val in self.index_dict:
            return False
        self.index_dict[val] = len(self.elem_list)
        self.elem_list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.index_dict:
            return False
        last_value, elem_idx = self.elem_list[-1], self.index_dict[val]
        self.elem_list[elem_idx], self.index_dict[last_value] = last_value, elem_idx
        self.elem_list.pop()
        del self.index_dict[val]
        return True

    def getRandom(self) -> int:
        return choice(self.elem_list)

    def list_elements(self) -> List[int]:
        return self.elem_list


if __name__ == '__main__':
    random_set = RandomizedSet()
    random_set.insert(1)
    random_set.insert(3)
    random_set.insert(4)
    random_set.insert(3)
    random_set.insert(5)
    random_set.insert(1)
    print(random_set.list_elements())
    random_set.remove(1)
    print(random_set.list_elements())
    print(random_set.getRandom())