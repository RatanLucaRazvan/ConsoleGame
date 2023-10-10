import copy


class GameRepository:
    def __init__(self):
        self.__all_moves = {}
        self.__game_table = [['-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-'],
                             ['-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-'],
                             ['-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-']]
        self.__copy_game_table = [['-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-'],
                             ['-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-'],
                             ['-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-']]

    def is_element_in_game_table(self, row, column):
        return 0 <= row < 6 and 0 <= column < 6

    def is_element_equal_with_empty(self, row, column):
        return self.__game_table[row][column] != '-'

    def save_move(self, move):
        row = int(move.get_row_of_move())
        column = int(move.get_column_of_move())
        if self.find_move_by_key(move.get_row_of_move() + move.get_column_of_move()) is not None:
            raise ValueError("Duplicate move!")
        self.__all_moves[move.get_row_of_move() + move.get_column_of_move()] = move
        self.__game_table[row][column] = move.get_symbol_of_move()
        if self.is_element_in_game_table(row + 1, column):
            self.__game_table[row + 1][column] = '$'
        if self.is_element_in_game_table(row + 1, column + 1):
            self.__game_table[row + 1][column + 1] = '$'
        if self.is_element_in_game_table(row - 1, column):
            self.__game_table[row - 1][column] = '$'
        if self.is_element_in_game_table(row + 1, column - 1):
            self.__game_table[row + 1][column - 1] = '$'
        if self.is_element_in_game_table(row - 1, column - 1):
            self.__game_table[row - 1][column - 1] = '$'
        if self.is_element_in_game_table(row, column + 1):
            self.__game_table[row][column + 1] = '$'
        if self.is_element_in_game_table(row, column - 1):
            self.__game_table[row][column - 1] = '$'
        if self.is_element_in_game_table(row - 1, column + 1):
            self.__game_table[row - 1][column + 1] = '$'

    def find_move_by_key(self, key_of_move):
        if key_of_move in self.__all_moves:
            return self.__all_moves[key_of_move]
        return None

    def find_table_of_game(self):
        return self.__game_table
    def save_table_of_game(self):
        self.__copy_game_table.append(copy.deepcopy(self.__game_table))

    def restore_previous_table_of_game(self, last_move):
        self.__game_table.clear()
        self.__game_table.extend(copy.deepcopy(self.__copy_game_table[-1]))
        self.__copy_game_table.pop()
        del self.__all_moves[last_move.get_row_of_move() + last_move.get_column_of_move()]
    # def find_twin_table_of_game(self):
    #     return self.__twin_game_table


class ComputerRepository:
    pass
