from ai import AI
from game import Game, Position


class TwoStackPosition(Position):
    def get_evaluation(self):
        return self.evaluate

    def get_legal_move(self):
        return self.legal_move

    def get_key(self):
        return self.key

    def get_player_on_move(self):
        return self.last_player

    def __init__(self, left, right, last_move, last_player):
        self.cur_left = left
        self.cur_right = right
        self.last_move = last_move
        self.last_player = last_player
        l, r = last_move
        self.cur_left -= l
        self.cur_right -= r
        self.key = self.give_key()
        self.evaluate = self.evaluate_position()
        self.legal_move = self.legal_move()

    def give_key(self):
        if self.last_player == 1:
            key = 1000 * self.cur_left + 10 * self.cur_right + 1
        else:
            key = 1000 * self.cur_left + 10 * self.cur_right + 2
        return key

    def evaluate_position(self):
        if self.cur_right + self.cur_left == 0:
            # print("self.last_player", self.last_player, self.cur_left, self.cur_right)
            return self.last_player * (-1)
        else:
            return 0

    def create_next_position(self, move):
        next_position = TwoStackPosition(left=self.cur_left, right=self.cur_right, last_move=move,
                                         last_player=self.last_player * (-1))
        return next_position

    def legal_move(self):
        moves = []
        for l in range(self.cur_left):
            moves.append((l + 1, 0))
        for r in range(self.cur_right):
            moves.append((0, r + 1))
        return moves

    def show(self):
        print(self.cur_left, self.cur_right)


class TwoStack(Game):
    def get_position_copy(self):
        return self.position

    def __init__(self, left, right):
        self.player_on_move = 1
        self.start_left = left
        self.start_right = right
        self.cur_left = left
        self.cur_right = right
        self.position = TwoStackPosition(self.start_left, self.start_right, last_move=(0, 0),
                                         last_player=self.player_on_move)

    def legal_move(self):
        moves = []
        for l in range(self.cur_left):
            moves.append((l + 1, 0))
        for r in range(self.cur_right):
            moves.append((0, r + 1))
        return moves

    def make_move(self, move):
        l, r = move
        self.position = self.position.create_next_position(move)
        self.cur_left = self.position.cur_left
        self.cur_right = self.position.cur_right
        self.player_on_move = self.position.last_player

    def show(self):
        print(self.cur_left, self.cur_right)

    def game_loop(self):
        print(self.position.evaluate)
        while self.position.evaluate == 0:
            self.show()
            raw_move = input("wpisz ruch")
            l, r = raw_move.split(",")
            move = (int(l), int(r))
            self.make_move(move)
        print("wygrał", self.position.evaluate)

    def game_loop_ai(self, ai_1, ai_2):
        while self.position.evaluate == 0:
            print("na ruchu jest gracz nr == ", self.player_on_move)
            print("na pozycji ,")
            self.show()
            if self.player_on_move == 1:
                move = ai_1.make_move(self.position)
            else:
                move = ai_2.make_move(self.position)
            self.make_move(move)
        self.show()
        print("wygrał ", self.position.evaluate)


def test_legal_move():
    two_stack = TwoStack(left=7, right=10)
    print(two_stack.legal_move())


def test_game_loop():
    two_stack = TwoStack(left=5, right=10)
    two_stack.game_loop()


def test_ai():
    two_stack = TwoStack(left=5, right=10)
    ai_1 = AI(two_stack, player=1)  # dziwny bug nie wiem czemu to tak działa XD
    ai_2 = AI(two_stack, player=-1)
    two_stack.game_loop_ai(ai_1, ai_2)


# test_legal_move()
# test_game_loop()
test_ai()
