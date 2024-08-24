from collections import Counter
from random import randrange


class NQueens:

    def __init__(self, N):
        self.N = N

    def initial(self):
        # Returns a random initial state
        return tuple(randrange(self.N) for i in range(self.N))

    def goal_test(self, state):
        # Returns True if the given state is a goal state
        n = set()
        minus = set()
        add = set()
        for i, j in enumerate(state):
            if j in n:
                return False
            if i - j in minus:
                return False
            if i + j in add:
                return False

            n.add(j)
            minus.add(i - j)
            add.add(i + j)
        return True

    def value(self, state):
        # Returns the value of a state. The higher the value, the closest to a goal state
        # to calculate number of item are attacking queen
        n, minus, add = Counter(), Counter(), Counter()
        for i, j in enumerate(state):
            n[j] += 1
            minus[i - j] += 1
            add[i + j] += 1
        heuristic = 0
        lst = [n, minus, add]
        for count in lst:
            for i in count:
                heuristic += count[i] * (count[i] - 1) / 2

        return -heuristic

    def neighbors(self, state):
        # Returns all possible neighbors (next states) of a state
        nearest_list = []
        for i in range(self.N):
            for j in range(self.N):
                if j != state[i]:
                    child = list(state)
                    child[i] = j
                    nearest_list.append(tuple(child))
        return nearest_list
