import math


def arg_min(T, S):
    amin = -1
    m = math.inf  # максимальное значение
    for i, t in enumerate(T):
        if t < m and i not in S:
            m = t
            amin = i

    return amin


D = ((0, 3, 3, 2, math.inf, math.inf, math.inf),
     (0, math.inf, math.inf, 4, 6, math.inf, math.inf),
     (0, math.inf, math.inf, 4, math.inf, 7, math.inf),
     (0, math.inf, math.inf, math.inf, 3, 4, math.inf),
     (0, math.inf, math.inf, math.inf, math.inf, 1, 8),
     (0, math.inf, math.inf, math.inf, math.inf, math.inf, 6),
     (0, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf))

# D = ((0, 3, 3, 2, 0, 0, 0),
#      (0, 0, 0, 4, 6, 0, 0),
#      (0, 0, 0, 4, 0, 7, 0),
#      (0, 0, 0, 0, 3, 4, 0),
#      (0, 0, 0, 0, 0, 1, 8),
#      (0, 0, 0, 0, 0, 0, 6),
#      (0, 0, 0, 0, 0, 0, 0))

N = len(D)  # число вершин в графе
T = [math.inf] * N  # последняя строка таблицы

v = 0  # стартовая вершина (нумерация с нуля)
S = {v}  # просмотренные вершины
T[v] = 0  # нулевой вес для стартовой вершины
M = [0] * N  # оптимальные связи между вершинами

while v != -1:  # цикл, пока не просмотрим все вершины
    for j, dw in enumerate(D[v]):  # перебираем все связанные вершины с вершиной v
        if j not in S:  # если вершина еще не просмотрена
            w = T[v] + dw
            if w < T[j]:
                T[j] = w
                M[j] = v  # связываем вершину j с вершиной v

    v = arg_min(T, S)  # выбираем следующий узел с наименьшим весом
    if v >= 0:  # выбрана очередная вершина
        S.add(v)  # добавляем новую вершину в рассмотрение

# print(T, M, sep="\n")

# формирование оптимального маршрута:
start = 0
end = 6
P = [end]
while end != start:
    end = M[P[-1]]
    P.append(end)

print(P)
