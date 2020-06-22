class Board:
    """ a data type for a Connect Four board with arbitrary dimensions
    """   
    def __init__(self, height, width):
        """ constructs a new Board object by initializing three attributes """
        self.height = height
        self.width = width
        self.slots = [[' '] * self.width for row in range(self.height)]
        
    
    def __repr__(self):
        """ Returns a string representation of a Board object.
        """
        s = ''         # begin with an empty string

        # add one row of slots at a time to s
        for row in range(self.height):
            s += '|'   # one vertical bar at the start of the row

            for col in range(self.width):
                s += self.slots[row][col] + '|'

            s += '\n'  # newline at the end of the row

        s += '-'
        for dash in range(self.width):
            s += '--'
        s += '\n'
        
        for n in range(self.width):
            if n < 10:
                s = s+ ' '+ str(n)
            else:
                s = s+ ' '+ str((n%10))
        return s

    def add_checker(self, checker, col):
        """ adds the specified checker (either 'X' or 'O') to the
            column with the specified index col in the called Board.
            inputs: checker is either 'X' or 'O'
                    col is a valid column index
        """
        assert(checker == 'X' or checker == 'O')
        assert(col >= 0 and col < self.width)
        
        ### put the rest of the method here ###
        pos = 0
        for row in range(self.height):
            if self.slots[row][col] == ' ':
                pos = row
        
        self.slots[pos][col] = checker 
    
    def reset(self):
        """ reset the Board object on which it is called by setting all slots
        to contain a space character """
        
        for row in range(self.height):
            for col in range(self.width):
                self.slots[row][col] = ' '
    
    def add_checkers(self, colnums):
        """ takes a string of column numbers and places alternating
            checkers in those columns of the called Board object,
            starting with 'X'.
            input: colnums is a string of valid column numbers
        """
        checker = 'X'   # start by playing 'X'

        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)

            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'

    ### add your remaining methods here
    def can_add_to(self, col):
        """ returns True if it is valid to place a checker in the column col
        on the calling Board object. Otherwise, it should return False
        """
        if col < 0 or col > (self.width - 1):
            return False
        elif self.slots[0][col] != ' ':  
            return False
        else:
            return True 
    
    def is_full(self):
        """  returns True if the called Board object is completely full of 
        checkers, and returns False otherwise """
        
        for col in range(self.width):
            if self.can_add_to(col) == True:
                return False
        return True 
    
    def remove_checker(self, col):
        """ removes the top checker from column col of the called Board
        object. If the column is empty, then the method should do nothing
        """
        for row in range(self.height):
            if row == self.height - 1 and self.slots[row][col] == ' ':
                self.slots[row][col] = ' '               
            elif self.slots[row][col] != ' ':
                self.slots[row][col] = ' '
                break
            elif self.slots[row][col] == ' ' and self.slots[row+1][col] != ' ':
                self.slots[row+1][col] = ' '
                break 
    
    def is_horizontal_win(self, checker):
        """ Checks for a horizontal win for the specified checker """
        for row in range(self.height):
            for col in range(self.width - 3):
            # Check if the next four columns in this row
            # contain the specified checker.
                if self.slots[row][col] == checker and \
                   self.slots[row][col + 1] == checker and \
                   self.slots[row][col + 2] == checker and \
                   self.slots[row][col + 3] == checker:
                    return True
        return False
    
    def is_vertical_win(self, checker):
        """ Checks for a vertical win for the specified checker """
        for col in range(self.width):
            for row in range(self.height - 3):
                if self.slots[row][col] == checker and \
                   self.slots[row + 1][col] == checker and \
                   self.slots[row + 2][col] == checker and \
                   self.slots[row + 3][col] == checker:
                       return True
        return False
    
    def is_down_diagonal_win(self,checker):
        """ Checks for a vertical win for the specified checker """
        for row in range(self.height - 3):
            for col in range(self.width - 3):
               if self.slots[row][col] == checker and \
                  self.slots[row + 1][col + 1] == checker and \
                  self.slots[row + 2][col + 2] == checker and \
                  self.slots[row + 3][col + 3] == checker:
                      return True
        return False
    
    def is_up_diagonal_win(self,checker):
        """ Checks for a vertical win for the specified checker """
        for row in range(self.height - 3):
            for col in range(3,self.width):
                if self.slots[row][col] == checker and \
                   self.slots[row + 1][col - 1] == checker and \
                   self.slots[row + 2][col - 2] == checker and \
                   self.slots[row + 3][col - 3] == checker:
                       return True
        return False
    
    def is_win_for(self, checker):
        """ returns True if there are four consecutive slots containing checker 
        on the board. Otherwise, it should return False """
    
        assert(checker == 'X' or checker == 'O')
        
        if self.is_vertical_win(checker) == True:
            return True
        elif self.is_horizontal_win(checker) == True:
            return True
        elif self.is_down_diagonal_win(checker) == True:
            return True
        elif self.is_up_diagonal_win(checker) == True:
            return True
        else:
            return False
            
            
class Player:
    """ a data type to represent a player of the Connect Four game """
    def __init__(self, checker):
        """ constructs a new Player object """
            
        assert(checker == 'X' or checker == 'O')
        self.checker = checker
        self.num_moves = 0
        
    def __repr__(self):
        """ returns a string representing a Player object """
        return 'Player ' + self.checker 
    
    def opponent_checker(self):
        """ returns a one-character string representing the checker of the 
        Player object’s opponent """
        if self.checker == 'X':
            return 'O'
        else:
            return 'X'
        
    def next_move(self, b):
        """ returns the column where the player wants to make the next move
        """
        self.num_moves += 1
        
        while True:
            col = int(input('Enter a column: '))
            
            if b.can_add_to(col) == True:
                return col
            else:
                print('Try again!')

def connect_four(player1, player2):
    """ Plays a game of Connect Four between the two specified players,
        and returns the Board object as it looks at the end of the game.
        inputs: player1 and player2 are objects representing Connect Four
                  players (objects of the Player class or a subclass of Player).
                  One player should use 'X' checkers and the other should
                  use 'O' checkers.
    """
    # Make sure one player is 'X' and one is 'O'.
    if player1.checker not in 'XO' or player2.checker not in 'XO' \
       or player1.checker == player2.checker:
        print('need one X player and one O player.')
        return None

    print('Welcome to Connect Four!')
    print()
    board = Board(6, 7)
    print(board)
    
    while True:
        if process_move(player1, board):
            return board

        if process_move(player2, board):
            return board
    
def process_move(p, b):
    """ The function will perform all of the steps involved in processing a 
    single move by player p on board b """
    
    print(str(p) + "'s turn")
    print()
    
    move = p.next_move(b)
    b.add_checker(p.checker,move)
    print()
    print(b)
    
    if b.is_win_for(p.checker) == True:
        print('Player X wins in ' + str(p.num_moves)+' moves.')
        print('Congratulations!')
        return True
    elif b.is_full() == True:
        print("It's a tie!")
        return True
    else:
        return False   
