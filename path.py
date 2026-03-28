import heapq
import time
import os

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    open_set = []
    heapq.heappush(open_set, (0 + heuristic(start, goal), start))
    came_from = {}
    g_score = {start: 0}
    while open_set:
        current = heapq.heappop(open_set)[1]
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor = (current[0] + dx, current[1] + dy)
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and grid[neighbor[0]][neighbor[1]] == 0:
                tentative_g_score = g_score[current] + 1
                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    g_score[neighbor] = tentative_g_score
                    f_score = tentative_g_score + heuristic(neighbor, goal)
                    heapq.heappush(open_set, (f_score, neighbor))
                    came_from[neighbor] = current
    return None

def print_step(grid,path,step_index,start,goal):
    display_grid = [row[:] for row in grid] 
    for i in range(step_index + 1):
        x, y = path[i]
        display_grid[x][y] = '*'
    r,c = path[step_index]
    display_grid[r][c] = 'X'
    display_grid[start[0]][start[1]] = 'S'
    display_grid[goal[0]][goal[1]] = 'G'
    for row in display_grid:
        print(' '.join(str(cell) for cell in row))
    print("\n")

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
print("Enter the grid (0 for open cell, 1 for wall):")
grid = [list(map(int, input().split())) for _ in range(rows)]
start = tuple(map(int, input("Enter start position (row col): ").split()))
goal = tuple(map(int, input("Enter goal position (row col): ").split()))
path = astar(grid, start, goal)
if path:
    print("Path found:")
    for step_index in range(len(path)):
        print_step(grid, path, step_index, start, goal)
        time.sleep(0.5)
else:
    print("No path found.")