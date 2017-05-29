#!/usr/bin/env python3


def main():
    max_size, count = (int(i) for i in input().split())
    net_buffer = Buffer(max_size)
    for package in stream(count):
        net_buffer.enter(*package)
    print(*net_buffer.log, sep="\n")


def stream(count):
    for i in range(count):
        yield (int(s) for s in input().split())


class Buffer():
    def __init__(self, max_size):
        self.max_size = max_size
        self._buffer = []
        self._proc_unlock = 0
        self.log = []

    def enter(self, arrival, duration):
        if self._check(arrival):
            self._push(arrival, duration)
        else:
            self.log.append(-1)

    def _push(self, arrival, duration):
        if not self._buffer:
            time_exit = max(self._proc_unlock, arrival)
        else:
            time_exit = max(self._buffer[-1], arrival)
        self._buffer.append(time_exit + duration)
        self.log.append(time_exit)

    def _check(self, time_check):
        while self._buffer and time_check >= self._buffer[0]:
            self._proc_unlock = self._buffer.pop(0)
        if len(self._buffer) < self.max_size:
            return True
        return False


if __name__ == "__main__":
    main()
