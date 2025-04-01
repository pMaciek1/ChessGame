import pygame
import moves

pygame.init()

screen = pygame.display.set_mode([1000, 900])
pygame.display.set_caption('Chess')

timer = pygame.time.Clock()


board = [[' ' for _ in range(8)] for _ in range(8)]



bp_img = pygame.image.load('pieces/black-pawn.png').convert_alpha()
wp_img = pygame.image.load('pieces/white-pawn.png').convert_alpha()
br_img = pygame.image.load('pieces/black-rook.png').convert_alpha()
wr_img = pygame.image.load('pieces/white-rook.png').convert_alpha()
bb_img = pygame.image.load('pieces/black-bishop.png').convert_alpha()
wb_img = pygame.image.load('pieces/white-bishop.png').convert_alpha()
bq_img = pygame.image.load('pieces/black-queen.png').convert_alpha()
wq_img = pygame.image.load('pieces/white-queen.png').convert_alpha()
bn_img = pygame.image.load('pieces/black-knight.png').convert_alpha()
wn_img = pygame.image.load('pieces/white-knight.png').convert_alpha()
bk_img = pygame.image.load('pieces/black-king.png').convert_alpha()
wk_img = pygame.image.load('pieces/white-king.png').convert_alpha()


def init_board() -> None:
    for i in range(8):
        board[1][i] = 'bp'
        board[6][i] = 'wp'
    board[0][0] = 'br'
    board[0][7] = 'br'
    board[0][1] = 'bn'
    board[0][6] = 'bn'
    board[0][2] = 'bb'
    board[0][5] = 'bb'
    board[0][3] = 'bq'
    board[0][4] = 'bk'

    board[7][0] = 'wr'
    board[7][7] = 'wr'
    board[7][1] = 'wn'
    board[7][6] = 'wn'
    board[7][2] = 'wb'
    board[7][5] = 'wb'
    board[7][3] = 'wq'
    board[7][4] = 'wk'
    board[4][4] = 'wr'

def draw_board() -> None:
    for i in range(8):
        for j in range(8):
            if (i+j) % 2 == 1:
                pygame.draw.rect(screen, (55, 55, 55), pygame.Rect((100 * i) + 100, (100 * j) + 50, 100, 100))
            else:
                pygame.draw.rect(screen, (200, 200, 200), pygame.Rect((100 * i) + 100, (100 * j) + 50, 100, 100))
    for line_index, line in enumerate(board):
        for square_index, square in enumerate(line):
            if square == 'bp':
                screen.blit(bp_img, ((100 * square_index) + 100, (100 * line_index) + 50))
            elif square == 'wp':
                screen.blit(wp_img, ((100 * square_index) + 100, (100 * line_index) + 50))
            elif square == 'br':
                screen.blit(br_img, ((100 * square_index) + 100, (100 * line_index) + 50))
            elif square == 'wr':
                screen.blit(wr_img, ((100 * square_index) + 100, (100 * line_index) + 50))
            elif square == 'bn':
                screen.blit(bn_img, ((100 * square_index) + 100, (100 * line_index) + 50))
            elif square == 'wn':
                screen.blit(wn_img, ((100 * square_index) + 100, (100 * line_index) + 50))
            elif square == 'bb':
                screen.blit(bb_img, ((100 * square_index) + 100, (100 * line_index) + 50))
            elif square == 'wb':
                screen.blit(wb_img, ((100 * square_index) + 100, (100 * line_index) + 50))
            elif square == 'bq':
                screen.blit(bq_img, ((100 * square_index) + 100, (100 * line_index) + 50))
            elif square == 'wq':
                screen.blit(wq_img, ((100 * square_index) + 100, (100 * line_index) + 50))
            elif square == 'bk':
                screen.blit(bk_img, ((100 * square_index) + 100, (100 * line_index) + 50))
            elif square == 'wk':
                screen.blit(wk_img, ((100 * square_index) + 100, (100 * line_index) + 50))
            elif square == 'mv':
                pygame.draw.circle(screen, (255, 0, 0), ((100 * square_index) + 150, (100 * line_index) + 100), 10)

def choose_piece(pos_x: float, pos_y:float, is_white: bool) -> str:
    try:
        buf = board[int((pos_y-50)/100)][int((pos_x-100)/100)]
        print(f'x: {[int((pos_y-50)/100)]}, y: {[int((pos_x-100)/100)]}')
    except IndexError:
        buf = ' '
    if is_white and buf.find('w') == 0:
        if buf == 'wp':
            moves.w_pawn(int((pos_y-50)/100), int((pos_x-100)/100), board)
        elif buf == 'wr':
            moves.rook(int((pos_y-50)/100), int((pos_x-100)/100), board)
        return buf
    elif not is_white and buf.find('b') == 0:
        if buf == 'bp':
            moves.b_pawn(int((pos_y-50)/100), int((pos_x-100)/100), board)
        return buf
    else:
        return ''

def drop_piece(pos_x: float, pos_y: float, old_x: float, old_y: float, piece: str) -> bool:
    if board[int((pos_y - 50) / 100)][int((pos_x - 100) / 100)] == 'mv':
        board[int((old_y - 50) / 100)][int((old_x - 100) / 100)] = ' '
        board[int((pos_y - 50) / 100)][int((pos_x - 100) / 100)] = piece
        for line_index, line in enumerate(board):
            for square_index, square in enumerate(line):
                if square == 'mv':
                    board[line_index][square_index] = ''
        return True
    return False


init_board()

running =  True
move = False
is_white_turn = True
is_legal_move = False


while running:
    timer.tick(60)
    screen.fill((128, 128, 128))
    draw_board()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            print(f'x: {x}, y: {y}')
            if not move:
                pick_up_piece = choose_piece(x, y, is_white_turn)
                if not pick_up_piece == '':
                    print('picked up piece')
                    xx = x
                    yy = y
                    move = not move
            else:
                is_legal_move = drop_piece(x, y, xx, yy, pick_up_piece)
                print('trying to drop piece, is legal move?' + str(is_legal_move))
                if is_legal_move:
                    print('legal move')
                    is_white_turn = not is_white_turn
                    move = not move
    pygame.display.flip()
pygame.quit()