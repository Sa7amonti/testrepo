play_again = True

game_board = {'A1': ' ',
              'B1': ' ',
              'C1': ' ',
              'A2': ' ',
              'B2': ' ',
              'C2': ' ',
              'A3': ' ',
              'B3': ' ',
              'C3': ' ',
              }


def print_board(board):
    print('  ' + ' | ' + 'A' + ' | ' + 'B' + ' | ' + 'C' + ' ')
    print('---+---+---+---')
    print('1 ' + ' | ' + board['A1'] + ' | ' + board['B1'] + ' | ' + board['C1'] + ' ')
    print('---+---+---+---')
    print('2 ' + ' | ' + board['A2'] + ' | ' + board['B2'] + ' | ' + board['C2'] + ' ')
    print('---+---+---+---')
    print('3 ' + ' | ' + board['A3'] + ' | ' + board['B3'] + ' | ' + board['C3'] + ' ')


def reset_board():
    for i in game_board:
        game_board[i] = ' '


def play_game(play_again_var):
    count = 0
    turn = 'X'

    for i in range(10):
        print_board(game_board)
        user_input = input(f'Pick an {turn} in a cell by choosing the Column Letter and the Row Number. (i.e. A1)\n')
        if user_input in game_board.keys():
            if game_board[user_input] == ' ':
                game_board[user_input] = turn
                count += 1
            else:
                print('This cell is not empty')
                if turn == 'X':
                    turn = 'O'
                else:
                    turn = 'X'
        if count >= 5:
            if game_board['A1'] != ' ' and game_board['A1'] == game_board['B1'] and game_board['A1'] == game_board['C1']:
                print(f'The winner is {turn}')
                print_board(game_board)
                break
            elif game_board['A1'] != ' ' and game_board['A1'] == game_board['A2'] and game_board['A1'] == game_board['A3']:
                print(f'The winner is {turn}')
                print_board(game_board)
                break
            elif game_board['A1'] != ' ' and game_board['A1'] == game_board['B2'] and game_board['A1'] == game_board['C3']:
                print(f'The winner is {turn}')
                print_board(game_board)
                break
            elif game_board['C1'] != ' ' and game_board['C1'] == game_board['C2'] and game_board['C1'] == game_board['C3']:
                print(f'The winner is {turn}')
                print_board(game_board)
                break
            elif game_board['C1'] != ' ' and game_board['C1'] == game_board['B2'] and game_board['C1'] == game_board['A3']:
                print(f'The winner is {turn}')
                print_board(game_board)
                break
            elif game_board['C3'] != ' ' and game_board['C3'] == game_board['B3'] and game_board['C3'] == game_board['A3']:
                print(f'The winner is {turn}')
                print_board(game_board)
                break
            elif game_board['B1'] != ' ' and game_board['B1'] == game_board['B2'] and game_board['B1'] == game_board['B3']:
                print(f'The winner is {turn}')
                print_board(game_board)
                break
            elif game_board['A2'] != ' ' and game_board['A2'] == game_board['B2'] and game_board['A2'] == game_board['C2']:
                print(f'The winner is {turn}')
                print_board(game_board)
                break
            else:
                pass
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

    user_answer = input('Would like to play again: Y/n')
    if user_answer == 'Y':
        reset_board()
        return play_again_var
    else:
        play_again_var = False
        return play_again_var


while play_again:
    play_again = play_game(play_again)
