import random
import time

class bcolors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    ENDC = '\033[0m'


def init_board():
    """Returns an empty 3-by-3 board (with .)."""
    board = {'a1': ' . ' , 'a2': ' . ' , 'a3': ' . ' ,
            'b1': ' . ' , 'b2': ' . ' , 'b3': ' . ' ,
            'c1': ' . ' , 'c2': ' . ' , 'c3': ' . ' }
    return board
    board_keys = []

    for key in theBoard:
        board_keys.append(key)



def get_move(board, player):

    player = 'X'
    steps = 0

    for i in range(10):
        possible_steps = ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3', 'quit']
        print_board(board)
        print("")
        move = input("   It's your turn " + player + ": ")
        if move in possible_steps:

            if move == 'quit':
                break
            else:
                if board[move] == ' . ':
                    board[move] = ' ' + player + ' '
                    steps += 1
                    print('\033c')           
                else:
                    print('\033c')
                    print("   That place is already filled.")
                    continue
        else:
                    print('\033c') 
                    print ("   Invalid input. Try again!")
                    continue
        
        if steps >=5:

            if board['a1'] == board ['a2'] == board ['a3'] != " . ":
                print('\033c')
                print_board(board)
                print("")
                print("   Congratulation! Player: "+ player+ " Won the game!" )
                break
                
            elif board['b1'] == board ['b2'] == board ['b3'] != " . ":
                print('\033c')
                print_board(board)
                print("")
                print("   Congratulation! Player: "+ player+ " Won the game!" )
                break
                        
            elif board['c1'] == board ['c2'] == board ['c3'] != " . ":
                print('\033c')
                print_board(board)
                print("")
                print("   Congratulation! Player: "+ player+ " Won the game!" )
                break
                        
            elif board['a1'] == board ['b1'] == board ['c1'] != " . ":
                print('\033c')
                print_board(board)
                print("")
                print("   Congratulation! Player: "+ player+ " Won the game!" )
                break
                        
            elif board['a2'] == board ['b2'] == board ['c2'] != " . ":
                print('\033c')
                print_board(board)
                print("")
                print("   Congratulation! Player: "+ player+ " Won the game!" )
                break
                        
            elif board['a3'] == board ['b3'] == board ['c3'] != " . ":
                print('\033c')
                print_board(board)
                print("")
                print("   Congratulation! Player: "+ player+ " Won the game!" )
                break
                    
            elif board['a1'] == board ['b2'] == board ['c3'] != " . ":
                print('\033c')
                print_board(board)
                print("")
                print("   Congratulation! Player: "+ player+ " Won the game!" )
                break
                    
            elif board['a3'] == board ['b2'] == board ['c1'] != " . ":
                print('\033c')
                print_board(board)
                print("")
                print("   Congratulation! Player: "+ player+ " Won the game!" )
                break
        if steps >= 9:
            is_full(board)
    
        if player == 'X':
            player = 'O'
        else:
            player = 'X'  
    

def get_ai_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    row, col = 0, 0
    return row, col
    pass



def is_full(board):
    """Returns True if board is full."""
    print("    Its a tie.")
    play_again()


def print_board(board):
    print("")
    print("   " + "   1   2   3")
    print("   " + "A " + board['a1'] + f"{bcolors.RED}|{bcolors.ENDC}" + board['a2'] + f"{bcolors.RED}|{bcolors.ENDC}" + board['a3'])
    print("   " + "  " + f"{bcolors.RED}---+---+---{bcolors.ENDC}")
    print("   " + "B " + board['b1'] + f"{bcolors.RED}|{bcolors.ENDC}" + board['b2'] + f"{bcolors.RED}|{bcolors.ENDC}" + board['b3'])
    print("   " + "  " + f"{bcolors.RED}---+---+---{bcolors.ENDC}")
    print("   " + "C " + board['c1'] + f"{bcolors.RED}|{bcolors.ENDC}" + board['c2'] + f"{bcolors.RED}|{bcolors.ENDC}" + board['c3'])
    print("")
    


def play_again():
    board = init_board()
    rematch = input("   Do you want to play again? (y) or (n) ")
    print("")
    while True:
        if rematch == 'y':
            game_mode()
        else:
            print('\033c')
            print(f"{bcolors.GREEN}                     _____   _                    _                              __              ")
            time.sleep(0.2)
            print("                    |_   _| | |_    __ _   _ _   | |__    _  _   ___   _  _     / _|  ___   _ _  ")
            time.sleep(0.2)
            print("                      | |   | ' \  / _` | | ' \  | / /   | || | / _ \ | || |   |  _| / _ \ | '_| ")
            time.sleep(0.2)
            print("                      |_|   |_||_| \__,_| |_||_| |_\_\    \_, | \___/  \_,_|   |_|   \___/ |_|  ")
            time.sleep(0.2)
            print("                                                          |__/                                  ")
            time.sleep(0.2)
            print("                                        _                 _                 _                   ")
            time.sleep(0.2)
            print("                                 _ __  | |  __ _   _  _  (_)  _ _    __ _  | |                 ")
            time.sleep(0.2)
            print("                                | '_ \ | | / _` | | || | | | | ' \  / _` | |_|                ")
            time.sleep(0.2)
            print("                                | .__/ |_| \__,_|  \_, | |_| |_||_| \__, | (_)                ")
            time.sleep(0.2)
            print(f"                                |_|                |__/             |___/                     {bcolors.ENDC}")
            time.sleep(3)
            print('\033c')
            break

    
