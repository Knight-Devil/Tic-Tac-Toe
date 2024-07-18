import pygame


pygame.init()
WIDTH, HEIGHT = 500, 500
ROWS, COLS = 3, 3
size = WIDTH // ROWS
LOST_FONT = pygame.font.SysFont('comicsans', 70)
BG_COLOR = "white"
NUM_COLOR = "black"
IMAGE_CROSS = pygame.image.load('cross.png')
IMAGE_CROSS = pygame.transform.scale(IMAGE_CROSS, (int(size), int(size)))

IMAGE_CIRCLE = pygame.image.load('circle.png')
IMAGE_CIRCLE = pygame.transform.scale(IMAGE_CIRCLE, (int(size), int(size)))

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

def get_grid_pos(mouse_pos):
    mx, my = mouse_pos
    row = int(my // size)
    col = int(mx // size)
    return row, col

def win_condition_cross(field):
    won = False
    if((field[0][0]==1 and
       field[1][0]==1 and
       field[2][0]==1 )
         or 
       (field[0][1]==1 and
       field[1][1]==1 and
       field[2][1]==1 ) 
       or
       (field[0][2]==1 and
       field[1][2]==1 and
       field[2][2]==1 ) # cols....
       or
       (field[0][0]==1 and
       field[0][1]==1 and
       field[0][2]==1 ) 
       or 
       (field[1][0]==1 and
       field[1][1]==1 and
       field[1][2]==1 ) 
       or
       (field[2][0]==1 and
       field[2][1]==1 and
       field[2][2]==1 ) # rows....
       or 
       (field[0][0]==1 and
       field[1][1]==1 and
       field[2][2]==1 ) 
       or
       (field[2][0]==1 and
       field[1][1]==1 and
       field[0][2]==1 ) # diagonals....
       ):
        won = True
    return won

def win_condition_circle(field):
    won = False
    if((field[0][0]==0 and
       field[1][0]==0 and
       field[2][0]==0 )
         or 
       (field[0][1]==0 and
       field[1][1]==0 and
       field[2][1]==0 ) 
       or
       (field[0][2]==0 and
       field[1][2]==0 and
       field[2][2]==0 ) # cols....
       or
       (field[0][0]==0 and
       field[0][1]==0 and
       field[0][2]==0 ) 
       or 
       (field[1][0]==0 and
       field[1][1]==0 and
       field[1][2]==0 ) 
       or
       (field[2][0]==0 and
       field[2][1]==0 and
       field[2][2]==0 ) # rows....
       or 
       (field[0][0]==0 and
       field[1][1]==0 and
       field[2][2]==0 ) 
       or
       (field[2][0]==0 and
       field[1][1]==0 and
       field[0][2]==0 ) # diagonals....
       ):
        won = True
    return won

def draw_won(win, text):
    text = LOST_FONT.render(text, 1, "green")
    win.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
    pygame.display.update()




def draw(win, field):
    win.fill(BG_COLOR)
    for i in range(ROWS):
        for j in range(COLS):
            x = size * j
            y = size * i
            if field[i][j] == 1:
                win.blit(IMAGE_CROSS, (x, y))
            elif field[i][j] == 0:
                win.blit(IMAGE_CIRCLE, (x, y))
            pygame.draw.rect(win, NUM_COLOR, (x, y, size, size), 2)  # Draw grid lines
    pygame.display.update()

def main():
    run = True
    field = [[-1 for _ in range(COLS)] for _ in range(ROWS)]  # Initialize the field
    count_clicks = 0
    
# note that the game begins with placing a circle
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                row, col = get_grid_pos(pygame.mouse.get_pos())
                
                if field[row][col] == -1:
                    field[row][col] = count_clicks%2
                    count_clicks+=1  # Switch player
                
            if win_condition_cross(field):
                draw(win, field)
                draw_won(win,"Cross Wins")
                pygame.time.delay(5000)
                run = False
                continue
            if win_condition_circle(field):
                draw(win, field)
                draw_won(win,"Circle Wins")
                pygame.time.delay(5000)
                run = False
                continue
            if count_clicks ==9:
                draw(win, field)
                draw_won(win,"Tie")
                pygame.time.delay(5000)
                run = False
                continue
        draw(win, field)


    pygame.quit()

if __name__ == "__main__":
    main()
