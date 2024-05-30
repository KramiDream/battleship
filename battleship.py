import random

class Ship: # обязательное усл задачи
    def __init__(self, position):
        self.position = position
        self.hits = [False] * len(position)

class Board: # обязательное усл задачи
    def __init__(self):
        self.board = [["O" for _ in range(6)] for _ in range(6)]
        self.ships = []

    def place_ship(self, ship):
        for x, y in ship.position:
            self.board[x][y] = "■"
        self.ships.append(ship)

    def print_board(self):
        print("  | 1 | 2 | 3 | 4 | 5 | 6 |")
        print("---------------------------")
        for i in range(6):
            print(f"{i+1} | {' | '.join(self.board[i])} |")
        print("---------------------------")

# расстояние между к. не меньше 1 кл.
def check_distance(board, x, y):
    for i in range(-1, 2):
        for j in range(-1, 2):
            if 0 <= x + i < 6 and 0 <= y + j < 6:
                if board.board[x + i][y + j] != "O":
                    return False
    return True

def place_ships():
    while True:
        board = Board()
        place_ships_create(board)
        if len(board.ships) == 7:
            return board
    return null

def place_ships_create(board):
    ships = []
    for ship_length in [3, 2, 2, 1, 1, 1, 1]:
        placed = False
        k = 0 #флажок
        while not placed:
            x, y = random.randint(0, 5), random.randint(0, 5)
            if k > 50: break

            k = k + 1
            direction = random.choice(["horizontal", "vertical"])
            position = []

            if direction == "horizontal":
                if y + ship_length > 6:
                    continue
                for i in range(ship_length):
                    if board.board[x][y + i] != "O" or not check_distance(board, x, y + i):
                        break
                    position.append((x, y + i))
                if len(position) == ship_length:
                    placed = True

            elif direction == "vertical":
                if x + ship_length > 6:
                    continue
                for i in range(ship_length):
                    if board.board[x + i][y] != "O" or not check_distance(board, x + i, y):
                        break
                    position.append((x + i, y))
                if len(position) == ship_length:
                    placed = True
        if len(position) != 0:
            ships.append(Ship(position))
            board.place_ship(Ship(position))
    return ships

#ход игрока, потом ход ИИ
def player_turn(board, x, y):
    if board.board[x][y] == "■":
        for ship in board.ships:
            for i, (ship_x, ship_y) in enumerate(ship.position):
                if ship_x == x and ship_y == y:
                    ship.hits[i] = True
                    board.board[x][y] = "X"
                    print("Попал!")
                    if all(ship.hits):
                        print("Вы уничтожили корабль!")
                    return
    elif board.board[x][y] == "O":
        board.board[x][y] = "T"
        print("Промах!")
    else:
        raise ValueError("Поменяйте координаты, вы уже стреляли по этой позиции.")


