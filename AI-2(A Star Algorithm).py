import heapq

goal = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]]  

def h(state):
    return sum(state[i][j] != goal[i][j] and state[i][j] != 0
               for i in range(3) for j in range(3))

def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def neighbors(state):
    x, y = find_blank(state)
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right
    result = []
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            result.append(new_state)
    return result

# A* Algorithm
def a_star(start):
    pq = []
    heapq.heappush(pq, (h(start), 0, start, []))
    visited = set()

    while pq:
        f, g, state, path = heapq.heappop(pq)

        if state == goal:
            return path + [state]

        visited.add(str(state))

        for nb in neighbors(state):
            if str(nb) not in visited:
                heapq.heappush(pq, (g + 1 + h(nb), g + 1, nb, path + [state]))
    return None

# Example run
start_state = [[1, 2, 3],
               [4, 0, 6],
               [7, 5, 8]]

solution = a_star(start_state)

for step in solution:
    for row in step:
        print(row)
    print("------")
