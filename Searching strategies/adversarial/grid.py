class GRID:
    def __init__(self, size=3):
        self.size = size
        self.grid = []

    def build_grid(self):
        for i in range(self.size):
            row = []
            for j in range(self.size):
                row.append(" ")
            self.grid.append(row)

    def get_grid(self):
        return self.grid
    def get_size(self):
        return self.size



# test
grid = GRID()
grid.build_grid()
grid = grid.get_grid()

for row in grid:
    print(row)