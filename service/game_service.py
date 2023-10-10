from domain.entities import Move


class GameService:
    def __init__(self, game_repository):
        self.__game_repository = game_repository

    def add_move(self, row, column, symbol_of_player):
        table_of_game = self.__game_repository.find_table_of_game()
        move = Move(row, column, symbol_of_player)
        try:
            if self.is_element_equal_with_empty(table_of_game, row, column) and self.is_element_in_table(row, column) == 0:
                self.__game_repository.save_move(move)
                return 1
            else:
                raise ValueError
        except ValueError:
            # print("You cannot place your symbol here!")
            return 0

    def get_table_of_game(self):
        return self.__game_repository.find_table_of_game()

    def is_element_in_table(self, row, column):
        return row < 0 or row > 6 or column < 0 or column > 6

    def is_element_equal_with_empty(self, table_of_game, row, column):
        if 0 <= row < 6 and 0 <= column < 6:
            return table_of_game[row][column] == '-'
        return 1

    def add_move_for_computer(self, symbol_of_computer, symbol_of_player):
        move_backup = 0
        table_of_game = self.__game_repository.find_table_of_game()
        for row in range(6):
            for column in range(6):
                if self.is_element_equal_with_empty(table_of_game, row, column):
                    move_for_computer = Move(row, column, symbol_of_computer)
                    if move_backup == 0:
                        move_backup = Move(row, column, symbol_of_computer)
                    self.__game_repository.save_table_of_game()
                    self.__game_repository.save_move(move_for_computer)
                    if self.check_if_lost() == 1:
                        return
                    elif self.check_if_player_can_win(symbol_of_player) == 0:
                        return
                    else:
                        self.__game_repository.restore_previous_table_of_game(move_for_computer)
        if move_backup != 0:
            self.__game_repository.save_move(move_backup)
        else:
            return 0
            # print("Congratulations, you won!")
            # quit()

    def check_if_lost(self):
        table_of_game = self.__game_repository.find_table_of_game()
        for row in range(6):
            for column in range(6):
                if table_of_game[row][column] == '-':
                    return 0
        return 1

    def check_if_player_can_win(self, symbol_of_player):
        table_of_game = self.__game_repository.find_table_of_game()
        for row in range(6):
            for column in range(6):
                if self.is_element_equal_with_empty(table_of_game, row, column):
                    move_for_player = Move(row, column, symbol_of_player)
                    self.__game_repository.save_table_of_game()
                    self.__game_repository.save_move(move_for_player)
                    if self.check_if_lost() == 1:
                        self.__game_repository.restore_previous_table_of_game(move_for_player)
                        return 1
                    else:
                        self.__game_repository.restore_previous_table_of_game(move_for_player)
        return 0


class ComputerService:
    pass
