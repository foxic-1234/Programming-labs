print('Програмування. Частина 2. Лаботаротна робота №5, Коломоєць Ольги ФБ-44 Варіант 9')
import heapq

graph = {
    'A': [('B', 2), ('C', 5)],
    'B': [('A', 2), ('D', 4), ('E', 1)],
    'C': [('A', 5), ('F', 3)],
    'D': [('B', 4), ('G', 2)],
    'E': [('B', 1), ('G', 3)],
    'F': [('C', 3), ('H', 2)],
    'G': [('D', 2), ('E', 3), ('I', 1)],
    'H': [('F', 2), ('I', 4)],
    'I': [('G', 1), ('H', 4)]
}

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    previous_nodes = {node: None for node in graph}
    queue = [(0, start)]

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(queue, (distance, neighbor))

    return distances, previous_nodes

def shortest_path(graph, start, end):
    distances, previous_nodes = dijkstra(graph, start)
    path = []
    current = end

    while current is not None:
        path.insert(0, current)
        current = previous_nodes[current]

    return path, distances[end]

start_node = 'A'
end_node = 'I'

path, distance = shortest_path(graph, start_node, end_node)

print(f"Найкоротший шлях від {start_node} до {end_node}: {' -> '.join(path)}")
print(f"Загальна довжина шляху: {distance}")
