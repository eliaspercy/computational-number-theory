# Originally for the leetcode problem: "Find Winner on a Tic Tac Toe Game"

def tictactoe(self, moves: List[List[int]]) -> str:
    # Number theoretic approach: entails calculating a value for each player
    # based on their moves, and if their value is divisible by one of the 
    # "winning numbers", each calculated by multiplying the numbers representing
    # combinations of winning grid positions (each number is a prime), then 
    # by the uniqueness of prime factors, this player will have a winning combo

    grid = [[2,  3,  5 ], # row1 = 30, row2 = 1001, row3 = 7429
            [7,  11, 13], # col1 = 238, col2 = 627, col3 = 1495
            [17, 19, 23]] # diag1 = 506, diag2 = 935
    win_nums = (30, 1001, 7429, 238, 627, 1495, 506, 935)

    a = 1
    b = 1
    for i, move in enumerate(moves):
        if i % 2 == 0:
            a *= grid[move[0]][move[1]]
        else:
            b *= grid[move[0]][move[1]]

    for num in win_nums:
        if a % num == 0:
            return "A"
        elif b % num ==0:
            return "B"

    return "Draw" if len(moves) == 9 else "Pending"
 

def testit():
    print(tictactoe([[0,0],[2,0],[1,1],[2,1],[2,2]])) == "A"
