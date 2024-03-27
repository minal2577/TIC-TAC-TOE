import minmax_algo 
import tic_tac_toe_code as t
import visuals
import pygame
from pygame.locals import  *
import sys
def main():
    clock=pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                if t.current_player =='X':
                    row,col = visuals.play(pygame.mouse.get_pos())
                    print("Row:", row, "Col:", col)
                    if t.board[row][col]==' ':
                        t.board[row][col]='X'
                        t.current_player='O'
        winner=t.check_winner()
        if winner:
            t.create_board()
            if winner=='tie':
              print("its a tie")
            else:
                print(f"player {winner} wins")
            pygame.quit()
            sys.exit()
        visuals.screen.fill("WHITE")
        visuals.draw_board(t.board)
        pygame.display.flip()
        clock.tick()
        if t.current_player=='O':
            ai_row,ai_col=t.get_ai_move()
            if t.board[ai_row][ai_col]==' ':
                t.board[ai_row][ai_col]='O'
                t.current_player='X'
if __name__ == '__main__':
    main()

