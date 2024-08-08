
class Game():
    def __init__(self, turn='X', tie=False, winner=None, board={
        'a1': None, 'b1': None, 'c1': None,
        'a2': None, 'b2': None, 'c2': None,
        'a3': None, 'b3': None, 'c3': None,
        }):
        self.turn = turn
        self.tie = tie
        self.winner = winner
        self.board = board
    
    def print_board(self):
        b = self.board
        print(f"""
        A   B   C
    1)  {b['a1'] or ' '} | {b['b1'] or ' '} | {b['c1'] or ' '}
        ----------
    2)  {b['a2'] or ' '} | {b['b2'] or ' '} | {b['c2'] or ' '}
        ----------
    3)  {b['a3'] or ' '} | {b['b3'] or ' '} | {b['c3'] or ' '}
  """)
        
    def get_move(self):
        move = input("Enter a valid move (example: A1): ").lower()

        while move not in {"a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3"}:
            move = input("Enter a valid move (example: A1): ").lower()
            if self.board[move] != None:
                print('Location already selected, please choose another!')
            continue

        while True:
            self.board[move] = self.turn
            break
            
    def win_check(self):
        #rows
        if self.board['a1'] and (self.board['a1'] == self.board['b1'] == self.board['c1']):
            self.winner = self.turn
        elif self.board['a2'] and (self.board['a2'] == self.board['b2'] == self.board['c2']) :
            self.winner = self.turn
        elif self.board['a3'] and (self.board['a3'] == self.board['b3'] == self.board['c3']) :
            self.winner = self.turn
        #columns
        elif self.board['a1'] and (self.board['a1'] == self.board['a2'] == self.board['a3']) :
            self.winner = self.turn
        elif self.board['b1'] and (self.board['b1'] == self.board['b2'] == self.board['b3']) :
            self.winner = self.turn
        elif self.board['c1'] and (self.board['c1'] == self.board['c2'] == self.board['c3']) :
            self.winner = self.turn
        #diagonal
        elif self.board['a1'] and (self.board['a1'] == self.board['b2'] == self.board['c3']) :
            self.winner = self.turn
        elif self.board['c1'] and (self.board['c1'] == self.board['b2'] == self.board['a3']) :
            self.winner = self.turn
        
    def tie_check(self):
        if None not in self.board.values():
            self.tie = True

    def player_switch(self):
        if self.turn == 'X':
            self.turn = 'O'
        else: 
            self.turn = 'X'
                  
    def print_message(self):
        if self.tie == True:
            print(f'Tie Game!')
        elif self.winner == 'X' or self.winner == 'O':
            print(f'{self.winner} wins the game!')
        else:
            print(f"It's player {self.turn}'s turn!")

    def play_game(self):
        print(f'Welcome to Tic-Tac-Toe')
        while self.winner == None:
            Game.print_board(self)
            Game.print_message(self)
            Game.get_move(self)
            Game.win_check(self)
            Game.tie_check(self)
            Game.player_switch(self)
            continue
        if self.winner:
            Game.print_board(self)
            Game.print_message(self)


Game().play_game()
