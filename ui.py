from tkinter import *

class UI:
    def __init__(self, bg_colour,text_colour,btn_colour,win_width,win_height,font):  #constructor pass json file path as argument to extract values 
        self.win_sieze = win_width + "x" + win_height
        self.text_colour = text_colour
        self.btn_colour = btn_colour
        self.bg_colour = bg_colour
        self.font = font 
        self.win = Tk()
        self.win.geometry(self.win_sieze) 
        self.win.title("Open Action Reciever")
        self.win.resizable(width=False,height=FALSE)
        #self.logo = PhotoImage()               #logo to be made
        #self.win.iconphoto(True, logo)
        self.win.config(background=bg_colour)
        UI.sidebar_draw()
    
        self.win.mainloop()
        
    def clear_content(self):    #helper caled froam any drawing func
        for widget in self.content_frame.winfo_children():
            widget.destroy()
    def sidebar_draw(self):
        
        ...