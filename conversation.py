from game_logic import check_space


while True:
    player1name = input("Hello Player 1. What's your name? ")
    if player1name.isdigit() or player1name.isspace():
        player1name = input("Your name cannot be a number or blank. Again, what's your name? ")
    elif len(player1name) < 2:
        player1name = input("Your name cannot be a single letter. Again, what's your name? ")
    elif player1name[0].islower():
        player1name = input("Please write your name with an upper first letter. ")
    player2name = input("Hello Player 2. What's your name? ")
    if player2name.isdigit() or player2name.isspace():
        player2name = input("Your name cannot be a number or blank. Again, what's your name? ")
    elif len(player2name) < 2:
        player2name = input("Your name cannot be a single letter. Again, what's your name? ")
    elif player2name[0].islower():
        player2name = input("Please write your name with an upper first letter. ")
    break


def players_input(player1, player2):
    player1 = input(f"{player1name}, do you want to play as 'X' or 'O'? ")
    while True:
        if player1.upper() == 'X':
            player2 = 'O'
            print(
                f'{player1name}, you have chosen to play as {player1.upper()}. Therefore {player2name} will be {player2}.')
            return player1.upper(), player2
        elif player1.upper() == 'O':
            player2 = 'X'
            print(
                f'{player1name}, you have chosen to play as {player1.upper()}. Therefore {player2name} will be {player2}.')
            return player1.upper(), player2
        else:
            player1 = input(f"{player1name}, you can only choose 'X' or 'O', so do you want to play as 'X' or 'O'? ")


def players_choice(current_player, table):
    choice = int(input(f"{current_player}, choose an empty space between 1 and 9: "))
    if choice not in range(1, 10):
        choice = int(input(f"{current_player}, you can only place a number between 1 and 9! So..? "))
    while not check_space(table, int(choice)):
        choice = input("This space isn't free. Please choose an empty space between 1 and 9: ")
    return choice
