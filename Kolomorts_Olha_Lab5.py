print('Програмування. Частина 2. Лаботаротна робота №6, Коломоєць Ольги ФБ-44 Варіант 9')
from collections import deque

graph = {
    'A': ['B', 'D'],
    'B': ['A', 'E'],
    'C': ['E', 'F'],
    'D': ['A', 'E'],
    'E': ['B', 'D', 'C'],
    'F': ['C']
}

def bfs_path(graph, start, goal):
    visited = set()
    queue = deque([(start, [start])])
    while queue:
        current, path = queue.popleft()
        if current == goal:
            return path
        visited.add(current)
        for neighbor in graph[current]:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))
    return None

path_ac = bfs_path(graph, 'A', 'C')
path_bc = bfs_path(graph, 'B', 'C')

def find_common_suffix(path1, path2):
    common = []
    i, j = len(path1) - 1, len(path2) - 1
    while i >= 0 and j >= 0 and path1[i] == path2[j]:
        common.insert(0, path1[i])
        i -= 1
        j -= 1
    return common

common_section = find_common_suffix(path_ac, path_bc)

print(f"Шлях A -> C: {path_ac}")
print(f"Шлях B -> C: {path_bc}")
print(f"Спільна дільниця: {common_section}")
print(f"Її довжина: {len(common_section)}")
