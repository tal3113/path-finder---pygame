from utils import pygame
from queue import PriorityQueue
# ----------------- Classes  ----------------- #
class Algorithm:
    def __init__(self, start, end):
        self.count = 0
        self.open_set = self.init_open_set(start)
        self.came_from = {}
        self.open_set_hash = {start}

    def init_open_set(self, start):
        open_set = PriorityQueue()
        open_set.put((0, self.count, start))
        return open_set

    def initialize_function(self, start, grid, initialize_start):
        func = {node: float("inf")
                for row in grid for node in row}
        func[start] = initialize_start
        return func

    def h(self, p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        return abs(x1 - x2) + abs(y1 - y2)

    def reconstruct_path(self, current, start, draw):
        while current in self.came_from:
            current = self.came_from[current]
            if current == start:
                break
            current.make_path()
            draw()

    def update_sets(self, f_score, neighbor):
        self.count += 1
        self.open_set.put((f_score[neighbor], self.count, neighbor))
        self.open_set_hash.add(neighbor)
        neighbor.make_open()

    def update_greater_g_score(self, g_score, f_score, neighbor, current, temp_g_score, end):
        self.came_from[neighbor] = current
        g_score[neighbor] = temp_g_score
        f_score[neighbor] = temp_g_score + \
            self.h(neighbor.get_pos(), end.get_pos())

    def calculate_f_score_neighbor(self, g_score, f_score, current, neighbor, end):
        temp_g_score = g_score[current] + 1
        if temp_g_score < g_score[neighbor]:
            self.update_greater_g_score(
                g_score, f_score, neighbor, current, temp_g_score, end)
            if neighbor not in self.open_set_hash:
                count = self.update_sets(f_score, neighbor)

    def run_algorithm(self, draw, start, end, grid):
        g_score = self.initialize_function(start, grid, 0)
        f_score = self.initialize_function(
            start, grid, self.h(start.get_pos(), end.get_pos()))
        while not self.open_set.empty():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            current = self.open_set.get()[2]

            self.open_set_hash.remove(current)

            if current == end:
                self.reconstruct_path(end, start, draw)
                end.make_end()
                return True

            for neighbor in current.neighbors:
                self.calculate_f_score_neighbor(
                    g_score, f_score, current, neighbor, end)

            draw()

            if current != start:
                current.make_closed()

        return False
