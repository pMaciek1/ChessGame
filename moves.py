from typing import List

def w_pawn(board_y: int, board_x: int, board: List[List[str]]):
    board[board_y-1][board_x] = 'mv'
    #allow to move one square forward
    #allow to move two squares forward if first move
    #allow to move diagonally if there is a piece

def b_pawn(board_y: int, board_x: int, board: List[List[str]]):
    board[board_y+1][board_x] = 'mv'
    #allow to move one square forward
    #allow to move two squares forward if first move
    #allow to move diagonally if there is a piece


def rook(board_y: int, board_x: int, board: List[List[str]]):
    for y in range(board_y+1, 8):
        print('1 loop')
        if not board[y][board_x] == ' ':
            break
        board[y][board_x] = 'mv'
    for y in range(board_y-1, -1, -1):
        print('2 loop')
        if not board[y][board_x] == ' ':
            break
        board[y][board_x] = 'mv'
    for x in range(board_x+1, 8):
        print('3 loop')
        if not board[board_y][x] == ' ':
            break
        board[board_y][x] = 'mv'
    for x in range(board_x-1, -1, -1):
        print('4 loop')
        if not board[board_y][x] == ' ':
            break
        board[board_y][x] = 'mv'

def bishop(board_y: int, board_x: int, board: List[List[str]]) -> List[List[str]]:
    pass

def knight(board_y: int, board_x: int, board: List[List[str]]) -> List[List[str]]:
    pass

def king(board_y: int, board_x: int, board: List[List[str]]) -> List[List[str]]:
    pass

def queen(board_y: int, board_x: int, board: List[List[str]]) -> List[List[str]]:
    #rook(square)
    #bishop(square)
    pass