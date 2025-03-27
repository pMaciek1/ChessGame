import pygame

pygame.init()

screen = pygame.display.set_mode([1000, 900])
pygame.display.set_caption('Chess')

timer = pygame.time.Clock()

class Piece:
    value_of_pieces = {'King': 0, 'Pawn': 1, 'Knight': 3, 'Bishop': 3, 'Rook': 5, 'Queen': 9}
    def __init__(self, name: str, is_white: bool) -> None:
        self.name = name
        self.is_white = is_white
        self.value = self.value_of_pieces[name]


running =  True
while running:
    timer.tick(60)
    screen.fill('gray')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
pygame.quit()