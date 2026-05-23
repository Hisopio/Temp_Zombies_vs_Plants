from __future__ import annotations
from collections.abc import Sequence

class Model:
    def __init__(self):
        self._player_position: Sequence[int] = [50,50]
        self._is_game_over: bool = False

        self._current_tick = 1

    @property
    def player_position(self) -> Sequence[int]:
        return self._player_position
    
    def update_player_position(self, new_position: Sequence[int]) -> None:
        self._player_position = new_position

    @property
    def is_game_over(self) -> bool:
        return self._is_game_over

    @classmethod
    def get_simple_model(cls):
        return cls()