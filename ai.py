import copy
from tree import Tree, BinaryTree, GameTree, GameNode
import numpy as np
from game import Game, Position


# proste AI oparte na algorytmie MinMax . Można "podpiąć" pod niego dowolną gre kombinatoryczną o ile ma
# Ważne żeby miała pole position i metode pozwalającą tworzyć kolejne pozycje wraz z oceną czy jest to stan końcowy
# i jeśli koniec to dająca odpowiedz kto wygrał
class AI:
    def __init__(self, game, player=1):
        self.player = player
        self.end_states = []
        self.cur_position = copy.deepcopy(game.position)
        self.binary_tree = BinaryTree()
        # binary_tree sprawdza czy nie ma kopi pozycji i przechowuje referencje do danej pozycji w drzewie gry
        self.game_tree = GameTree(key=self.cur_position.key, value=self.cur_position)
        self.binary_tree.add(key=self.cur_position.key, value=self.game_tree.root, start_node=self.binary_tree.root)
        self.build_game_tree(start_position=self.cur_position)
        # przypisujemy wartości w drzewie
        print("liczba wierzchołków w drzewie gry == ", len(self.game_tree.all_nodes))
        print("drzewo się zbudowało")
        for node in self.game_tree.all_nodes:
            if type(node) != type(self.game_tree.root):
                print("wtf")
                exit()
        self.min_max(start_node=self.game_tree.root)
        print(len(self.end_states))

    def make_move(self, position):
        moves = position.legal_move
        node_in_game_tree = self.binary_tree.find_in_tree(key=position.key, start_node=self.binary_tree.root).value
        child_list = node_in_game_tree.child_list
        pos_list = [child.value for child in child_list]
        choose_pos = self.find_the_best_position(pos_list)
        for move in moves:
            next_position = position.create_next_position(move)
            if next_position.key == choose_pos.key:
                return move
        return moves[0]

    def find_the_best_position(self, position_list):
        for pos in position_list:
            if pos.evaluate == self.player:
                choose = pos
                return choose
        for pos in position_list:
            if pos.evaluate == 0:
                choose = pos
                return choose
        return position_list[0]

    def min_max(self, start_node):
        if len(start_node.child_list) == 0:
            return start_node.value.get_evaluation()
        else:
            values = []
            for child in start_node.child_list:
                values.append(self.min_max(child))
            if start_node.value.get_player_on_move() == 1:
                evaluation = max(values)
            else:
                evaluation = min(values)
            start_node.value.evaluate = evaluation
            return evaluation

    def build_game_tree(self, start_position: Position):
        game_tree_node = self.binary_tree.find_in_tree(key=start_position.get_key(),
                                                       start_node=self.binary_tree.root).value
        game_tree_position = game_tree_node.value
        moves = game_tree_position.get_legal_move()
        positions = []
        new_position = []
        for move in moves:
            positions.append(game_tree_position.create_next_position(move))
        for position in positions:
            if self.binary_tree.in_tree(key=position.get_key(), start_node=self.binary_tree.root):
                game_node = self.binary_tree.find_in_tree(key=position.get_key(),
                                                          start_node=self.binary_tree.root).value
                game_tree_node.add_child(game_node)
            else:
                game_node = self.game_tree.add(key=position.get_key, value=position, start_node=game_tree_node)
                self.binary_tree.add(key=position.get_key(), value=game_node, start_node=self.binary_tree.root)
                new_position.append(position)
        for position in new_position:
            self.build_game_tree(position)
