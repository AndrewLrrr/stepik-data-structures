import queue as Q


class TaskManager:
    def __init__(self, p):
        self.__processes_q = Q.PriorityQueue(p)
        self.__free_processors_q = Q.PriorityQueue(p)
        self.__process_memory = {}
        for i in range(p):
            self.__free_processors_q.put(i)

    def add(self, task_time):
        if not self.__free_processors_q.empty():
            processor = self.__free_processors_q.get()
            time = self.__process_memory[processor] if processor in self.__process_memory else 0
        else:
            time, processor = self.__processes_q.get()
        if task_time == 0:
            self.__free_processors_q.put(processor)
            self.__process_memory[processor] = time
        else:
            self.__processes_q.put((time + task_time, processor))

        return processor, time


def main():
    processors, total_tasks = [int(i) for i in input().split()]
    tasks = [int(i) for i in input().split()]
    tm = TaskManager(processors)
    for task in tasks:
        print(*tm.add(task))


if __name__ == '__main__':
    main()
