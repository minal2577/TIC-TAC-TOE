current_player='X'
import minmax_algo 
import visuals
import main
board=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
def create_board():
    for row in board:
        print('|'.join(row))
        print('-'* 5)
def check_winner():
    for i in range(3):
     if board[i][0]==board[i][1]==board[i][2]!=' ':
        return board[i][0]
     if board[0][i]==board[1][i]==board[2][i]!=' ':
        return board[0][i]
     if board[0][0]==board[1][1]==board[2][2]!=' ':
        return board[0][0]
     elif board[0][2]==board[1][1]==board[2][0]!=' ':
        return board[0][2]
    if all(board[i][j]!=' 'for i in range(3) for j in range(3)):
     return 'tie'
    return None
def get_player_input():
   while True:
     try:
       print('player',current_player,'ente row(0-2)')
       row=int(input())
       print('player',current_player,'ente row(0-2)')
       col=int(input())
       if 0<=row<=2 and 0<=col<=2 and board ==' ':
        board[row][col]=current_player
        break
       else:
          print('invalid')
     except ValueError:
        print('invalid input')

def get_ai_move():
   best_score=float('-inf')
   best_move=None
   for i in range(3):
      for j in range(3):
         if board[i][j]==' ':
            board[i][j]='O'
            score=minmax_algo.minmax(board,0,False)
            board[i][j]=' '
            if score >best_score:
               best_score=score
               best_move=(i,j)
   return best_move
def is_board_full():
    for row in board:
        for cell in row:
            if cell == ' ':
                return False 
    return True 

