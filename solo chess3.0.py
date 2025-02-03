import random

letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
board = [[". "] * 8 for _ in range(8)]  
positions = set() 

piece_symbols = {
    "rook": "R ",
    "bishop": "B ",
    "queen": "Q ",
    "knight": "N ",
    "king": "K "
}


def rook_challenge(pos1, pos2):
    return pos1[0] == pos2[0] or pos1[1] == pos2[1]


def bishop_challenge(pos1, pos2):
    col1 = ord(pos1[0]) - ord('a')
    col2 = ord(pos2[0]) - ord('a')
    return abs(col1 - col2) == abs(pos1[1] - pos2[1])


def knight_challenge(pos1, pos2):
    col1 = ord(pos1[0]) - ord('a')
    col2 = ord(pos2[0]) - ord('a')
    row1, row2 = pos1[1], pos2[1]
    return (abs(col1 - col2), abs(row1 - row2)) in [(1, 2), (2, 1)]


def king_challenge(pos1, pos2):
    col1 = ord(pos1[0]) - ord('a')
    col2 = ord(pos2[0]) - ord('a')
    row1, row2 = pos1[1], pos2[1]
    return abs(col1 - col2) <= 1 and abs(row1 - row2) <= 1


def queen_challenge(pos1, pos2):
    return rook_challenge(pos1, pos2) or bishop_challenge(pos1, pos2)

def any_piece_can_capture(pos1, type1, pos2, type2):
    if type1 == "rook" and rook_challenge(pos1, pos2):
        return True
    elif type1 == "bishop" and bishop_challenge(pos1, pos2):
        return True
    elif type1 == "knight" and knight_challenge(pos1, pos2):
        return True
    elif type1 == "king" and king_challenge(pos1, pos2):
        return True
    elif type1 == "queen" and queen_challenge(pos1, pos2):
        return True
    return False


num_pieces = int(input("Number of pieces to place: "))


piece_types = ["rook", "bishop", "queen", "knight", "king"]
placed_pieces = []  

for _ in range(num_pieces):
    while True:
        col = random.choice(letters)
        row = random.randint(1, 8)
        piece_type = random.choice(piece_types)
        if (col, row) not in positions:  
            positions.add((col, row))
            placed_pieces.append((col, row, piece_type))
            break

for col, row, piece_type in placed_pieces:
    col_index = ord(col) - ord('a')
    row_index = 8 - row  
    board[row_index][col_index] = piece_symbols[piece_type]


print("\nChessboard:")
for i, row in enumerate(board):
    print(8 - i, " ".join(row))
print("  a  b  c  d  e  f  g  h")

capture_possible = False
for i in range(len(placed_pieces)):
    for j in range(i + 1, len(placed_pieces)):
        pos1, type1 = placed_pieces[i][:2], placed_pieces[i][2]
        pos2, type2 = placed_pieces[j][:2], placed_pieces[j][2]
        if any_piece_can_capture(pos1, type1, pos2, type2):
            print(f"\n{type1.capitalize()} at {pos1} can capture {type2.capitalize()} at {pos2}!")
            capture_possible = True

if not capture_possible:
    print("\nNo pieces can capture each other.")
