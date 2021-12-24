import math


def get_link_v(v, D):
    for i, weight in enumerate(D[v]):
        if weight > 0:
            yield i


def arg_min(T, S):
    amin = -1
    m = max(T)
    for i, t in enumerate(T):
        if t < m and i not in S:
            m = t
            amin = i

    return amin


D = ((0, 3, 3, 2, 0, 0, 0),
     (0, 0, 0, 4, 6, 0, 0),
     (0, 0, 0, 4, 0, 7, 0),
     (0, 0, 0, 0, 3, 4, 0),
     (0, 0, 0, 0, 0, 1, 8),
     (0, 0, 0, 0, 0, 0, 6),
     (0, 0, 0, 0, 0, 0, 0))

N = len(D)  # число вершин в графе
T = [math.inf] * N  # последняя строка таблицы

v = 0  # начальная вершина (стартовая)
S = {v}  # просмотренные вершины
T[v] = 0  # нулевой вес дл стартовой вершины

while v != -1:  # цикл, пока не рассмотрем все вершины
    for j in get_link_v(v, D):  # перебираем все связанные вершины
        if j not in S:  # если вершина еще в просмотренной вершине
            weight = T[v] + D[v][j]
            if weight < T[j]:
                T[j] = weight

v = arg_min(T, S)
if v > 0:
    S.add(v)

print(T)
