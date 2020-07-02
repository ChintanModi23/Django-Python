import random

def game_board(board):
    print(board[0] + '|' +board[1] + '|' + board[2])
    print(board[3] + '|' +board[4] + '|' + board[5])
    print(board[6] + '|' +board[7] + '|' + board[8])

def choose_mark():
    mark = input('Player choose your team, X or O:  ')
    return (('X','O') if mark.upper() == 'X' else ('O','X') if mark.upper() == 'O' else 'Wrong Choice')

def who_goes_first():
    toss = random.randint(0,1)
    return('Player' if toss == 1 else 'Computer')

def make_move(board_cells, position, team):
    if position in range (0,9):
        board_cells[position] = team


def iswin(board_cells, turn):
    if (board_cells[0]==board_cells[1]==board_cells[2] or board_cells[3]==board_cells[4]==board_cells[5] or
        board_cells[6]==board_cells[7]==board_cells[8] or board_cells[0]==board_cells[3]==board_cells[6] or
        board_cells[1]==board_cells[4]==board_cells[7] or board_cells[2]==board_cells[5]==board_cells[8] or
        board_cells[0]==board_cells[4]==board_cells[8] or board_cells[2]==board_cells[4]==board_cells[6] ):
        return True

def isboardfull(board_cells):
    isfull = True
    for i in range(0,9):
        if board_cells[i].isdigit():
            isfull = False
    return isfull

def play_again():
    choice = input('Do you want to play again? Y/N:').upper()
    return choice == 'Y'


while(True):
    print("LET'S PLAY TO TIC TAC TOE !!!")
    board_cells = [str(x )for x in range(0, 9)]
    game_board(board_cells)

    p,c = choose_mark()
    print("Player team is : ", p) 
    print("Computer team is : " ,c)

    turn = who_goes_first()
    print( turn + ' will go first')

    status= True
    while(status):
        if turn == 'Player':
            place = int(input(turn + " choose a position to make your move: "))
            if place in range(0,9):
                if board_cells[place] != 'X' and board_cells[place] != 'O':
                    make_move(board_cells, place, p)
                    game_board(board_cells)
                else:
                    print('Choose correct position!')
                    continue
            else:
                print('Choose correct position!')
            if iswin(board_cells, turn):
                game_board(board_cells)
                print('Player won!!')
                status=False
            else:
                if isboardfull(board_cells):
                    game_board(board_cells)
                    print('TIE Game!!')
                    status=False
                    break
                else:
                    turn='Computer'

        else:
            if board_cells[4] == '4' and (board_cells[1] == board_cells[7] or board_cells[3] == board_cells[5] or board_cells[0] == board_cells[8] 
            or board_cells[2] == board_cells[6]):
                place = 4
            elif board_cells[0] == '0' and (board_cells[1] == board_cells[2] or board_cells[3] == board_cells[6] or board_cells[4] == board_cells[8]):
                place = 0
            elif board_cells[2] == '2' and (board_cells[1] == board_cells[0] or board_cells[5] == board_cells[8] or board_cells[4] == board_cells[6]):
                place = 2
            elif board_cells[6] == '6' and (board_cells[0] == board_cells[3] or board_cells[7] == board_cells[8] or board_cells[2] == board_cells[4]):
                place = 6
            elif board_cells[8] == '8' and (board_cells[2] == board_cells[5] or board_cells[6] == board_cells[7] or board_cells[0] == board_cells[4]):
                place = 8
            elif board_cells[1] == '1' and (board_cells[0] == board_cells[2] or board_cells[4] == board_cells[7]):
                place = 1
            elif board_cells[3] == '3' and (board_cells[0] == board_cells[6] or board_cells[4] == board_cells[5]):
                place = 3
            elif board_cells[5] == '5' and (board_cells[2] == board_cells[8] or board_cells[3] == board_cells[4]):
                place = 5
            elif board_cells[7] == '7' and (board_cells[1] == board_cells[4] or board_cells[6] == board_cells[8]):
                place = 7
            else:
                place=random.randint(0,8)
            if board_cells[place]!='X' and board_cells[place]!='O':
                print(turn + " will choose a position to make its move now")
                print(turn, " will place ", c," at position ", place)
                make_move(board_cells, place, c)
                game_board(board_cells)
            else:
                continue
            if iswin(board_cells, turn):
                game_board(board_cells)
                print('Computer won!!')
                status=False
            else:
                if isboardfull(board_cells):
                    game_board(board_cells)
                    print('TIE Game!!')
                    status=False
                    break
                else:
                    turn='Player'
    if not play_again():
        break