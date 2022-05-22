import copy
from game import Position, Game

x_import = 1
if x_import == 1:
    print(x_import)
    from ai import AI

    x_import += 1
import copy


class TicTacPosition(Position):

    def get_player_on_move(self):
        return self.last_player * (-1)

    def get_evaluation(self):
        return self.evaluate

    def get_legal_move(self):
        return self.legal_move

    def get_key(self):
        return self.key

    def __init__(self, board, last_move, last_player, last_key=0):
        self.end_state = False
        self.last_player = last_player
        self.board = copy.deepcopy(board)
        if last_move is None:
            self.last_move = None
            self.key = 0
            self.evaluate = 0
        else:
            x, y = last_move
            if self.last_player == 1:
                self.board[x][y] = 1
            else:
                self.board[x][y] = -1
            self.last_move = last_move
            self.key = self.give_key(last_key)
            self.evaluate = self.evaluate_position()
        self.legal_move = self.create_legal_move()
        if len(self.legal_move) == 0:
            self.end_state = True

    def give_key(self, last_key):
        key = last_key
        x, y = self.last_move
        if self.last_player == 1:
            m = 1
        else:
            m = 2
        key += m * (3 ** (3 * y + x))
        return key

    def evaluate_position(self):
        last_x, last_y = self.last_move
        col = self.board[last_x][0] + self.board[last_x][1] + self.board[last_x][2]
        line = self.board[0][last_y] + self.board[1][last_y] + self.board[2][last_y]
        # print("col ==", col, "ostatni ruch to ", self.last_move)
        # print("line ==", line)
        if col == 3 or line == 3:
            return 1
        if col == -3 or line == -3:
            return -1
        diagonal_1 = self.board[0][0] + self.board[1][1] + self.board[2][2]
        diagonal_2 = self.board[2][0] + self.board[1][1] + self.board[0][2]
        if diagonal_1 == 3 or diagonal_2 == 3:
            return 1
        if diagonal_1 == -3 or diagonal_2 == -3:
            return -1
        return 0

    def create_next_position(self, move):
        next_position = TicTacPosition(self.board, last_move=move, last_player=self.last_player * (-1),
                                       last_key=self.key)
        return next_position

    def create_legal_move(self):
        moves = []
        if self.evaluate != 0:
            return moves
        for x in range(len(self.board)):
            for y in range(len(self.board[x])):
                if self.board[x][y] == 0:
                    moves.append((x, y))
        return moves

    def show(self):
        for line in self.board:
            print()
            for box in line:
                print("|", box, "|", end="")
        print()


class TicTacToe:
    def __init__(self):
        self.board = [[0 for x in range(3)] for y in range(3)]
        self.position = TicTacPosition(board=self.board, last_move=None, last_player=-1)
        self.player_on_move = 1

    def show(self):
        for line in self.board:
            print()
            for box in line:
                print("|", box, "|", end="")
        print()

    def legal_move(self):
        moves = []
        for x in range(len(self.board)):
            for y in range(len(self.board[x])):
                if self.board[x][y] == 0:
                    moves.append((x, y))
        return moves

    def evaluate_position(self):
        if self.position is None:
            return 0
        return self.position.evaluate

    def make_move(self, move):
        x, y = move
        self.update_position(move)
        if move in self.legal_move():
            if self.player_on_move == 1:
                self.board[x][y] = 1
            else:
                self.board[x][y] = -1
            self.player_on_move *= -1

    def update_position(self, move):
        if self.position is None:
            self.position = TicTacPosition(board=self.board, last_move=move, last_player=self.player_on_move)
        else:
            self.position = TicTacPosition(board=self.board, last_move=move, last_player=self.player_on_move,
                                           last_key=self.position.key)

    def game_loop(self):
        legals_moves = self.legal_move()
        while len(legals_moves) > 0 and self.evaluate_position() == 0:
            self.show()
            print(legals_moves)
            raw_move = input("wybierz ruch")
            x, y = raw_move.split(",")
            move = (int(x), int(y))
            print(move)
            self.make_move(move)
            legals_moves = self.legal_move()
            print("evaluation ==", self.evaluate_position())
        print("wygrał", self.evaluate_position())

    def game_loop_ai(self, ai_1: AI, ai_2: AI):
        legals_moves = self.legal_move()
        print(self.position.evaluate)
        while len(legals_moves) > 0 and self.evaluate_position() == 0:
            print("na ruchu jest gracz nr == ", self.player_on_move)
            self.show()
            if self.player_on_move == 1:
                move = ai_1.make_move(self.position)
            else:
                move = ai_2.make_move(self.position)
            self.make_move(move)
            legals_moves = self.legal_move()
        self.show()
        print("wygrał ", self.evaluate_position())

    def game_loop_ai_vs_human(self, ai_1: AI):
        legals_moves = self.legal_move()
        while len(legals_moves) > 0 and self.evaluate_position() == 0:
            print("na ruchu jest gracz nr == ", self.player_on_move)
            self.show()
            if self.player_on_move == 1:
                move = ai_1.make_move(self.position)
            else:
                raw_move = input("wybierz ruch")
                x, y = raw_move.split(",")
                move = (int(x), int(y))
                print(move)
            self.make_move(move)
            legals_moves = self.legal_move()
            print("evaluation ==", self.evaluate_position())
        self.show()
        print("wygrał ", self.evaluate_position())


def test():
    tic_tac_toe = TicTacToe()
    tic_tac_toe.show()
    legal_moves = tic_tac_toe.legal_move()
    print(legal_moves)
    evaluation = tic_tac_toe.evaluate_position()
    print("evaluation" == evaluation)
    for x in range(9):
        legal_moves = tic_tac_toe.legal_move()
        tic_tac_toe.make_move(legal_moves[0])
        tic_tac_toe.show()
        print(tic_tac_toe.evaluate_position())


def test_2():
    tic_tac_toe = TicTacToe()
    tic_tac_toe.game_loop()


def test_ai():
    tic_tac_toe = TicTacToe()
    ai_1 = AI(tic_tac_toe, player=1)
    ai_2 = AI(tic_tac_toe, player=-1)
    tic_tac_toe.game_loop_ai(ai_1, ai_2)
    # ai_1.make_move(tic_tac_toe.position)


def test_ai_vs_human():
    tic_tac_toe = TicTacToe()
    ai_1 = AI(tic_tac_toe, player=1)
    tic_tac_toe.game_loop_ai_vs_human(ai_1)


test_ai()
# test_2()
