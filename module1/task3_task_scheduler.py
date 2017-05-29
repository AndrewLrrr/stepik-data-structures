class Scheduler:
    def __init__(self, buffer_size):
        self.__buffer = []
        self.__buffer_size = buffer_size
        self.__delay = 0
        self.__current_task_finish_time = 0
        self.__next_task_finish_time = 0

    def __is_buffer_full(self, task_arrival):
        return self.__current_task_finish_time > task_arrival and len(self.__buffer) > (self.__buffer_size - 1)

    def __check_buffer(self, task_arrival, task_duration):
        if not self.__buffer:
            self.__current_task_finish_time = self.__next_task_finish_time
        else:
            if self.__current_task_finish_time <= task_arrival:
                self.__buffer = self.__buffer[1::]
                if self.__buffer:
                    task = self.__buffer[0]
                    self.__current_task_finish_time = task['arrival'] + task['duration'] + task['delay']
                else:
                    self.__current_task_finish_time = self.__next_task_finish_time

        self.__buffer.append({'arrival': task_arrival, 'duration': task_duration, 'delay': self.__delay})

    def add(self, arrival, duration):
        if self.__is_buffer_full(arrival):
            return -1

        self.__delay = self.__next_task_finish_time - arrival

        if self.__delay < 0:
            self.__delay = 0

        self.__next_task_finish_time = arrival + duration + self.__delay

        self.__check_buffer(arrival, duration)

        return arrival + self.__delay


def main():
    buffer_size, packages = [int(i) for i in input().split()]
    scheduler = Scheduler(buffer_size)
    for package in range(packages):
        task = [int(i) for i in input().split()]
        print(scheduler.add(*task))


if __name__ == '__main__':
    main()


# buffer = 3
# 6 23 -> delay = 0 -> 6 + 0 = 6
# 15 44 -> (6 + 23 + 0) - 15 -> delay = 14 -> 15 + 14 = 29
# 24 28 -> (15 + 44 + 14) - 24 -> delay = 49 -> 24 + 49 = 73
# 35 15 -> (24 + 28 + 49) - 35 -> delay = 66 -> 35 + 66 = 101
# 40 20 -> buffer is full -> -1

# 6 + 0 = 6
# 15 + 14 = 29
# 24 + 49 = 73
# 35 + 66 = 101
# -1
