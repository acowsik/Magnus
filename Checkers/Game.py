BLACK = 0b001
WHITE = 0b010
KING  = 0b100
BLANK = 0b000

STANDARD_BOARD = [
    [BLANK, WHITE, BLANK, WHITE, BLANK, WHITE, BLANK, WHITE],
    [WHITE, BLANK, WHITE, BLANK, WHITE, BLANK, WHITE, BLANK],
    [BLANK, WHITE, BLANK, WHITE, BLANK, WHITE, BLANK, WHITE],
    [BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK],
    [BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK],
    [BLACK, BLANK, BLACK, BLANK, BLACK, BLANK, BLACK, BLANK],
    [BLANK, BLACK, BLANK, BLACK, BLANK, BLACK, BLANK, BLACK],
    [BLACK, BLANK, BLACK, BLANK, BLACK, BLANK, BLACK, BLANK]
]

class Game(object):
    def __init__(self, board=None):
        """
        :param board: If you want to pass in a non-standard starting board in row-major order. The board
        should start with the first row being white's home row.
        """