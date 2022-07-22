import numpy as np
import logging
import sys
import time

msg0 = "Enter the knight's starting position:"
msg1 = 'Enter your board dimensions:'
msg2 = 'Here are the possible moves:'
msg3 = 'Enter your next move:'
msg4 = 'No more possible moves!'
msg5 = 'Your knight visited {} squares'
msg6 = 'Do you want to try the puzzle? (y/n):'
msg7 = 'Invalid input!'
msg8 = "Here's the solution!"
msg9 = 'No solution exists!'
msg_invalid_dim = 'Invalid dimensions!'
msg_invalid_move = 'Invalid move!'
msg_win = 'What a great tour! Congratulations!'

logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')


class Board:
    def __init__(self, n, m):
        self.len_m = len(str(m))
        self.len_n = len(str(n))
        self.len_dim = len(str(m * n))
        self.n = int(n)
        self.m = int(m)
        self.size = self.n * self.m
        self.space = '_' * len(str(n * m))
        self.matrix = np.full((n, m), self.space)
        self.border = ' ' * self.len_n + '---' + '-' * m * (len(self.space) + 1)

    def show(self):
        # Prints the current board state
        print(self.border)
        for i in range(len(self.matrix), 0, -1):
            print(' ' * (self.len_n - len(str(i))) + str(i) + '|', end=' ')
            for j in self.matrix[i - 1]:
                print(j, end=' ')
            print('|')
        print(self.border)
        print(' ' * (self.len_n + 1), *[' ' * (self.len_dim - len(str(x))) + str(x) for x in range(1, self.m + 1)])

    def check_coord(self, i, j, errors=False):
        # Checks the given coordinates. Prints errors if errors is set to True
        try:
            if str(int(i)) != str(i) or str(int(j)) != str(j) or \
                    not (0 < int(i) <= int(self.m) and 0 < int(j) <= int(self.n)):
                if errors:
                    print(msg_invalid_dim)
                return False
        except ValueError:
            if errors:
                print(msg_invalid_dim)
            return False
        return True

    def fill_with(self, coord_list, obj=None):
        # Fills the squares in coord_list on the board with obj. Empties them by default
        logging.debug(f'Filling {coord_list} with {obj}')
        if not obj:
            obj = ''
        for x, y in coord_list:
            self.place(x, y, obj)


class Knight(Board):
    def __init__(self, n, m, id):
        super().__init__(n, m)
        self.i = -1
        self.j = -1
        self.board = Board(n, m)
        self.id = id
        self.step = 0
        self.visited = set()
        self.moves = dict()

    def available(self, coords):
        # Checks if a square (coords) has not been visited before (is available)
        if coords in self.visited:
            return False
        return True

    def get_moves(self, coordinates):
        # Gets valid moves from coordinates, returns a list.
        m, n = coordinates[0], coordinates[1]
        visited = self.visited.copy()
        visited.add((int(m), int(n)))
        valid_moves = []
        knight_moves = [(1, 2), (2, 1), (-1, 2), (2, -1), (-2, -1), (-1, -2), (1, -2), (-2, 1)]
        for i, j in knight_moves:
            x, y = int(m) + i, int(n) + j
            if self.check_coord(x, y, errors=False) and (x, y) not in visited:
                valid_moves.append((x, y))
        return valid_moves

    def place(self, i, j, obj, update=False):
        # Places an object on the board. Updates the board if update is True
        if self.check_coord(i, j, errors=True):
            if update:
                self.i, self.j = i, j
            if not obj:
                obj = self.space
            else:
                obj = ' ' * (len(self.space) - len(str(obj))) + str(obj)
            self.matrix[int(j) - 1][int(i) - 1] = obj
            return True
        logging.debug(f'Did not place the piece because reasons {i}, {j}')
        return False

    def place_piece(self, i, j, obj):
        # Places the obj on the board
        self.place(i, j, obj, update=True)
        self.visited.add((int(i), int(j)))

    def moves_matrix(self, coordinates):
        # Returns a matrix of moves, depth 2: {move1: [move1.1, move1.2, ...], move2: [move2.1, ...]}
        if not coordinates:
            return
        valid_coords = dict()
        m, n = coordinates[0], coordinates[1]
        for coords in self.get_moves((m, n)):
            valid_coords[coords] = self.get_moves(coords)
        return valid_coords

    def show_moves(self):
        # Prints the current board with possible moves for the active piece, marked
        self.moves = self.moves_matrix((self.i, self.j))
        for coord, move_list in self.moves.items():
            self.place(coord[0], coord[1], len(move_list))
        self.show()
        self.fill_with(list(self.moves.keys()))

    def move(self, end):
        # Moves the obj (self) to the selected coordinates (end)
        i, j = end
        logging.debug(f'Looking for {i}, {j} in {set(self.moves.keys())}')
        if end in self.moves.keys():
            logging.debug(f'Moving {self.id}: {self.i}, {self.j} to {i}, {j}')
            self.fill_with([(self.i, self.j)], obj='*')
            self.place_piece(i, j, self.id)
            self.i = i
            self.j = j


