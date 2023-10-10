from repository.move_repository import GameRepository
from service.game_service import GameService
from ui.console import Console

if __name__ == '__main__':
    game_repository = GameRepository()
    game_service = GameService(game_repository)
    console = Console(game_service)
    console.run_console()