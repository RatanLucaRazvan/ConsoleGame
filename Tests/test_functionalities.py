from unittest import TestCase

from domain.entities import Move
from repository.move_repository import GameRepository
from service.game_service import GameService


class TestFunctionalities(TestCase):
    def test_add_move_for_player(self):
        game_repository = GameRepository()
        game_service = GameService(game_repository)
        game_service.add_move(0, 0, 'X')
        table_of_game = game_repository.find_table_of_game()
        self.assertEqual(table_of_game[0][0], 'X')

        self.assertEqual(game_service.add_move(1, 1, '0'), 0)

        game_service.add_move(4, 4, '0')
        table_of_game = game_repository.find_table_of_game()
        self.assertEqual(table_of_game[4][4], '0')

    def test_add_move_for_computer(self):
        game_repository = GameRepository()
        game_service = GameService(game_repository)
        game_service.add_move_for_computer('0', 'X')
        table_of_game = game_repository.find_table_of_game()
        self.assertEqual(table_of_game[0][0], '0')

    def test_is_element_in_table(self):
        game_repository = GameRepository()
        game_service = GameService(game_repository)
        self.assertEqual(game_service.is_element_in_table(-4, -5), True)
        self.assertEqual(game_service.is_element_in_table(0, 4), False)

    def test_is_element_equal_with_empty(self):
        game_repository = GameRepository()
        game_service = GameService(game_repository)
        table_of_game = game_repository.find_table_of_game()
        self.assertEqual(game_service.is_element_equal_with_empty(table_of_game, 0, 0), True)

        game_service.add_move(0, 0, 'X')
        table_of_game = game_repository.find_table_of_game()
        self.assertEqual(game_service.is_element_equal_with_empty(table_of_game, 0, 0), False)
        self.assertEqual(game_service.is_element_equal_with_empty(table_of_game, 0, 1), False)

    def test_get_element_of_table(self):
        game_repository = GameRepository()
        game_service = GameService(game_repository)
        table_of_game = game_service.get_table_of_game()
        table_for_verifying = [['-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-'],
                              ['-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-'],
                              ['-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-']]
        self.assertEqual(table_of_game, table_for_verifying)

        game_service.add_move(0, 0, 'X')
        table_of_game = game_service.get_table_of_game()
        # print(table_of_game)
        table_for_verifying = [['X', '$', '-', '-', '-', '-'], ['$', '$', '-', '-', '-', '-'],
                              ['-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-'],
                              ['-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-']]
        self.assertEqual(table_of_game, table_for_verifying)

    def test_save_table_of_game(self):
        game_repository = GameRepository()
        game_service = GameService(game_repository)

        game_service.add_move(4, 4, 'X')
        game_repository.save_table_of_game()
        game_service.add_move(0, 0, 'X')
        game_repository.restore_previous_table_of_game(Move(0, 0 ,'X'))
        table_of_game = game_repository.find_table_of_game()
        table_for_verifying = [['-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-'],
                              ['-', '-', '-', '-', '-', '-'], ['-', '-', '-', '$', '$', '$'],
                              ['-', '-', '-', '$', 'X', '$'], ['-', '-', '-', '$', '$', '$']]
        self.assertEqual(table_of_game, table_for_verifying)

    def test_find_by_key(self):
        game_repository = GameRepository()
        game_service = GameService(game_repository)
        game_service.add_move(0, 0, 'X')
        move = game_repository.find_move_by_key('00')
        self.assertEqual(move.get_row_of_move(), '0')
        self.assertEqual(move.get_column_of_move(), '0')
        self.assertEqual(move.get_symbol_of_move(), 'X')

    def test_check_if_player_can_win(self):
        game_repository = GameRepository()
        game_service = GameService(game_repository)

        game_service.add_move(0, 0, 'X')
        game_service.add_move(0, 3, '0')
        game_service.add_move(0, 5, 'X')
        game_service.add_move(2, 1, '0')
        game_service.add_move(2, 4, 'X')
        game_service.add_move(4, 1, '0')

        self.assertEqual(game_service.check_if_player_can_win('X'), 1)

    def test_check_if_lost(self):
        game_repository = GameRepository()
        game_service = GameService(game_repository)

        game_service.add_move(0, 0, 'X')
        game_service.add_move(0, 3, '0')
        game_service.add_move(0, 5, 'X')
        game_service.add_move(2, 1, '0')
        game_service.add_move(2, 4, 'X')
        game_service.add_move(4, 1, '0')
        game_service.add_move(4, 4, '0')

        self.assertEqual(game_service.check_if_lost(), 1)



