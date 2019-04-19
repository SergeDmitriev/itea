# Начнем с простейшей игры - крестики-нолики :)
# Реализуйте определение исхода игры на доске.
# Доска представлена кортежем.
# Крестик - 1, нолик - 0, пустые клетки обозначены None.
# Для визуализации я определил переменные с удобными именами.
# None я здесь именую _ (подчеркивание - валидное имя в Python).
import itertools
import random

X, O, _ = 1, 0, None

TEST_BOARD = (
    O, X, O,
    X, O, X,
    _, _, X
)

# Возможны четыре исхода, для них я тоже определил именованные константы.
O_WINS, X_WINS, UNDEFINED, DRAW = range(4)

# Первая подзадача и подсказка - реализуйте функцию,
# которая возвращает все возможные комбинации по 3 клетки в ряд:
# горизонтали, вертикали, диагонали. Таким образом эта часть
# задачи сводится к упражнению на слайсинг последовательности.
# Можете также попробовать реализовать как генератор.


def generate_board():
    l = []
    v = [1, 0, None]

    for i in range(9):
        l.append(random.choice(v))
    return tuple(l)


def slice3(board):
    """
    Возвращает все возможные комбинации по 3 клетки в ряд:
    горизонтали, вертикали, диагонали.

    >>> from pprint import pprint
    >>> pprint(list(slice3((
    ... O, X, O,
    ... X, O, X,
    ... _, _, X
    ... ))))
    [(0, 1, 0),
     (1, 0, 1),
     (None, None, 1),
     (0, 1, None),
     (1, 0, None),
     (0, 1, 1),
     (0, 0, 1),
     (0, 0, None)]
    """
    # board = generate_board()
    horizontals = [board[0:3], board[3:6], board[6:9]]
    verticals = [board[::3], board[1::3], board[2::3]]
    cross = [board[::4], board[2:7:2]]
    x = list(horizontals + verticals + cross)
    # print(x)
    return x


def outcome(board):
    """
    Определение исхода.

    Допущение: доска может содержать только множество корректных состояний,
    которое могут получиться в результате справедливой игры.

    1. Когда на доске перечеркнуты первые 3 клетки - игра завершена.
    В этом случае вы должны определить, кто выиграл, и вернуть
    X_WINS или O_WINS.

    >>> outcome((
    ... X, X, O,
    ... O, X, _,
    ... O, _, X))
    1

    2. Для простоты мы пока предполагаем, что игра всегда доигрывается
    до конца. Пока есть пустые клетки и не перечеркнуты любые 3 -
    исход не определен - UNDEFINED.

    >>> outcome((
    ... X, X, O,
    ... O, O, X,
    ... _, _, X))
    2

    3. Если заполнены все клетки, и нет комбинации из трех смежных,
    выигрыш невозможен ни для кого, присуждаем ничью - DRAW

    >>> outcome((
    ... X, X, O,
    ... O, O, X,
    ... X, X, O))
    3
    """
    sliced = slice3(board)

    # if (1, 1, 1,) in b:
    #     return 1
    # elif (0, 0, 0,) in b:
    #     return 0
    # else:
    #     for i in b:
    #         if None in i:
    #             return 2
    #         elif None not in i:
    #             return 3

    x_wins = (1, 1, 1,)
    o_wins = (0, 0, 0,)

    if x_wins in sliced:
        return 1
    elif o_wins in sliced:
        return 0
    else:
        c = 0
        for i in sliced:
            if None in i:
                c += 1
                return 2
    if c == 0:
        return 3


if __name__ == "__main__":
    import doctest
    doctest.testmod()
