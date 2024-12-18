from graph import Graph

# Создали сущность Граф. В конструктор передали значение вершин для генерации графа
graph = Graph(n=3)

# graph = Graph(filename="matrix.txt")

# Распечатали граф, который был либо сгенерирован, либо прочитали из файла
graph.print_graph()

# Ищем самый длинный/оптимальный маршрут
result = graph.search()

# Распечатали результат
print(result)

# Записывем результат вычислений в result.txt
graph.write_graph_file(result)

