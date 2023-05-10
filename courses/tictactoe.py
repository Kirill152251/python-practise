def display_board(board):
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('---|---|---')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('---|---|---')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])


def get_player_move(current_board: list, actual_player):
    print()
    while True:
        player_input = input(f'Move belongs to "{actual_player}". Enter your move (1-9): ')
        if player_input.isdigit() and len(player_input) == 1:
            if current_board[int(player_input)] == ' ':
                return int(player_input)
            else:
                print('Cell is already filled.')
        else:
            print('Incorrect input. Try again.')


def change_player(actual_player):
    if actual_player == 'O':
        return 'X'
    else:
        return 'O'


def update_board(current_board: list, position, actual_player):
    current_board[position] = actual_player
    return current_board


def print_tie_message():
    print()
    print('TIE!')
    start_new_game()


def print_win_message(winner):
    print()
    print(winner, '- WINNER!')
    start_new_game()


def start_new_game():
    print()
    answer = input('Wanna play more? Y / N ').upper()
    if answer == 'N':
        pass
    elif answer == 'Y':
        restart_game_conditions()
        print('\n' * 100)
        start_game()
    else:
        print('Incorrect input. Type "Y" or "N".')
        start_new_game()


def get_game_state(current_board: list):
    winner_comb = [
        (1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 5, 9), (3, 5, 7)
    ]
    for comb in winner_comb:
        one, two, tree = current_board[comb[0]], current_board[comb[1]], current_board[comb[2]]
        if one == two == tree == 'O' or one == two == tree == 'X':
            return 'end'
    if current_board.count(' ') == 0:
        return 'tie'
    return 'continue'


def restart_game_conditions():
    global game_board
    global current_player
    game_board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    current_player = 'O'


def start_game():
    global game_board
    global current_player
    display_board(game_board)
    while True:
        play_move = get_player_move(game_board, current_player)
        game_board = update_board(game_board, play_move, current_player)
        display_board(game_board)
        state = get_game_state(game_board)
        if state == 'end':
            print_win_message(current_player)
            break
        elif state == 'tie':
            print_tie_message()
            break
        else:
            pass
        current_player = change_player(current_player)


game_board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
current_player = 'O'
start_game()
