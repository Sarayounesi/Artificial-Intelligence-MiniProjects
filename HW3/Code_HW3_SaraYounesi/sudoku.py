from time import time


class Sudoku:
    def __init__(self, dim, fileDir):
        self.dim = dim
        self.expandedNodes = 0
        with open(fileDir) as f:
            content = f.readlines()
            self.board = [list(x.strip()) for x in content]
        self.rv = self.get_remaining_puzzle()

    def isSafe(self, row, col, choice):
        choiceStr = str(choice)
        for i in range(self.dim):
            if self.board[row][i] == choiceStr or self.board[i][col] == choiceStr:
                return False

        boxR = row - (row % 3)
        boxV = col - (col % 3)
        for i in range(3):
            for j in range(3):
                if self.board[boxR + i][boxV + j] == choiceStr:
                    return False
        return True

    # for simple backtracking
    def get_next_location(self):
        for i in range(self.dim):
            for j in range(self.dim):
                if self.board[i][j] == '0':
                    return i, j
        return -1, -1

    # this fun return valid choice per cell
    def get_valid_domain(self, row, col):
        valid_domain = [str(i) for i in range(1, self.dim + 1)]

        # check horizontally
        for i in range(self.dim):
            if self.board[row][i] != '0':
                if self.board[row][i] in valid_domain:
                    valid_domain.remove(self.board[row][i])

        # check vertically
        for i in range(self.dim):
            if self.board[i][col] != '0':
                if self.board[i][col] in valid_domain:
                    valid_domain.remove(self.board[i][col])

        # check index in its square
        square_i = row - row % 3
        square_j = col - col % 3
        for i in range(3):
            for j in range(3):
                if self.board[square_i + i][square_j + j] != 0:
                    if self.board[square_i + i][square_j + j] in valid_domain:
                        valid_domain.remove(self.board[square_i + i][square_j + j])
        return valid_domain

    # this fun return minimum remaining value index of self.board
    # it means it prefer the i, j which are in row, col with minimum number of '0'
    def get_next_mrv_location(self):
        min_empty_per_i = float('inf')
        min_empty_per_j = float('inf')
        _i, _j = 9, 9
        minRow = []
        for i in range(self.dim):
            counter = 0
            if '0' not in self.board[i]:
                continue
            for j in range(self.dim):
                if self.board[i][j] == '0':
                    counter += 1
            if min_empty_per_i > counter:
                min_empty_per_i = counter
                minRow = self.board[i]
                _i = i
        if not minRow:
            return -1, -1
        else:
            for i in range(self.dim):
                counter = 0
                if minRow[i] == '0':
                    for j in range(self.dim):
                        if self.board[j][i] == '0':
                            counter += 1
                    if counter < min_empty_per_j:
                        min_empty_per_j = counter
                        _j = i
            return _i, _j

    # this fun return rv list , it checks all cell
    def get_remaining_puzzle(self):
        rv_list = []
        for i in range(self.dim):
            for j in range(self.dim):
                if self.board[i][j] != '0':
                    rv_list.append(['x'])
                else:
                    rv_list.append(self.get_valid_domain(i, j))
        return rv_list

    # backtracking
    def solveSimpleBackTracking(self):
        current_position = self.get_next_location()
        if current_position[0] == -1:
            return True
        else:
            i, j = current_position
            self.expandedNodes += 1
            for choice in range(1, self.dim + 1):
                if self.isSafe(i, j, choice):
                    self.board[i][j] = str(choice)
                    if self.solveSimpleBackTracking():
                        return True
                    self.board[i][j] = '0'
            return False

    # CSP forward checking
    def solveCSPF(self):
        current_position = self.get_next_mrv_location()
        if current_position[0] == -1:
            return True
        else:
            self.expandedNodes += 1
            i, j = current_position

            for choice in self.rv[i * 9 + j]:
                self.board[i][j] = str(choice)
                # get a copy from rv list to forward checking
                rv_copy = self.get_remaining_puzzle()
                if [] in rv_copy:
                    self.board[i][j] = '0'
                elif self.solveCSPF():
                    return True
                self.board[i][j] = '0'
            return False


if __name__ == '__main__':
    file = 'samples/hardest.txt'

    # create sudoku
    sudoku_solver = Sudoku(9, file)

    # print empty sudoku
    for x in sudoku_solver.board:
        print(x)

    start = time()

    # sudoku_solver.solveSimpleBackTracking()  # ==> solving sudoku using simple backtracking ==> part A
    sudoku_solver.solveCSPF()  # ==> solving sudoku using CSP forward backtracking ==> part B

    end = time()

    print()

    # print filled sudoku
    for x in sudoku_solver.board:
        print(x)
        
    print("Time Elapsed:{} ".format((end - start) * 1000), "ms")
    print("Expanded node:{} ".format(sudoku_solver.expandedNodes))
