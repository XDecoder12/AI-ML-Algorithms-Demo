print("8 Box Puzzle Problem")
print("")
print("u to move the 0 up")
print("d to move the 0 down")
print("l to move the 0 left")
print("r to move the 0 right")
print("")

initial_state = [[3,7,2],
                 [1,8,4],
                 [0,6,5]]
goal_state = [[1,2,3],
              [4,5,6],
              [7,8,0]]

print("Initial State is: ")
for row in initial_state:
    print(" ".join(map(str, row)))
print("") 

def swap(demo_state, i1, i2, j1, j2):
    demo_state[i1][j1], demo_state[i2][j2] = demo_state[i2][j2], demo_state[i1][j1]

while initial_state != goal_state:    
    moves = []
    for i in range(3):
        for j in range(3):
            if initial_state[i][j] == 0 :
                blank_i, blank_j = i, j

    if blank_i > 1:
        moves.append("u")
    if blank_i < 3:
        moves.append("d")
    if blank_j > 1:
        moves.append("l")
    if blank_j < 3:
        moves.append("r")

    print("Current state is: ")
    for row in initial_state:
        print(" ".join(map(str, row)))
    print("Available moves are: ",moves)
    action = input("Enter your move: ")

    if action == "u":
        swap(initial_state, blank_i, blank_j, blank_i-1, blank_j)
        blank_i -= 1
    if action == "d":
        swap(initial_state, blank_i, blank_j, blank_i+1, blank_j)
        blank_i += 1
    if action == "l":
        swap(initial_state, blank_i, blank_j, blank_i, blank_j-1)
        blank_j -= 1
    if action == "r":
        swap(initial_state, blank_i, blank_j, blank_i, blank_j+1)
        blank_j += 1

print("Congratulations you have solved it !!!!!!!!!")

# initial_state = [[3,7,2],
#                  [1,8,4],
#                  [0,6,5]]

# goal_state = [[1,2,3],
#               [4,5,6],
#               [7,8,0]]

# print("Initial State:")
# for row in initial_state:
#     print(" ".join(map(str, row)))
# print()

# while initial_state != goal_state:
#     moves = []
    
#     # find blank
#     for i in range(3):
#         for j in range(3):
#             if initial_state[i][j] == 0:
#                 blank_i, blank_j = i, j
    
#     if blank_i > 0:    moves.append("u")
#     if blank_i < 2:    moves.append("d")
#     if blank_j > 0:    moves.append("l")
#     if blank_j < 2:    moves.append("r")
    
#     print("Current state:")
#     for row in initial_state:
#         print(" ".join(map(str, row)))
#     print("Available moves:", " ".join(moves))
    
#     action = input("Enter your move (u/d/l/r): ").lower().strip()
    
#     if action == "u" and blank_i > 0:
#         # swap with tile above
#         initial_state[blank_i][blank_j], initial_state[blank_i-1][blank_j] = \
#             initial_state[blank_i-1][blank_j], initial_state[blank_i][blank_j]
            
#     elif action == "d" and blank_i < 2:
#         initial_state[blank_i][blank_j], initial_state[blank_i+1][blank_j] = \
#             initial_state[blank_i+1][blank_j], initial_state[blank_i][blank_j]
            
#     elif action == "l" and blank_j > 0:
#         initial_state[blank_i][blank_j], initial_state[blank_i][blank_j-1] = \
#             initial_state[blank_i][blank_j-1], initial_state[blank_i][blank_j]
            
#     elif action == "r" and blank_j < 2:
#         initial_state[blank_i][blank_j], initial_state[blank_i][blank_j+1] = \
#             initial_state[blank_i][blank_j+1], initial_state[blank_i][blank_j]
            
#     else:
#         print("Invalid move or direction not allowed!")

# print("Congratulations! You solved it!")
# for row in initial_state:
#     print(" ".join(map(str, row)))