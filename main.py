import tkinter as tk
from PIL import Image, ImageTk
from pieces import *
from game import *

window = tk.Tk()
window.title('Chess')
window.geometry('1000x1000')
window.configure(bg='#2A3033')

board_canvas = tk.Canvas(window, bg='#2A3033', highlightthickness=0, width=800, height=800)
board_canvas.place(anchor='c', relx=.5, rely=.5)
board_img = tk.PhotoImage(file='img/board.png')
board_canvas.create_image(400, 400, image=board_img)

p1_r_img = tk.PhotoImage(file='img/rook_white.png')
p1_r1 = board_canvas.create_image(50, 750, image=p1_r_img)

p1_kn_img = tk.PhotoImage(file='img/knight_white.png')
p1_kn1 = board_canvas.create_image(150, 750, image=p1_kn_img)

p1_b_img = tk.PhotoImage(file='img/bishop_white.png')
p1_b1 = board_canvas.create_image(250, 750, image=p1_b_img)

p1_q_img = tk.PhotoImage(file='img/queen_white.png')
p1_q = board_canvas.create_image(350, 750, image=p1_q_img)

p1_ki_img = tk.PhotoImage(file='img/king_white.png')
p1_ki = board_canvas.create_image(450, 750, image=p1_ki_img)

p1_b2 = board_canvas.create_image(550, 750, image=p1_b_img)

p1_kn2 = board_canvas.create_image(650, 750, image=p1_kn_img)

p1_r2 = board_canvas.create_image(750, 750, image=p1_r_img)

p1_p_img = tk.PhotoImage(file='img/pawn_white.png')
p1_p1 = board_canvas.create_image(50, 650, image=p1_p_img)
p1_p2 = board_canvas.create_image(150, 650, image=p1_p_img)
p1_p3 = board_canvas.create_image(250, 650, image=p1_p_img)
p1_p4 = board_canvas.create_image(350, 650, image=p1_p_img)
p1_p5 = board_canvas.create_image(450, 650, image=p1_p_img)
p1_p6 = board_canvas.create_image(550, 650, image=p1_p_img)
p1_p7 = board_canvas.create_image(650, 650, image=p1_p_img)
p1_p8 = board_canvas.create_image(750, 650, image=p1_p_img)

p2_r_img = tk.PhotoImage(file='img/rook_black.png')
p2_r1 = board_canvas.create_image(50, 50, image=p2_r_img)

p2_kn_img = tk.PhotoImage(file='img/knight_black.png')
p2_kn1 = board_canvas.create_image(150, 50, image=p2_kn_img)

p2_b_img = tk.PhotoImage(file='img/bishop_black.png')
p2_b1 = board_canvas.create_image(250, 50, image=p2_b_img)

p2_q_img = tk.PhotoImage(file='img/queen_black.png')
p2_q = board_canvas.create_image(350, 50, image=p2_q_img)

p2_ki_img = tk.PhotoImage(file='img/king_black.png')
p2_ki = board_canvas.create_image(450, 50, image=p2_ki_img)

p2_b2 = board_canvas.create_image(550, 50, image=p2_b_img)

p2_kn2 = board_canvas.create_image(650, 50, image=p2_kn_img)

p2_r2 = board_canvas.create_image(750, 50, image=p2_r_img)

p2_p_img = tk.PhotoImage(file='img/pawn_black.png')
p2_p1 = board_canvas.create_image(50, 150, image=p2_p_img)
p2_p2 = board_canvas.create_image(150, 150, image=p2_p_img)
p2_p3 = board_canvas.create_image(250, 150, image=p2_p_img)
p2_p4 = board_canvas.create_image(350, 150, image=p2_p_img)
p2_p5 = board_canvas.create_image(450, 150, image=p2_p_img)
p2_p6 = board_canvas.create_image(550, 150, image=p2_p_img)
p2_p7 = board_canvas.create_image(650, 150, image=p2_p_img)
p2_p8 = board_canvas.create_image(750, 150, image=p2_p_img)

p1_piece_list = [p1_r1, p1_r2, p1_kn1, p1_kn2, p1_b1, p1_b2, p1_q, p1_ki, p1_p1, p1_p2, p1_p3, p1_p4, p1_p5, p1_p6, p1_p7, p1_p8]
p2_piece_list = [p2_r1, p2_r2, p2_kn1, p2_kn2, p2_b1, p2_b2, p2_q, p2_ki, p2_p1, p2_p2, p2_p3, p2_p4, p2_p5, p2_p6, p2_p7, p2_p8]

board_widgets = [[p1_r1, p1_kn1, p1_b1, p1_q, p1_ki, p1_b2, p1_kn2, p1_r2],
                 [p1_p1, p1_p2, p1_p3, p1_p4, p1_p5, p1_p6, p1_p7, p1_p8],
                 ['', '', '', '', '', '', '', ''],
                 ['', '', '', '', '', '', '', ''],
                 ['', '', '', '', '', '', '', ''],
                 ['', '', '', '', '', '', '', ''],
                 [p2_p1, p2_p2, p2_p3, p2_p4, p2_p5, p2_p6, p2_p7, p2_p8],
                 [p2_r1, p2_kn1, p2_b1, p2_q, p2_ki, p2_b2, p2_kn2, p2_r2]]

game = Game()

def isValidCol(c):
    return c >= 97 and c <= 104 or c >= 65 and c <= 72

def isValidRow(c):
    return c >= 49 and c <= 56

def charToCoordinate(c1, c2):
    if c1 >= 97:
        return c2 - 49, c1 - 97
    else:
        return c2 - 49, c1 - 65
    

def evaluate(e):
    entry = move_entry.get()
    move_entry.delete(0, 'end')

    if len(entry) != 4:
        print('TODO: error message')
    else:
        c1, c2, c3, c4 = ord(entry[0]), ord(entry[1]), ord(entry[2]), ord(entry[3])
        if isValidCol(c1) and isValidRow(c2) and isValidCol(c3) and isValidRow(c4):
            i, j = charToCoordinate(c1, c2)
            destY, destX = charToCoordinate(c3, c4)
            print(j, i, destX, destY)
            print(board[i][j])
            print(board[destY][destX])
            if game.getTurn() == 0 and board_widgets[i][j] in p1_piece_list or game.getTurn() == 1 and board_widgets[i][j] in p2_piece_list:
                if board[i][j].move(destX, destY):
                    if board_widgets[destY][destX] != '':
                        board_canvas.delete(board_widgets[destY][destX])

                    board_widgets[destY][destX] = board_widgets[i][j]
                    board_widgets[i][j] = ''

                    board_canvas.move(board_widgets[destY][destX], (destX - j) * 100, -(destY - i) * 100)

                    game.changeTurn()
                else:
                    print('Invalid move')
            else:
                print('It is player ' + str(game.getTurn()) + '\'s turn')

move_entry = tk.Entry(window, bg='#1F2120', fg='white', highlightthickness=0)
move_entry.bind('<Return>', evaluate)
move_entry.place(anchor='c', relx=.5, rely = .96)

window.mainloop()

