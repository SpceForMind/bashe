class ComputerPlayer:
    def __init__(self,
                 max_count_to_take : int):
        self.__max_count_to_take = max_count_to_take

    def step(self,
             heap_size: int):

        for i in range(1, self.__max_count_to_take + 1):
            if (heap_size - i) % (self.__max_count_to_take + 1) == 0:
                return i

        return self.__max_count_to_take