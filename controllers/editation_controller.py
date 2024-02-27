# editation_controller.py
from models.database_manager import DatabaseManager
from controllers.view_controller import ViewController

class EditationController:
    def __init__(self, model: DatabaseManager, view: ViewController) -> None:
        self.model = model
        self.view = view