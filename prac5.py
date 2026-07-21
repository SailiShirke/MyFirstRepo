from queue import PriorityQueue

GOAL = [
    [1,2,3],
    [4,5,6],
    [7,8,0],
    ]
def find_position(board, value):
    for i in range(3):
        for j in range(3):
            if board[i][j] == value:
              return (i,j);

def manhattan_distance(board):
    distance = 0
    for i in range(3):
        for j in range(3):
            value = board[i][j]
            if value != 0:
                goal_i,goal_j = find_position(GOAL, value)
                distance += abs(i - goal_i) + abs(j - goal_j)
    return distance

def board_to_tuple(board):
    return tuple(tuple(row) for row in board)

def find_blank(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                return (i,j)

def get_neighbors(board):
    neighbors = []
    x,y = find_blank(board)
    moves = [(-1,0), (1,0), (0,-1), (0,1)]
    for dx,dy in moves:
        nx,ny = x + dx, y + dy
        if 0 <=nx < 3 and 0 <=ny <3:
            new_board = [row[:] for row in board]
            new_board[x][y],new_board[nx][ny] = new_board[nx][ny], new_board[x][y]
            neighbors.append(new_board)
    return neighbors

def a_star(start):
    pq = PriorityQueue()
    pq.put((manhattan_distance(start), 0, start,[]))
    visited ={}

    while not pq.empty():
         f, g, current, path = pq.get()
         board_tuple = board_to_tuple(current)
         if board_tuple in visited and visited[board_tuple] <= g:
             continue
         visited[board_tuple] = g

         if current == GOAL:
            return path + [current]
         for neighbor in get_neighbors(current):
            new_g = g + 1
            h = manhattan_distance(neighbor)
            new_f = new_g +h

            pq.put((new_f, new_g, neighbor, path +[current]))
    return None

def print_board(board):
    for row in board:
        print(row)
    print()

initial = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 5, 8]
]
solution = a_star(initial)

if solution:
    print("Shortest path found!\n")
    for step, board in enumerate(solution):
        print("Step", step)
        print_board(board)
else:
    print("No solution Found. ")
