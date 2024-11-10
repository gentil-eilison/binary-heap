from typing import Any
import math


class HeapItem:
    def __init__(self, value: Any, key: int|None = None) -> None:
        self.__value = value
        self.__key: int = key or value
    
    @property
    def value(self) -> Any:
        return self.__value
    
    @value.setter
    def value(self, new_value: Any) -> None:
        self.__value = new_value
    
    @property
    def key(self) -> int:
        return self.__key
    
    @key.setter
    def key(self, new_key: int) -> None:
        self.__key = new_key
    
    def __repr__(self):
        return f"{self.__value}"
    

class BinaryHeap:
    def __init__(self) -> None:
        self.__list: list[HeapItem] = [math.inf]
    
    def go_up(self, idx: int) -> None:
        parent_node_idx = idx // 2
        if parent_node_idx >= 1:
            if self.__list[idx].key > self.__list[parent_node_idx].key:
                self.__list[idx], self.__list[parent_node_idx] = (
                    self.__list[parent_node_idx],
                    self.__list[idx]
                )
                self.go_up(parent_node_idx)
    
    def go_down(self, idx: int, n: int) -> None:
        child_node_idx = 2 * idx

        if child_node_idx <= n:
            if child_node_idx < n:
                if self.__list[child_node_idx + 1].key > self.__list[child_node_idx].key:
                    child_node_idx += 1
            if self.__list[idx].key < self.__list[child_node_idx].key:
                print(f"Descendo o valor {self.__list[idx].value}")
                self.__list[idx], self.__list[child_node_idx] = (
                    self.__list[child_node_idx],
                    self.__list[idx]
                )
                self.display_heap()
                self.go_down(child_node_idx, n)

    def insert(self, item: int) -> None:
        self.__list.append(HeapItem(item))
        self.go_up(len(self.__list) - 1)

    def remove(self) -> None:
        if len(self.__list) != 0:
            self.__list.pop(1)
            self.__list.insert(1, self.__list[-1])
            self.__list.pop()
            print("Removi o de alta prioridade e coloquei o último em alta prioridade")
            self.display_heap()
            self.go_down(1, len(self.__list) - 1)
        else:
            raise Exception("Couldn't remove item from binary heap")

    def change_priority(self, idx: int, new_priority: int) -> None:
        self.__list[idx].key = new_priority
        self.__list[idx].value = new_priority
        self.arrange()

    def get_high_priority(self) -> int:
        return self.__list[1].value
        
    def arrange(self) -> None:
        idx = len(self.__list) // 2
        while idx > 1:
            idx -= 1
            self.go_down(idx, len(self.__list) - 1)
        
    def heap_sort(self) -> list[int]:
        self.arrange()
        original_binary_heap = self.__list.copy()
        m = len(self.__list) - 1
        while m > 1:
            self.__list[1], self.__list[m] = (
                self.__list[m],
                self.__list[1]
            )
            m -= 1
            print("Troquei")
            self.display_heap()
            self.go_down(1, m)
        sorted_list = self.__list.copy()
        self.__list = original_binary_heap
        return sorted_list

    def display_heap(self) -> None:
        output = "["
        for item in self.__list[1:len(self.__list) - 1]:
            output += f"{item.value}, "
        output += f"{self.__list[-1].value}]"
        print(output)
