
#Code of A* Algorithm (without importing any library)
class Node:
    def __init__(self, pos, parent=None):
        self.pos = pos
        self.parent = parent
        self.g = self.h = self.f = 0

def a_star(start, goal, grid):
    open_list, closed_list = [Node(start)], []
    goal_node = Node(goal)

    while open_list:
        current = min(open_list, key=lambda x: x.f)
        if current.pos == goal_node.pos:
            return reconstruct_path(current)
        
        open_list.remove(current)
        closed_list.append(current)

        for neighbor_pos in get_neighbors(current.pos, grid):
            if any(closed.pos == neighbor_pos for closed in closed_list):
                continue
            neighbor = Node(neighbor_pos, current)
            neighbor.g = current.g + 1
            neighbor.h = abs(neighbor.pos[0] - goal[0]) + abs(neighbor.pos[1] - goal[1])
            neighbor.f = neighbor.g + neighbor.h

            if any(open_node.pos == neighbor.pos and open_node.g <= neighbor.g for open_node in open_list):
                continue
            open_list.append(neighbor)

    return None

def get_neighbors(pos, grid):
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    return [(pos[0] + dx, pos[1] + dy) for dx, dy in moves
            if 0 <= pos[0] + dx < len(grid) and 0 <= pos[1] + dy < len(grid[0]) and grid[pos[0] + dx][pos[1] + dy] == 0]

def reconstruct_path(node):
    path = []
    while node:
        path.append(node.pos)
        node = node.parent
    return path[::-1]

grid = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
goal = (4, 4)

path = a_star(start, goal, grid)
print("Path found:", path if path else "No path found")
