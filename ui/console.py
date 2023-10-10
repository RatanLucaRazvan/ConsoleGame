player_starts = 1
computer_starts = 2


class OptionError(Exception):
    pass


class Console:
    def __init__(self, game_service):
        self.__game_service = game_service

    def run_console(self):
        print("Welcome to Obstruction!")
        print("You and the computer will take turns and place an 'X' or '0' on a table of 6X6!")
        print("You aren't allowed to place your symbol in neighbour cells of the cells that were used by the computer!")
        print("The one who can't place his symbol anymore looses!")
        # symbol_of_player = input("Type the symbol you want between 'X' and '0':")
        print()
        print("Who do you want to start?")
        print("[Type 1] Me")
        print("[Type 2] The computer!")
        while True:
            try:
                starting_option = int(input("Choose:"))
                self.is_option_valid(starting_option)
                break
            except ValueError:
                print("You haven't chosen right!")
            except OptionError:
                print("You haven't chosen right!")
        symbol_of_computer = 0
        symbol_of_player = 0
        if starting_option == player_starts:
            symbol_of_computer = '0'
            symbol_of_player = 'X'
        elif starting_option == computer_starts:
            symbol_of_computer = 'X'
            symbol_of_player = '0'
        if starting_option == player_starts:
            self.print_table()
            while True:
                if self.__game_service.check_if_lost() == 1:
                    print("You lost")
                    break
                print("Make your move!")
                while True:
                    try:
                        row = int(input("Type the row you want to place your symbol on:")) - 1
                        column = int(input("Type the column you want to place your symbol on:")) - 1
                        break
                    except ValueError:
                        print("You did not type something right!")

                if self.__game_service.add_move(row, column, symbol_of_player) == 1:
                    if self.__game_service.add_move_for_computer(symbol_of_computer, symbol_of_player) == 0:
                        print("Congratulations, you won!")
                        break
                    self.print_table()
                else:
                    print("You cannot place your symbol there!")
        elif starting_option == computer_starts:
            first_move_done = 0
            row = -1
            column = -1
            while True:
                if self.__game_service.add_move(row, column, symbol_of_player) or (row == -1 and column == -1 and first_move_done == 0):
                    if self.__game_service.add_move_for_computer(symbol_of_computer, symbol_of_player) == 0:
                        print("Congratulations, you won!")
                        break
                    self.print_table()
                elif (row != -1 and column != -1) or first_move_done == 1:
                    print("You cannot place your symbol here!")
                if self.__game_service.check_if_lost() == 1:
                    print("You lost")
                    break
                print("Make your move!")
                while True:
                    try:
                        row = int(input("Type the row you want to place your symbol on:")) - 1
                        column = int(input("Type the column you want to place your symbol on:")) - 1
                        first_move_done = 1
                        break
                    except ValueError:
                        print("You did not type something right!")
                # self.__game_service.add_move(row, column, symbol_of_player)

    def print_table(self):
        table_of_game = self.__game_service.get_table_of_game()
        for index_of_list in range(len(table_of_game)):
            print(*table_of_game[index_of_list], sep=' ')

    def is_option_valid(self, starting_option):
        if starting_option != player_starts and starting_option != computer_starts:
            raise OptionError
