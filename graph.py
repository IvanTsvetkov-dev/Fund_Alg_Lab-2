import random

import numpy


def generate_matrix(n):
    matrix = numpy.zeros((n, n), dtype=int)
    for i in range(n):
        for j in range(i + 1, n):
            weight = random.randint(1, 100)  # Можно задать вес ребрам. Поставил от 1 до 100
            matrix[i][j] = weight
            matrix[j][i] = weight
    return matrix


class Graph:
    def __init__(self, n=None, filename=None):
        if n is not None:
            self.matrix = generate_matrix(n)
        elif filename is not None:
            self.matrix = self.read_graph_file(filename)
        else:
            raise ValueError("передайте либо количество вершин, либо путь к файлу.")
        self.n = len(self.matrix)

    # Поиск Оптимального/длинного маршрута в графе
    def search(self):
        visited = [False] * len(self.matrix)
        path = []
        current_vertex = self.get_first_vertex()
        total_length = 0

        while True:
            visited[current_vertex] = True
            path.append(current_vertex)

            max_edge_weight = 0
            next_vertex = -1

            for i in range(0, self.n):
                if self.matrix[current_vertex][i] > max_edge_weight and not visited[i]:
                    max_edge_weight = self.matrix[current_vertex][i]
                    next_vertex = i

            if next_vertex == -1:
                break

            total_length += max_edge_weight
            current_vertex = next_vertex

        return path, total_length

    # Ищем стартовую вершину
    def get_first_vertex(self):
        start_vertex = 0
        max_edge = 0
        for i in range(0, self.n):
            for j in range(0, self.n):
                if max_edge < self.matrix[i][j]:
                    max_edge = self.matrix[i][j]
                    start_vertex = i
        return start_vertex

    def read_graph_file(self, path_to_file):
        f = open(path_to_file, 'r')
        matrix = []
        f.readline()
        i = 0
        for line in f:
            matrix.append([])
            for j in range(0, len(line.split())):
                matrix[i].append(int(line.split()[j]))
            i += 1

        f.close()
        return matrix

    def write_graph_file(self, result):
        f = open("result.txt", 'w', encoding="UTF-8")

        f.write("Оптимальный/Самый длинный путь:" + str(result[0]) + '\n' "Длина:" + str(result[1]))
        f.close()

    def print_graph(self):
        print("[")
        for i in self.matrix:
            print("  " + str(i))
        print("]")