def tictactoe_game(mode='HUMAN-HUMAN'):
    board = init_board()
    get_move(board, 1)
    # use get_move(), mark(), has_won(), is_full(), and print_board() to create game logic
    play_again()





def main_menu():

    print(f"{bcolors.RED}                                  _   _                           ")
    time.sleep(0.2)
    print("                  __ __ __  ___  | | | |  __   ___   _ __    ___  ")
    time.sleep(0.2)
    print("                  \ V  V / / -_) | | | | / _| / _ \ | '  \  / -_) ")
    time.sleep(0.2)
    print(f"                   \_/\_/  \___| |_| |_| \__| \___/ |_|_|_| \___| {bcolors.ENDC}") 
    time.sleep(0.2)
    print("                                    _____                         ")
    time.sleep(0.2)
    print("                                   |_   _|  ___                   ")
    time.sleep(0.2)
    print("                                     | |   / _ \                  ")
    time.sleep(0.2)
    print("                                     |_|   \___/                  ")
    time.sleep(0.2)
    print(f"{bcolors.GREEN}              _____   _        _____               _____            ")
    time.sleep(0.2)
    print("             |_   _| (_)  __  |_   _|  __ _   __  |_   _|  ___   ___  ")
    time.sleep(0.2)
    print("               | |   | | / _|   | |   / _` | / _|   | |   / _ \ / -_) ")
    time.sleep(0.2)
    print(f"               |_|   |_| \__|   |_|   \__,_| \__|   |_|   \___/ \___| {bcolors.ENDC}")

    time.sleep(2)
    print('\033c')

    print("           __  __           _             __  __                         ")
    time.sleep(0.2)
    print("          |  \/  |         (_)           |  \/  |                        ")
    time.sleep(0.2)
    print("          | \  / |   __ _   _   _ __     | \  / |   ___   _ __    _   _  ")
    time.sleep(0.2)
    print("          | |\/| |  / _` | | | | '_ \    | |\/| |  / _ \ | '_ \  | | | | ")
    time.sleep(0.2)
    print("          | |  | | | (_| | | | | | | |   | |  | | |  __/ | | | | | |_| | ")
    time.sleep(0.2)
    print("          |_|  |_|  \__,_| |_| |_| |_|   |_|  |_|  \___| |_| |_|  \__,_| ", "\n")
                                                                
    time.sleep(0.3)
    game_mode()

def game_mode():
    while True:
        print("                    =======================================")
        time.sleep(0.2)
        print("")
        print("                          Do you want to play against")
        time.sleep(0.2)
        print("                        a Player (p) or a Computer (c)?")
        time.sleep(0.2)
        print("                            or type (q) for quit.")
        print("")
        time.sleep(0.2)
        print("                    =======================================")
        print("")

        mode = input("                              Choose wisely: ")
        mode = str(mode)
        if mode == 'p':
            print("         You are playing against a player")
            print('\033c')
            tictactoe_game()
            break
        elif mode == 'c':
            print("         You are playing against a computer")
            break
            print('\033c')
        elif mode == 'q':
            print('\033c')
            print(f"{bcolors.GREEN}                      _____   _                    _                              __              ")
            time.sleep(0.2)
            print("                    |_   _| | |_    __ _   _ _   | |__    _  _   ___   _  _     / _|  ___   _ _  ")
            time.sleep(0.2)
            print("                      | |   | ' \  / _` | | ' \  | / /   | || | / _ \ | || |   |  _| / _ \ | '_| ")
            time.sleep(0.2)
            print("                      |_|   |_||_| \__,_| |_||_| |_\_\    \_, | \___/  \_,_|   |_|   \___/ |_|  ")
            time.sleep(0.2)
            print("                                                          |__/                                  ")
            time.sleep(0.2)
            print("                                        _                 _                 _                   ")
            time.sleep(0.2)
            print("                                 _ __  | |  __ _   _  _  (_)  _ _    __ _  | |                 ")
            time.sleep(0.2)
            print("                                | '_ \ | | / _` | | || | | | | ' \  / _` | |_|                ")
            time.sleep(0.2)
            print("                                | .__/ |_| \__,_|  \_, | |_| |_||_| \__, | (_)                ")
            time.sleep(0.2)
            print(f"                                |_|                |__/             |___/                     {bcolors.ENDC}")
            time.sleep(3)
            print("")
            break
        else:
            print('\033c')
            print("                     Please choose from (p) or (c) or (q)!")




main_menu()