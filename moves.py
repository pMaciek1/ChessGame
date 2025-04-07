from typing import List

def w_pawn(board_y: int, board_x: int, board: List[List[str]]):
    try:
        # allow to move two squares forward if first move - done
        # allow to move one square forward - done
        if board[board_y-1][board_x] == ' ':
            board[board_y-1][board_x] = 'mv'
            if board_y == 6 and board[board_y-2][board_x] == ' ':
                board[board_y - 2][board_x] = 'mv'
        #allow to move diagonally if there is a piece
        if not board[board_y-1][board_x-1] == ' ':
            board[board_y - 1][board_x - 1] = 'mv'
        if not board[board_y-1][board_x+1] == ' ':
            board[board_y - 1][board_x + 1] = 'mv'
    except IndexError:
        pass

def b_pawn(board_y: int, board_x: int, board: List[List[str]]):
    try:
        if board[board_y + 1][board_x] == ' ':
            board[board_y + 1][board_x] = 'mv'
            if board_y == 1 and board[board_y + 2][board_x] == ' ':
                board[board_y + 2][board_x] = 'mv'
        if not board[board_y + 1][board_x - 1] == ' ':
            board[board_y + 1][board_x - 1] = 'mv'
        if not board[board_y + 1][board_x + 1] == ' ':
            board[board_y + 1][board_x + 1] = 'mv'
    except IndexError:
        pass


def rook(board_y: int, board_x: int, board: List[List[str]]):
    for y in range(board_y+1, 8):
        if not board[y][board_x] == ' ':
            break
        board[y][board_x] = 'mv'
    for y in range(board_y-1, -1, -1):
        if not board[y][board_x] == ' ':
            break
        board[y][board_x] = 'mv'
    for x in range(board_x+1, 8):
        if not board[board_y][x] == ' ':
            break
        board[board_y][x] = 'mv'
    for x in range(board_x-1, -1, -1):
        if not board[board_y][x] == ' ':
            break
        board[board_y][x] = 'mv'

def bishop(board_y: int, board_x: int, board: List[List[str]]) -> None:
    for x in range(max(board_y, board_x)+1, 8):
        if not board[x][x] == ' ':
            break
        board[x][x] = 'mv'
    for x in range(min(board_y, board_x) -1, -1, -1):
        if not board[x][x] == ' ':
            break
        board[x][x] = 'mv'
    #todo add two more diagonals

def knight(board_y: int, board_x: int, board: List[List[str]]) -> List[List[str]]:
    pass

def king(board_y: int, board_x: int, board: List[List[str]]) -> List[List[str]]:
    pass

def queen(board_y: int, board_x: int, board: List[List[str]]) -> List[List[str]]:
    #rook(square)
    #bishop(square)
    pass