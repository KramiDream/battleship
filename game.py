import battleship
import random

def game_loop():
    player_board = battleship.place_ships()
    computer_board = battleship.place_ships()
    # Условия победы!!!
    while True:
        print("\nХод игрока:")
        player_board.print_board()
        try:
            x, y = map(int, input("Введите координаты цели (например, 1 2): ").split())
            x -= 1
            y -= 1
            battleship.player_turn(computer_board, x, y)
        except (ValueError, IndexError):
            print("Неверный ввод. Пожалуйста, введите координаты еще раз.")
            continue

        if all(all(hit for hit in ship.hits) for ship in computer_board.ships):
            print("Вы потопили все корабли ИИ;) Вы победили!")
            break

        print("\nХод компьютера:")
        x = random.randint(0, 5)
        y = random.randint(0, 5)
        battleship.player_turn(player_board, x, y)

        if all(all(hit for hit in ship.hits) for ship in player_board.ships):
            print("Компьютер побеждает! Он потопил все ваши корабли.")
            break

if __name__ == "__main__":
    game_loop()
