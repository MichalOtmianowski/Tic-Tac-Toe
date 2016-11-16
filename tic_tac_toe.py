"""
Witamy ;-)
Twoim zadaniem jest napisanie funkcji,
która na podstawie informacji o planszy
obliczy bieżący stan gry "kółko i krzyżyk".
Nie chcemy stworzyć całej gry!
Napisaną funkcję będzie można wykorzystać podczas gry do sprawdzania:
  czy ktoś wygrał
  czy nikt nie wygrał
  czy mamy remis
Powodzenia!
"""


def state(board):
    """Funkcja sprawdzająca stan gry w 'kółko i krzyżyk'.
    Wejście:
      board
        Lista ciągów znaków reprezentujących planszę.
        Dozwolone znaki:
          '.' - niezajęte pole
          'X' - pole zajęte przez gracza X
          'O' - pole zajęte przez gracza O
        Przykład:
          board = [
              'XO.",
              '.0X',
              '.X.',
          ]
    Wyjście:
      '.' jeśli nikt nie wygrywa
      'X' jeśli X wygrywa
      'Y' jeśli Y wygrywa
      'XY' jeśli jest remis
    Zadania dodatkowe:
      Zwróć False jeśli plansza jest niepoprawna (nie jest kwadratowa).
      Napisz funkcję tak by działała niezależnie od rozmiaru planszy.
    """
    
    new_board=[]
    for row in board:
        if len(row)!=len(board):
            return False
            
    for row in board:
        row_new=[]
        for element in row:
            if element=='X':
                row_new.append(1)
            elif element=='O':
                row_new.append(-1)
            else:
                row_new.append(0)

        new_board.append(row_new)

    for row in new_board:
        if sum(row)==len(new_board):
            return 'X'
        elif sum(row)==len(new_board):
            return 'O'
            
    cols=[0]*len(new_board)

    for row_index, row in enumerate(new_board):
        for col_index, column in enumerate(row):
            cols[col_index]+=column
            
    
    for element in cols:
        if element==len(new_board):
            return 'X'
        elif element==-len(new_board):
            return 'O'
            
    diag=[0,0]
    
    for row_index, row in enumerate(new_board):
        for col_index, column in enumerate(row):
            if row_index==col_index:
                diag[0]+=column
                diag[1]+=new_board[row_index][-col_index+1]

        
    for element in diag:
        if element==len(new_board):
            return 'X'
        elif element==-len(new_board):
            return 'O'
    zeros=0
    for row in new_board:
        if 0 in row:
           zeros+=1 
        
    if zeros==0:
        return 'XY'
    return '.'
