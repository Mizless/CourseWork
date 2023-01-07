from checkers.point import Point
from checkers.enums import CheckerType, SideType

# Сторона за которую играет игрок
PLAYER_SIDE = SideType.WHITE

# Размер поля
X_SIZE = Y_SIZE = 9
# Размер ячейки
CELL_SIZE = 75

# Скорость анимации
ANIMATION_SPEED = 5

# Количество ходов для предсказания (не менять, стоит максимальная возможная сложность при сохранении высокой скорости работы программы)
MAX_PREDICTION_DEPTH = 3

# Ширина рамки
BORDER_WIDTH = 2 * 2

# Цвета игровой доски
FIELD_COLORS = ['#f5deb3', '#747474']
# Цвет рамки при наведении на ячейку мышкой
HOVER_BORDER_COLOR = '#54b346'
# Цвет рамки при выделении ячейки
SELECT_BORDER_COLOR = '#800000'
# Цвет кружков возможных ходов
POSIBLE_MOVE_CIRCLE_COLOR = '#800000'

# Возможные смещения ходов шашек
MOVE_OFFSETS = [
    Point(-1, -1),
    Point( 1, -1),
    Point(-1,  1),
    Point( 1,  1)
]

# Массивы типов белых и чёрных шашек [Обычная пешка, дамка, вождь]
WHITE_CHECKERS = [CheckerType.WHITE_REGULAR, CheckerType.WHITE_QUEEN, CheckerType.WHITE_KING]
BLACK_CHECKERS = [CheckerType.BLACK_REGULAR, CheckerType.BLACK_QUEEN, CheckerType.BLACK_KING]