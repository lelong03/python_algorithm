import math


def dots_and_boxes(ar):
    n = get_n(ar)
    squares = {}
    player_1 = player_2 = 0
    is_player_1 = true
    for x, y in ar:
        x, y = sort_p(x, y)
        squares[(x,y)] = True
        if ((x, x+n) in squares and (y, y+n) in squares and (x+n, y+n) in squares) \
                or ():
            if is_player_1:
                player_1 += 1
            else:
                player_2 += 1


def sort_p(x, y):
    if x < y:
        return x, y
    return y, x

def get_n(ar):
    max = 0
    for item in ar:
        x, y = item
        if max < x:
            max = x
        if max < y:
            max = y
    return int(math.sqrt(max+1))


dots_and_boxes(((0,1),(7,8),(1,2),(6,7),(0,3),(5,8),(3,4),(1,4),(4,5),(2,5),(4,7),(3,6)))