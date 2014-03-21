from tkinter import *
import random
import time

class Ball: 
    def __init__( self, canvas, paddle, color ):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval( 10,10, 25,25, fill = color )
        self.canvas.move( self.id, 245, 100 )
        starts = [ -3, -2, -1, 1, 2, 3 ]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_buttom = False
        self.score = 0
    def hit_paddle( self, pos ):
        paddle_pos = self.canvas.coords( self.paddle.id )
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
        else:
            return False
    def draw(self):
        self.canvas.move( self.id, self.x, self.y )
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= self.canvas_height:
            self.hit_buttom = True
        if self.hit_paddle(pos):
            self.y = -3
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3
            
class Paddle: 
    def __init__( self, canvas, color ):
        self.canvas = canvas
        self.id = canvas.create_rectangle( 0,0, 100,10, fill = color )
        self.canvas.move( self.id, 200, 300 )
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all( '<KeyPress-Left>', self.turn_left )
        self.canvas.bind_all( '<KeyPress-Right>', self.turn_right )
    def draw(self):
        self.canvas.move( self.id, self.x, 0 )
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0
    def turn_left( self, evt ):
        self.x = -2
    def turn_right( self, evt ):
        self.x = 2
  
def game_start(evt):
    canvas.itemconfig( txt_click_to_start, state = 'hidden' )
    while True:
        if not ball.hit_buttom:
            ball.draw()
            paddle.draw()
        else:
            canvas.itemconfig( txt_false, state = 'normal' )
        tk.update_idletasks()
        tk.update()
        time.sleep(0.01)

tk = Tk()
tk.title("Game")
tk.resizable(0,0)
tk.wm_attributes("-topmost",1)
canvas = Canvas( tk, width = 500, height = 400, bd = 0, highlightthickness = 0 )
canvas.pack()
'''
btn = Button( tk, text = "play again", command = game_start, state = 'hidden' )
btn.pack'''
txt_false = canvas.create_text(
    250, 100,
    text = 'False!!',
    font = ('Courier',30),
    state = 'hidden',
    fill = 'red' )
txt_click_to_start = canvas.create_text(
    250, 50,
    text = 'to click to start the game',
    font = ('Courier',10),
    state = 'normal',
    fill = 'blue' )
tk.update()
paddle = Paddle( canvas, 'blue' )
ball = Ball( canvas, paddle, 'red' )
canvas.bind_all( '<Button-1>', game_start )

game_start()
