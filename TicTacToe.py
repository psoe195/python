### History ###
# 1. downloaded from Github
# 2. started debugging

def display_board(user_positions):
    print('   |   |   ')
    print(' {} | {} | {} '.format(user_positions[7], user_positions[8], user_positions[9]))
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(' {} | {} | {} '.format(user_positions[4], user_positions[5], user_positions[6]))
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(' {} | {} | {} '.format(user_positions[1], user_positions[2], user_positions[3]))
    print('   |   |   ')


def input_user_symbol(user_name):
    user_1 = ''
    user_2 = ''

    user_input = {'user_1': '', 'user_2': ''}

    while (user_1 == ''):
        user_1 = input('{} : choose your symbol X or O : '.format(user_name))
        if user_1.upper() not in ('X', 'O'):
            user_1 = ''
            print('Input is not valid. Please enter X or O')
            continue
        else:
            if user_1.upper() == 'X':
                user_2 = 'O'
            elif user_1.upper() == 'O':
                user_2 = 'X'
            user_input['user_1'] = user_1.upper()
            user_input['user_2'] = user_2.upper()
            break
    return user_input

def check_game_status(board, user_symbol):
    game_over = False

    if (user_symbol == board[1] and user_symbol == board[2] and user_symbol == board[3]) \
        or (user_symbol == board[4] and user_symbol == board[5] and user_symbol == board[6]) \
        or (user_symbol == board[7] and user_symbol == board[8] and user_symbol == board[9]) \
        or (user_symbol == board[1] and user_symbol == board[5] and user_symbol == board[9]) \
        or (user_symbol == board[3] and user_symbol == board[5] and user_symbol == board[7]) \
        or (user_symbol == board[1] and user_symbol == board[4] and user_symbol == board[7]) \
        or (user_symbol == board[2] and user_symbol == board[5] and user_symbol == board[8]) \
        or (user_symbol == board[3] and user_symbol == board[6] and user_symbol == board[9]):
        game_over = True
    else:
        game_over = False
    return game_over

def check_game_is_draw(board):
    if  ( board.count('X') + board.count('O')  == 9 ):
        return True
    else:
        return False

def input_next_move(player_name):
    valid_input = False
    while not valid_input:
        try:
            num = int(input('{}, Enter your move (1 to 9) : '.format(player_name)))
            if num in (1,2,3,4,5,6,7,8,9):
                valid_input = True
            else:
                print('Invalid input. Please enter a number between 1 to 9')
        except:
            print('Invalid input. Please enter numbers only between 1 to 9')

    return num

def input_player_names():
    player_1 = input('Enter player 1 name : ')
    player_2 = input('Enter player 2 name : ')
    player_names = {'player_1' : player_1, 'player_2' : player_2}
    return player_names

def display_game_over(player_name):
    print('Game over! {} wins. '.format(player_name))

def display_draw():
    print('The game is draw. No body wins.')

player_names = input_player_names()
print('Player 1 is {}. Player 2 is {}'.format(player_names['player_1'], player_names['player_2']))

user_symbol = input_user_symbol(player_names['player_1'])
print('{}\'s symbol is {}'.format(player_names['player_1'], user_symbol['user_1']))
print('{}\'s symbol is {}'.format(player_names['player_2'], user_symbol['user_2']))


still_playing = True
current_player = player_names['player_1']
current_symbol = user_symbol['user_1']

# init user_board
user_board = ['1', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

while still_playing:

    # display board
    display_board(user_board)

    # input move and check for valid move or not
    input_check = False
    while not input_check:
        pos = input_next_move(current_player)
        if user_board[pos] != ' ':
            print('Invalid input. Already taken.')
            continue
        else:
            input_check = True
            break

    user_board[pos] = current_symbol

    game_over = check_game_status(user_board, current_symbol)
    if game_over == True:
        display_game_over(current_player)
        still_playing = False
        display_board(user_board)
        break
    # check game is draw
    elif check_game_is_draw(user_board) == True:
        still_playing = False
        display_draw()
        display_board(user_board)
        break

    # switch turn to another player
    if current_player == player_names['player_1']:
        current_player = player_names['player_2']
        current_symbol = user_symbol['user_2']
    else:
        current_player = player_names['player_1']
        current_symbol = user_symbol['user_1']
