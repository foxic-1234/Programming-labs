print('Програмування. Частина 2. Лаботаротна робота №4, Коломоєць Ольги ФБ-44 Варіант 9')
import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        if self._queue:
            return heapq.heappop(self._queue)[-1]
        raise IndexError("Спроба видалення з порожньої черги")

    def is_empty(self):
        return len(self._queue) == 0

    def peek(self):
        if self._queue:
            return self._queue[0][-1]
        raise IndexError("Спроба перегляду елемента в порожній черзі")

if __name__ == "__main__":
    pq = PriorityQueue()
    pq.push("Task 1", 1)
    pq.push("Task 2", 3)
    pq.push("Task 3", 2)
    
    while not pq.is_empty():
        print(pq.pop())
