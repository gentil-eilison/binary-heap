from tests import BinaryHeapOperationTests


# Conjunto 1: Dados Aleatórios Pequenos

first_set_data = (10, 5, 20, 1, 15, 30, 25)
first_set_tests = BinaryHeapOperationTests(first_set_data, 1)
first_set_tests.fill_heap()
first_set_tests.priority_change(((3, 50), (1, 8)))
first_set_tests.remove_items(3)
first_set_tests.heap_sort()
first_set_tests.display_high_priority()


# Conjunto 2: Sequência Crescente

second_set_data = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
second_set_tests = BinaryHeapOperationTests(second_set_data, 2)
second_set_tests.fill_heap()
second_set_tests.priority_change(((4, 15), (8, 3)))
second_set_tests.remove_items(5)
second_set_tests.heap_sort()
second_set_tests.display_high_priority()


# Conjunto 3: Sequência Decrescente
third_set_data = (50, 40, 30, 20, 10, 5, 3)
third_set_tests = BinaryHeapOperationTests(test_data=third_set_data, case_number=3)
third_set_tests.fill_heap()
third_set_tests.priority_change(((2, 60), (5, 1)))
third_set_tests.remove_items(3)
third_set_tests.heap_sort()
third_set_tests.display_high_priority()


# Conjunto 4: Dados Aleatórios Maiores
fourth_set_data = (13, 26, 19, 17, 24, 31, 22, 11, 8, 20, 5, 27, 18)
fourth_set_tests = BinaryHeapOperationTests(test_data=fourth_set_data, case_number=4)
fourth_set_tests.fill_heap()
fourth_set_tests.priority_change(((7, 35), (10, 12)))
fourth_set_tests.remove_items(4)
fourth_set_tests.heap_sort()
fourth_set_tests.display_high_priority()