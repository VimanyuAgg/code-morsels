import copy

def solveNQueens(n: int, serialized=False):
    '''@input: n is the grid size'''
    res = []
    # columns[6] = 3 means on row '6' queen is placed on column 3
    cols = [0 for _ in range(n)]

    def _placeQueen(row, columns):

        # Below doesn't work as it's not possible that we hit solution everytime while placing queen on last row
        # if row == n - 1:
        #     remaining_col = n * (n + 1) // 2 - sum(columns)
        #     columns[row] = remaining_col
        #     res.append(copy.deepcopy(columns))

        if row == n:
            res.append(copy.deepcopy(columns))

        else:
            for i in range(n):
                if _can_place_queen(i, row, columns):
                    columns[row] = i
                    _placeQueen(row + 1, columns)


    def _can_place_queen(col, row, columns):
        for i in range(row):
            if columns[i] == col:
                return False

            # Check one diagonal (\)
            if i + columns[i] == row + col:
                return False

            # Check other diagonal (/)
            if i - columns[i] == row - col:
                return False

        return True

    def _serialize_result():
        nonlocal res
        serres = []
        for sol in res:
            ser_sol = []
            for i in range(n):
                entry = ['.' for _ in range(n)]
                entry[sol[i]] = 'Q'
                ser_sol.append(''.join(entry))
            serres.append(ser_sol)

        return serres

    _placeQueen(0, cols)

    if not serialized:
        return res

    else:
        return _serialize_result()
