import pygame
import os

pygame.init()

screen = pygame.display.set_mode([1000, 900])
pygame.display.set_caption('Chess')

timer = pygame.time.Clock()

class Piece:
    value_of_pieces = {'King': 0, 'Pawn': 1, 'Knight': 3, 'Bishop': 3, 'Rook': 5, 'Queen': 9}
    image_of_white_pieces = {'King': 'pieces/w_king.png', 'Pawn': 'pieces/w_pawn.png', 'Knight': 'pieces/w_horse.png',
                             'Bishop': 'pieces/w_bishop.png', 'Rook': 'pieces/w_rook.png', 'Queen': 'pieces/w_queen.png'}
    image_of_black_pieces = {'King': 'pieces/b_king.png', 'Pawn': 'pieces/b_pawn.png', 'Knight': 'pieces/b_horse.png',
                             'Bishop': 'pieces/b_bishop.png', 'Rook': 'pieces/b_rook.png', 'Queen': 'pieces/b_queen.png'}
    def __init__(self, name: str, is_white: bool):
        self.name = name
        self.is_white = is_white
        self.value = self.value_of_pieces[name]
        self.image = self.image_of_white_pieces[name] if is_white else self.image_of_black_pieces[name]



white_pawn = Piece('Pawn', True)
black_pawn = Piece('Pawn', False)
white_knight = Piece('Knight', True)
black_knight = Piece('Knight', False)
white_bishop = Piece('Bishop', True)
black_bishop = Piece('Bishop', False)
white_queen = Piece('Queen', True)
black_queen = Piece('Queen', False)
white_king = Piece('King', True)
black_king = Piece('King', False)

def init_board() -> None:
    for i in range(8):
        for j in range(8):
            if (i+j) % 2 == 1:
                pygame.draw.rect(screen, (0, 0, 0), pygame.Rect((100 * i) + 100, (100 * j) + 50, 100, 100))
            else:
                pygame.draw.rect(screen, (255, 255, 255), pygame.Rect((100 * i) + 100, (100 * j) + 50, 100, 100))
            if i == 1:
                print(black_pawn.image)

running =  True
while running:
    timer.tick(60)
    screen.fill((128, 128, 128))
    init_board()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
pygame.quit()