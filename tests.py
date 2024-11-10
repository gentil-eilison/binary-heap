from classes import BinaryHeap


class BinaryHeapOperationTests:
    def __init__(self, test_data: tuple[int], case_number: int = 1) -> None:
        self.__test_data = test_data
        self.__binary_heap = BinaryHeap()
        self.case_number = case_number
    
    @property
    def test_data(self) -> tuple[int]:
        return self.__test_data
    
    @test_data.setter
    def test_data(self, new_test_data: tuple[int]) -> None:
        self.__test_data = new_test_data

    def fill_heap(self) -> None:
        print(f"======= Construção do Heap {self.case_number} =======")
        for value in self.__test_data:
            self.__binary_heap.insert(value)
            self.__binary_heap.display_heap()
    
    def priority_change(self, new_priorities: tuple[tuple[int, int]]) -> None:
        print(f"======= Alteração de Prioridade {self.case_number} =======")
        for priority_data in new_priorities:
            idx, priority = priority_data[0], priority_data[1]
            self.__binary_heap.change_priority(idx, priority)
            print("Prioridade alterada!")
            self.__binary_heap.display_heap()
    
    def remove_items(self, count: int) -> None:
        print(f"======= Remoções {self.case_number} =======")
        for _ in range(count):
            self.__binary_heap.remove()
    
    def heap_sort(self) -> None:
        print(f"======= Usando o Heap Sort {self.case_number} =======")
        sorted_list = self.__binary_heap.heap_sort()
        print(sorted_list[1:])
        
    def display_high_priority(self) -> None:
        print(f"======= Elemento de Alta Prioridade {self.case_number} =======")
        print(self.__binary_heap.get_high_priority())
 