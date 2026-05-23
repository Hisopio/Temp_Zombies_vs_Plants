from collections.abc import Sequence
from typing import Protocol

import pyxel


class UpdateHandler(Protocol):
    def update(self):
        ...

 
class DrawHandler(Protocol):
    def draw(self):
        ...


# Controller <: UpdateHandler
# Controller <: DrawHandler


class View:
    def __init__ (self, width: int, height: int):
        self._width = width
        self._height = height
        self._size = 5
        self._origin = (self._width//2, self._height//2)

    def start_game(self, update_handler: UpdateHandler, draw_handler: DrawHandler) -> None:
        pyxel.init(self._width, self._height)
        pyxel.run(update_handler.update, draw_handler.draw)

            
    def get_player_movement(self, position: Sequence[int]) -> Sequence[int]:
        if pyxel.btnp(pyxel.KEY_W, 5, 5):
            position = [position[0], position[1] - 5]
        
        if pyxel.btnp(pyxel.KEY_A, 5, 5):
            position = [position[0] - 5, position[1]]
            
        if pyxel.btnp(pyxel.KEY_S, 5, 5):
            position = [position[0], position[1] + 5]
        
        if pyxel.btnp(pyxel.KEY_D, 5, 5):
            position = [position[0] + 5, position[1]]
        
        return position
    
    def draw_player(self, position: Sequence[int]) -> None:
        pyxel.circ(position[0], position[1], 5, 2)
    
    def reset_screen(self) -> None:
        pyxel.mouse(True)
        pyxel.cls(11)
        pyxel.bltm(0,0,0,0,0,300,300)
    
    def game_over(self):
        pyxel.mouse(False)
        pyxel.rect(self._origin[0] - 50, self._origin[1] - 35,100,70, 0)
        pyxel.rect(self._origin[0] - 45, self._origin[1] - 30,90,60, 8)
        pyxel.text(self._origin[0] - 20, self._origin[1], "Game Over", 0)