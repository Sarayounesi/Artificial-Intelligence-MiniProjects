from random import choice
import os
# from math import log, sqrt
import math
import copy

player, opponent = 'X', 'O'

# Sara sadat Younesi // HW6 // DR.Mohammadi // 98533053


class TreeNode:
    def __init__(self, board, player, parent=[], action=[]):
        self.board = board
        self.player = player
        self.totalRollouts = 0.00
        self.totalCount = 0.00
        self.parent = parent
        self.action = action
        self.children = None
        self.ucb = -float('inf')

    def findNeighber(self):
        if self.children != None:
            return self.children
        else:
            neighbers = []
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == '_':
                        copyBoard = copy.deepcopy(self.board)
                        copyBoard[i][j] = self.player
                        neighbers.append(
                            TreeNode(copyBoard, opponent if self.player == player else player, self, [i, j]))
            self.children = neighbers
            return self.children

    def calculateUCB(node):

        constant = 4
        if node.totalRollouts == 0:
            return float('inf')
        return (node.totalCount / node.totalRollouts) + constant * math.sqrt(math.log(node.parent.totalRollouts) / node.totalRollouts)

    def isFinalState(self):
        return checkWin(self.board) or not isMovesLeft(self.board)


def _selection_(node):
    if node.isFinalState():
        return node
    if node.totalRollouts == 0:
        return node
    maxScore = -float('inf')
    selected = None
    for child in node.findNeighber():

        score = child.calculateUCB()
        if score > maxScore:
            maxScore = score
            selected = child
    return _selection_(selected)

def _expansion_(node):
    neighbers = node.findNeighber()
    return choice(neighbers)

def _simulation_(node):
    board = copy.deepcopy(node.board)
    P = node.player
    while not checkWin(board) and isMovesLeft(board):
        i, j = findRandom(board)
        board[i][j] = P
        P = opponent if P == player else player
    return calculateScore(board, P)


def _backpropagation_(node, utility):
    node.totalRollouts = 1 + node.totalRollouts
    node.totalCount = utility + node.totalCount
    if node.parent:
        _backpropagation_(node.parent, utility)


def calculateScore(board, turn):
    if checkWin(board):
        if turn == player:
            return 1
        else:
            return -1
    else:
        return 0.75


def findBestMove(board):

    root = TreeNode(board, opponent)
    for i in range(695):
        node = _selection_(root)
        if not node.isFinalState():
            node = _expansion_(node)
        utility = _simulation_(node)
        _backpropagation_(node, utility)
    result = max(root.findNeighber(),
                 key=lambda s: s.totalCount / s.totalRollouts).action
    return result


def findRandom(board):
    empty_spots = [i*3+j for i in range(3)
                   for j in range(3) if board[i][j] == "_"]
    idx = choice(empty_spots)
    return [int(idx/3), idx % 3]


def checkWin(board):
    for row in range(3):
        if (board[row][0] == board[row][1] and board[row][1] == board[row][2] and not board[row][0] == '_'):
            return True
    for col in range(3):
        if (board[0][col] == board[1][col] and board[1][col] == board[2][col] and not board[0][col] == '_'):
            return True

    # main diameter check (col - row = 0)
    if (board[0][0] == board[1][1] and board[1][1] == board[2][2] and not board[0][0] == '_'):
        return True

    # secondary diameter (col + row = 2)
    if (board[0][2] == board[1][1] and board[1][1] == board[2][0] and not board[0][2] == '_'):
        return True

    return False


def isMovesLeft(board):
    return ('_' in board[0] or '_' in board[1] or '_' in board[2])


def printBoard(board):
    os.system('cls||clear')
    print("\n Player : X , Agent: O \n")
    for i in range(3):
        print(" ", end=" ")
        for j in range(3):
            if (board[i][j] == '_'):
                print(f"[{i*3+j+1}]", end=" ")
            else:
                print(f" {board[i][j]} ", end=" ")

        print()
    print()


if __name__ == "__main__":
    board = [
            ['_', '_', '_'],
            ['_', '_', '_'],
            ['_', '_', '_']
    ]

    turn = 0

    while isMovesLeft(board) and not checkWin(board):
        if (turn == 0):
            printBoard(board)
            print(" Select Your Move :", end=" ")
            tmp = int(input())-1
            userMove = [int(tmp/3),  tmp % 3]
            while ((userMove[0] < 0 or userMove[0] > 2) or (userMove[1] < 0 or userMove[1] > 2) or board[userMove[0]][userMove[1]] != "_"):
                print('\n \x1b[0;33;91m' + ' Invalid move ' + '\x1b[0m \n')
                print("Select Your Move :", end=" ")
                tmp = int(input())-1
                userMove = [int(tmp/3),  tmp % 3]
            board[userMove[0]][userMove[1]] = player
            print("Player Move:")
            printBoard(board)
            turn = 1
        else:
            bestMove = findBestMove(board)
            board[bestMove[0]][bestMove[1]] = opponent
            print("Agent Move:")
            printBoard(board)
            turn = 0

    if (checkWin(board)):
        if (turn == 1):
            print('\n \x1b[6;30;42m' + ' Player Wins! ' + '\x1b[0m')

        else:
            print('\n \x1b[6;30;42m' + ' Agent Wins! ' + '\x1b[0m')
    else:
        print('\n \x1b[0;33;96m' + ' Draw! ' + '\x1b[0m')

    input('\n Press Enter to Exit... \n')
