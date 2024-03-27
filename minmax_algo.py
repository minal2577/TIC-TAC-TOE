import  tic_tac_toe_code as t
def minmax(boards,depth,maximizing):
   scores={'X':-1,'O':1,'Tie':0}
   result = t.check_winner()
   if result or t.is_board_full():
      return scores.get(result, 0) 
   if maximizing :
      best_score=float('-inf')
      for i in range(3):
         for j in range(3):
            if boards[i][j]==' ':
               boards[i][j]= 'O'
               score = minmax(boards,depth+1,False)
               boards[i][j]=' '
               best_score=max(score,best_score)
      return best_score
   else:
      best_score=float('inf')
      for i in range(3):
         for  j in range(3):
            if boards[i][j]==' ':
               boards[i][j]='X'
               score= minmax(boards,depth+1,True)
               boards[i][j]=' '
               best_score=min(score,best_score)
      return best_score