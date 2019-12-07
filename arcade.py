from tkinter import *
import Pong
import Snake


class GameWindow(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, bg = 'brown')
        self.parent = parent

        self.pack(fill=BOTH, expand=1)

        self.title_box = Label(self, width = 50, font = ('Helvetica', 30),
                               bg = 'light grey', relief = 'sunken',
                               text = 'The End Racism Arcade')
        self.game1 = Button(self, text = 'Pong', command = Pong.main,
                            width = 10, bg = 'dark grey', relief = 'raised',
                            font = ('Helvetica', 30))
        self.game2 = Button(self, text = 'Snake', command = Snake.main,
                            width = 10, bg = 'dark grey', relief = 'raised',
                            font = ('Helvetica', 30))
        self.title_box.pack()
        self.game1.pack()
        self.game2.pack()


master = Tk()
master.title('ARCADE')
master.geometry("500x500+100+100")
game = GameWindow(master)