import tic_tac_toe_code as t
import pygame
from pygame.locals import  *
import sys

pygame.init()
t.current_player
WIDTH,HEIGHT=300,300
CELL_SIZE =WIDTH//3
WHITE=(255,255,255)
BLACK=(0,0,0)
FPS=38
screen =pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")
font = pygame.font.Font(None,36)
def draw_board(board):
  for i in range(1,3):
    pygame.draw.line(screen,BLACK,(i*CELL_SIZE,0),(i*CELL_SIZE,HEIGHT),2)
    pygame.draw.line(screen,BLACK,(0,i*CELL_SIZE),(WIDTH,i*CELL_SIZE),2)
  for row in range(3):
    for col in range(3):
      player =board[row][col]
      if player=='X':
       draw_x(col * CELL_SIZE, row * CELL_SIZE)
      elif player=='O':
        draw_O(col * CELL_SIZE, row * CELL_SIZE)
def draw_x(x,y):
  pygame.draw.line(screen,BLACK,(x+20,y+20),(x+CELL_SIZE-20,y+CELL_SIZE-20),2)
  pygame.draw.line(screen,BLACK,(x+CELL_SIZE-20,y+20),(x+20,y+CELL_SIZE -20),2)
def draw_O(x,y):
 pygame.draw.circle(screen,BLACK,(x+CELL_SIZE//2,y+CELL_SIZE//2),CELL_SIZE//2 -20,2)
def play(mouse_pos):
    if mouse_pos[0] < 0 or mouse_pos[0] >= WIDTH or \
            mouse_pos[1] < 0 or mouse_pos[1] >= HEIGHT:
        return -1, -1
    row = mouse_pos[1] // CELL_SIZE
    col = mouse_pos[0] // CELL_SIZE
    row = round(row)
    col = round(col)
    row = max(0, min(row, 2))
    col = max(0, min(col, 2))
    return row, col