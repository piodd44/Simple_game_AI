from abc import ABC, abstractmethod


class Position(ABC):
    @abstractmethod
    def get_evaluation(self):
        pass

    @abstractmethod
    def create_next_position(self, move):
        pass

    @abstractmethod
    def get_legal_move(self):
        pass

    @abstractmethod
    def get_key(self):
        pass

    @abstractmethod
    def get_player_on_move(self):
        pass


class Game(ABC):
    @abstractmethod
    def make_move(self):
        pass

    @abstractmethod
    def get_position_copy(self):
        pass
