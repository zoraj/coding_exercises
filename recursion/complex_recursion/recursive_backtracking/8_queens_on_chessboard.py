
# http://stackoverflow.com/questions/5133509/eight-queens-problem-in-python
# http://pyeda.readthedocs.org/en/latest/queens.html

BOARD_SIZE = 8

def under_attack(column, existing_queens):
    # ASSUMES that row = len(existing_queens)
    # this assumption is hard coded into the algorithm. that's okay, it makes sense here. 
    row = len(existing_queens)
    for queen in existing_queens:
        r,c = queen # get coordinates of existing queen
        if r == row: return True # check row
        if c == column: return True # check column
        if (column-c) == (row-r): return True # check left diagonal, offset is (-1, -1)
        if (column-c) == -(row-r): return True # check right diagonal, offset is (1, 1)

        # the above assumes that you are only placing queens on a board from left to right 
        # exiting queens will only exist on the left side of the board relative to current position in consideration

        # more rigorous test would be to write a while loop and 
        # keep on adding on offset to current position until you reach the end of the board
        # ensure you don't run into any queens along the way

        # okay, actually, I lied. The above is perfectly fine. plug and chug to test!!!!!!! it's like an absolute relative positioning thing.
    return False

# solve a board for n queens
def solve(n):
    if n == 0: 
        return [[]]
    
    smaller_solutions = solve(n - 1) # solve for placing a smaller number of queens
    # this will be a list of lists of tuples/queen coordinates

    current_solutions = []
    for solution in smaller_solutions: # solution is a list
        for column in range(0, BOARD_SIZE):
            # try adding a new queen to row = n - 1, column = column
            # (off by one for grid coordiates that include (0,0), column = column 
            if not under_attack(column, solution):
                row = n - 1 # place current queen as high on the board as possible
                # eventually, will place one queen in each of the eight rows
                current_solutions.append(solution + [(row, column)])
    return current_solutions

# WRITE A FUNCTION TO RETURN ONLY ONE SOLUTION.

if __name__ == "__main__":
    n = 8
    import pprint
    pprint.pprint(solve(n))
    print len(solve(n))
