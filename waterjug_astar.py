from heapq import heappush, heappop

def heuristic(state, target):
    return min(abs(state[0]-target), abs(state[1]-target))

def water_jug_a_star(capA, capB, target):

    start = (0,0)
    open_list = []
    visited = set()
    
    heappush(open_list,(0,0,start,[]))

    while open_list:
        f,g,state,path = heappop(open_list)
        if state in visited:
            continue
        visited.add(state)
        path = path + [state]
        a,b = state
        if a == target or b == target:
            return path
        next_states = [
            (capA,b),
            (a,capB),
            (0,b),
            (a,0),
            (max(0,a-(capB-b)), min(capB,b+a)),
            (min(capA,a+b), max(0,b-(capA-a)))
        ]
        for ns in next_states:
            if ns not in visited:
                g_new = g + 1
                h = heuristic(ns,target)
                heappush(open_list,(g_new+h,g_new,ns,path))

capA = int(input("Enter capacity of Jug A: "))
capB = int(input("Enter capacity of Jug B: "))
target = int(input("Enter target amount: "))

solution = water_jug_a_star(capA, capB, target)

if solution:
    print("Solution steps:")
    for step in solution:
        print(step)
else:
    print("No solution found")
