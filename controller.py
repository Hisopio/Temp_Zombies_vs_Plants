from model import Model
from view import View


class Controller:
    def __init__(self, model: Model, view: View):
        self._model = model
        self._view = view

    def start_game(self):
        self._view.start_game(self, self)

    def update(self):
        self._model.update_player_position(self._view.get_player_movement(self._model.player_position))

    def draw(self):
        self._view.reset_screen()
        self._view.draw_player(self._model.player_position)



"""
Player input:
Game start
	LeaderBoard -> Game start
	Settings -> Game start
		Player HP
		Enemies per round
		Music on/off
	2 Gameplay Types:
		Campaign 
		Endless
	Start Game

Game Loop:
	Pre-round 
		Tower placing
Round	
If not round_over:
		Movement
		Shooting
Next Round

If Game Over -> Game Start
"""