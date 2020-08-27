# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
T = int(input())
for _ in range(T):    
    def creat_board():
        board = list()
        for i in range(8):
            board.append([])
            for j in range(8):
                board[i].append('.')
        return board
    
    
    def print_board(board):
        for i in board:
            print("".join(i))
            
    def poner_obtaculos(board, k):
        fila = k//8
        sobras = k%8
        if fila != 8:
            for i in range(sobras, 8):
                board[fila][i] = "X"
        if fila<7:
            for i in range(sobras+1):
                board[fila+1][i] = 'X'
        
        
        return board
    

    k = int(input())
    board = creat_board()
    board[0][0] = 'O'
    board = poner_obtaculos(board, k)
    
    print_board(board)

