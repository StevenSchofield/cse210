# Nested array to keep track of the current board state
game_board = [
    [0,0,0],
    [0,0,0],
    [0,0,0]]

# Simplify the translation process so I can use numbers in code and letters in display
piece_translation = [" ", "X", "O"]
index_translation = ["A", "B", "C"]

# Display the current board state, including indexes
def print_board(boardArray):
    print(" |1|2|3")
    for rowIndex in range(0,3):
        print_line = str(index_translation[rowIndex])
        print("--------")

        for index in boardArray[rowIndex]:
            print_line += "|"
            print_line += piece_translation[index]
        
        print(print_line)


print_board(game_board)