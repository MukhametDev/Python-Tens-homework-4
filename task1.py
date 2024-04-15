from itertools import product
def read_sudoku_from_file(filename):
    with open(filename, 'r') as file:
        grid = [list(map(int, line.split())) for line in file]
    return grid

def write_sudoku_to_file(filename, grid):
    with open(filename, 'w') as file:
        for row in grid:
            file.write(' '.join(map(str, row)) + '\n')

def solve_sudoku(grid):
    from itertools import product

    n = 9
    X, Y = create_cover_matrix(n)

    def search(X, Y, solution):
        if not X:
            return solution
        c = min(X, key=lambda c: len(X[c]))
        for r in list(X[c]):
            solution.append(r)
            cols = select(X, Y, r)
            result = search(cols[0], Y, solution)
            if result:
                return result
            solution.pop()
            deselect(X, Y, r, cols[1])
        return None

    initial_solution = [(r, c, grid[r][c] - 1) for r, c in product(range(n), range(n)) if grid[r][c] != 0]
    solved = search(X, Y, initial_solution)
    if solved:
        solution_grid = [[0] * n for _ in range(n)]
        for r, c, v in solved:
            solution_grid[r][c] = v + 1
        return solution_grid
    return None

def create_cover_matrix(n):
    rows = product(range(n), range(n), range(n))
    columns = product(range(4), range(n), range(n))
    Y = {(r, c, n): [("RC", (r, c)), ("RN", (r, n)), ("CN", (c, n)), ("BN", (3 * (r // 3) + c // 3, n))] for r, c, n in rows}
    X = {j: set() for i in Y for j in Y[i]}
    for i in Y:
        for j in Y[i]:
            X[j].add(i)
    return X, Y

def select(X, Y, r):
    new_X = {j: set(X[j]) for j in X}
    cols = {j: set() for j in Y[r]}

    for j in Y[r]:
        for i in new_X[j]:
            for k in Y[i]:
                if k != j:
                    new_X[k].remove(i)
            cols[j].add(i)

        del new_X[j]

    return new_X, cols

def deselect(X, Y, r, cols):
    for j in reversed(Y[r]):
        for i in cols[j]:
            for k in Y[i]:
                if k != j:
                    X[k].add(i)
        X[j] = cols[j]



def main():
    grid = read_sudoku_from_file('input.txt')
    solved_grid = solve_sudoku(grid)
    if solved_grid:
        write_sudoku_to_file('output.txt', solved_grid)
    else:
        print("Impossible")

if __name__ == "__main__":
    main()
