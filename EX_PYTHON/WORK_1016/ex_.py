from tkinter import *
# import main_code



window = Tk()
window.title("**Equal Grid**")
window.geometry("800x800")
window.resizable(False,False)
ROWS = 4
COLS = 4


def make_equal_grid(parent, rows, cols):
    # 모든 행/열을 동일 비율로
    for r in range(rows):
        parent.grid_rowconfigure(r, weight=1, uniform="row")
    for c in range(cols):
        parent.grid_columnconfigure(c, weight=1, uniform="col")

make_equal_grid(window, ROWS, COLS)

def GAME_1(event):
    print(event)


BTN = Button(window,text="경찰과 도둑",fg = "yellow",bg="black")
BTN.grid(row=0,column=0,columnspan=4,sticky="nsew")

BTN.bind("<Button-1>",GAME_1)
window.mainloop()