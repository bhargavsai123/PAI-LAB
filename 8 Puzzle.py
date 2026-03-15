import heapq
goal = [[1,2,3],
        [4,5,6],
        [7,8,0]]

# Manhattan Distance Heuristic
def heuristic(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                goal_x = (value - 1) // 3
                goal_y = (value - 1) % 3
                distance += abs(i - goal_x) + abs(j - goal_y)
    return distance

def print_state(state):
    for row in state:
        print(row)
    print()

def get_neighbors(state):
    neighbors = []
    
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                x, y = i, j

    moves = [(-1,0),(1,0),(0,-1),(0,1)]

    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)

    return neighbors

def a_star(start):

    pq = []
    heapq.heappush(pq, (heuristic(start), 0, start, []))
    visited = set()

    while pq:
        f, g, state, path = heapq.heappop(pq)

        if state == goal:
            print("Solution Steps:\n")
            for step in path + [state]:
                print_state(step)
            return

        visited.add(tuple(map(tuple, state)))

        for neighbor in get_neighbors(state):
            if tuple(map(tuple, neighbor)) not in visited:
                heapq.heappush(pq, (g+1+heuristic(neighbor), g+1, neighbor, path+[state]))


# Initial state
start_state = [[1,2,3],
               [4,0,6],
               [7,5,8]]

a_star(start_state)