import random


class Maze:
    def __init__(self, width=10, height=10, begin=(0, 0), end=(9, 9)):
        self.width = width
        self.height = height
        self._not_walls = set()
        self.begin = begin
        self.end = end
        self.generate_maze()

    def __repr__(self):
        my_str = ""
        for i in range(self.width):
            for k in range(2):
                for j in range(self.height):
                    if k == 0:
                        if j == 0:
                            my_str += "*"
                        if i == 0 or ((i - 1, j),
                                      (i, j)) not in self._not_walls:
                            my_str += "---*"
                        else:
                            my_str += "   *"
                    if k == 1:
                        if j == 0:
                            my_str += "|"
                        if ((i, j), (i, j + 1)) not in self._not_walls:
                            my_str += "   |"
                        else:
                            my_str += "    "
                my_str += "\n"
        my_str += "*"
        for _ in range(self.width):
            my_str += "---*"
        return my_str

    def is_correct_tile(self, tile):
        """
        Check if the tile with coords is in labyrinth
        """
        return 0 <= tile[0] < self.width and 0 <= tile[1] < self.height

    def is_wall(self, tile1, tile2):
        """
        Check if there is a wall between the tiles
        """
        return tuple(
            sorted((tile1, tile2))
        ) not in self._not_walls or not self.is_correct_tile(
            tile1) or not self.is_correct_tile(tile2)

    def adjacent(self, tile):
        """
        Returns list with adjacent tiles (borders don't count)
        """
        adj = []
        if tile[0] > 0:
            adj.append((tile[0] - 1, tile[1]))
        if tile[0] < self.width - 1:
            adj.append((tile[0] + 1, tile[1]))
        if tile[1] > 0:
            adj.append((tile[0], tile[1] - 1))
        if tile[1] < self.height - 1:
            adj.append((tile[0], tile[1] + 1))

        return adj

    def accessible_sides(self, tile):
        """
        Returns tuple of accessible tiles: bool LEFT UP RIGHT DOWN
        """
        tile_x, tile_y = tile
        return (not self.is_wall(tile, (tile_x - 1, tile_y)),
                not self.is_wall(tile, (tile_x, tile_y - 1)),
                not self.is_wall(tile, (tile_x + 1, tile_y)),
                not self.is_wall(tile, (tile_x, tile_y + 1)),
                )

    def remove_wall(self, tile1, tile2):
        """
        Removes wall between two tiles
        """
        if not self.is_correct_tile(tile1) or not self.is_correct_tile(
                tile2):
            return

        self._not_walls.add(tuple(sorted((tile1, tile2))))

    def generate_maze(self):
        """
        Labyrinth generator that uses DFS algorithm
        Simply runs backtracking non-recursive DFS, selecting random walls
        """
        visited = {self.begin}
        stack = [self.begin]
        while stack:
            cur_v = stack[-1]

            adj = self.adjacent(cur_v)
            adj_not_visited = [u for u in adj if u not in visited]

            if not adj_not_visited:
                stack.pop()
            else:
                next_v = random.choice(adj_not_visited)
                self.remove_wall(cur_v, next_v)
                visited.add(next_v)
                stack.append(next_v)


print(Maze())
