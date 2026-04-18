import heapq

goal = [1,2,3,4,5,6,7,8,0]

def heuristic(state): 
    distance = 0
    for i in range(9):
        if state[i] == 0:
            continue
        goal_pos = goal.index(state[i])
        distance += abs(i//3 - goal_pos//3) + abs(i%3 - goal_pos%3)
    return distance

def get_neighbours(state):
    neighbours = []
    i = state.index(0)
    moves = [-3,3,-1,1]
    for move in moves:
        new_i = i + move

        if new_i < 0 or new_i >= 9:
            continue
        if i % 3 == 0 and move == -1:
            continue
        if i % 3 == 2 and move == 1:
            continue

        new_state = state[:]
        new_state[i], new_state[new_i] = new_state[new_i], new_state[i]
        neighbours.append(new_state)
    return neighbours

def a_star(start):
    open_list = []
    heapq.heappush(open_list, (0, start, []))
    visited = set()

    while open_list:
        cost, state, path = heapq.heappop(open_list)

        if tuple(state) in visited:
            continue
        visited.add(tuple(state))

        if state == goal:
            return path
        
        for neighbour in get_neighbours(state):
            g = len(path) + 1
            h = heuristic(neighbour)
            f = g + h
            heapq.heappush(open_list, (f, neighbour, path + [neighbour]))

#start = [1,4,7,0,3,8,6,5,2] this can't be solved
start = [1, 8, 2, 0, 4, 3, 7, 6, 5]
solution = a_star(start)

print("A* Solution Steps: ")
for step in solution:
    print(step)