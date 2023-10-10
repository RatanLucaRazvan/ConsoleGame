class Move:
    def __init__(self, row, column, symbol):
        self.__row = row
        self.__column = column
        self.__symbol = symbol

    def get_row_of_move(self):
        return str(self.__row)

    def get_column_of_move(self):
        return str(self.__column)
    def get_symbol_of_move(self):
        return self.__symbol
