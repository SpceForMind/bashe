import typing


class HeapManager:
    def __init__(self,
                 heap_size: int,
                 max_count_to_take : int):
        self.__heap = [_ for _ in range(heap_size)]
        self.__heap_size = heap_size
        self.__max_count_to_take = max_count_to_take

    def refresh(self):
        self.__heap = [_ for _ in range(self.__heap_size)]

    def size(self) -> int:
        return len(self.__heap)

    def remove_items(self,
                     count: int):
        if count > self.__max_count_to_take or count < 1:
            raise ValueError(f'Count: {count} out of range 1 <= count <= 3')

        if count > len(self.__heap):
            raise IndexError(f'len: {len(self.__heap)} < count: {count}')

        for i in range(count):
            self.__heap.pop()
    def remove_items_ids(self,
                     ids: typing.List[int]):
        for id_ in ids:
            self.__heap.remove(id_)

    def is_empty(self) -> bool:
        return len(self.__heap) == 0