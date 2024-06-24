def main(board,player,turn):
        while 1:
            try:
                col = int(input("Enter column (1, 2, 3): "))-1
                row = int(input("Enter row (1, 2, 3): "))-1
                
                if row == -1 or col == -1:
                    int('')

                if board[row][col] == '-':
                    board[row][col] = player[turn]
                    for i in board:
                        print(" ".join(i)) 

                else:
                    print('enter a valid row and colum')
                    print_board(board)
                try:
                    if full(board):
                        print("Draw!!!!")
                        break

                    elif win(board):
                        print(f"Player: {player[turn]} has won :)")
                        break

                except:
                    print(f"Player: {player[turn]} has won :)")

                if turn == 1:
                    turn = 0
                else:
                    turn = 1

            except IndexError:
                print('Please Enter A Valid Row/Column :)')
                print_board(board)
            except ValueError:
                print("Please Enter numb3r")
                print_board(board)

        if play_again():
            board = [['-','-','-'],['-','-','-'],['-','-','-']]
            player = ["X","O"]
            turn=0
            print('Game On!')
            print_board(board)
            main(board,player,turn)
def full(board):
    for i in board:
        if "-" in i:
            return 0
    return 1
def print_board(board):
    for i in board:
        print(" ".join(i))
def play_again():
        try:
            time.sleep(1)
            print()
            print('Do you want to lose...')
            time.sleep(2)
            print('...')
            time.sleep(1)
            for i in range(20):
                print()

            p = str(input('Do you want to play*** Again (Y/N)?: '))

            if p.lower() == 'y':
                return 1
            return 0
        except:
            print('gg')
            pass
def win(board):
    #sh+
    for row in board:#row
        if all(cell == row[0] and cell != '-' for cell in row):
            return True
    for col in range(3):#column
        if all(board[row][col] == board[0][col] and board[row][col] != '-' for row in range(3)):
            return True
    if (board[0][0] == board[1][1] == board[2][2] != '-') or (board[0][2] == board[1][1] == board[2][0] != '-'):#diagnal
        return True

    return False

if __name__ == '__main__':
    import time
    board = [['-','-','-'],
             ['-','-','-'],
             ['-','-','-']]
    player = ["X","O"]
    turn = 0
    print_board(board)
    main(board,player,turn)
