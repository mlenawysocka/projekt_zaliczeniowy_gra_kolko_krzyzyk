from conversation import player1name, player2name, players_choice, players_input
from game_logic import show_table, place_marker, check_win, full_table_check, rematch

if __name__ == "__main__":
    print(f"Hello {player1name} and {player2name}! It's time to play a game. Welcome to Tic Tac Toe!")
    i = 1
    players = players_input(player1={player1name}, player2={player2name})
    table = ["#"] * 10
    while True:
        game_on = full_table_check(table)
        while not game_on:
            if i % 2 == 0:
                current_player = player2name
                marker = players[1]
            else:
                current_player = player1name
                marker = players[0]
            position = players_choice(current_player, table)
            place_marker(table, marker, int(position))
            show_table(table)
            i += 1
            if check_win(table, marker):
                print("Win, win win!!!")
                break
            game_on = full_table_check(table)
        if not rematch():
            break
        else:
            i = 1
            players = players_input(player1={player1name}, player2={player2name})
            table = ['#'] * 10