def check_dimensions(dimensions: str, errors=None) -> bool:
    # Checks if the dimensions entered are valid
    try:
        n, m = dimensions.split()
    except ValueError:
        if errors:
            print(msg_invalid_dim)
        return False
    try:
        if str(int(n)) != n or str(int(m)) != m or \
                not (0 < int(n) and 0 < int(m)):
            if errors:
                print(msg_invalid_dim)
            return False
    except ValueError:
        if errors:
            print(msg_invalid_dim)
        return False
    return True


def create():
    # Creates the board
    while True:
        dimensions = input(msg1)
        if check_dimensions(dimensions, errors=True):
            n, m = dimensions.split()
            global knight01
            knight01 = Knight(int(m), int(n), 'X')
            break


def play():
    # Lets the user try and solve the puzzle
    while True:
        knight01.show_moves()
        while True:
            if knight01.moves:
                x, y = input(msg3).split()
                if knight01.check_coord(x, y, errors=True):
                    if knight01.available((int(x), int(y))) and (int(x), int(y)) in knight01.moves:
                        knight01.move((int(x), int(y)))
                        break
                    else:
                        print(msg_invalid_move, end=' ')
                else:
                    print(msg_invalid_dim)
            elif len(knight01.visited) == knight01.size:
                print(msg_win)
                return True
            else:
                print(msg4)
                print(msg5.format(len(knight01.visited)))
                return False


def solve(coords_list):
    # Recursive function that tries to solve the Knights Puzzle. Accepts a list of tuples (coordinates)
    tmp_list = coords_list.copy()
    if len(coords_list) == knight01.size:
        perf_chk01 = time.perf_counter()
        logging.debug(f'Solution found: {coords_list}')
        logging.info(f'Solution found. Runtime: {round((perf_chk01 - perf_start)*1000, 2)}ms')
        return coords_list
    i, j = coords_list[-1]
    matrix = knight01.moves_matrix((int(i), int(j)))
    matrix = dict(sorted(matrix.items(), key=lambda item: len(item[1])))
    logging.debug(matrix)
    for pos, move_list in matrix.items():
        if pos not in coords_list:
            tmp_list = solve(tmp_list + [pos])
            if tmp_list and len(tmp_list) > len(coords_list):
                coords_list = tmp_list
    return coords_list


def start():
    create()

    while True:
        try:
            x, y = input(msg0).split()
            if knight01.check_coord(x, y, errors=True):
                break
        except ValueError:
            print(msg_invalid_dim)

    knight01.place_piece(int(x), int(y), knight01.id)
    sys.setrecursionlimit(5000)
    global perf_start
    perf_start = time.perf_counter()
    solution = solve([(int(x), int(y))])
    sys.setrecursionlimit(1000)

    while True:
        answer = input(msg6)

        if answer == 'y':
            if len(solution) == knight01.size:
                play()
                break
            else:
                print(msg9)
                break
        elif answer == 'n':
            logging.debug(f'Board size: {knight01.size}, Solution size: {len(solution)}')
            if len(solution) == int(knight01.size):
                print(msg8)
                for num, coords in enumerate(solution):
                    knight01.place(int(coords[0]), int(coords[1]), str(num + 1))
                knight01.show()
            else:
                print(msg9)
            break
        else:
            print(msg7)


if __name__ == "__main__":
    start()
