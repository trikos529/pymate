from tkinter import *

class UI:
    def __init__(self, bg_colour, text_colour, btn_colour, 
                 btn_size, btn_active_colour, win_width, win_height,
                   font, font_size, sidebar_bg,
                    sidebar_width_percent):
        self.win_height = win_height
        self.win_width = win_width
        self.win_size = self.win_width + "x" + self.win_height
        self.text_colour = text_colour
        self.btn_colour = btn_colour
        self.btn_size = btn_size
        self.btn_active_colour = btn_active_colour
        self.bg_colour = bg_colour
        self.font = font
        self.fontsize = font_size 
        self.sidebar_bg = sidebar_bg
        self.sidebar_width = (win_width / 100) * sidebar_width_percent
        self.btn_width = (self.sidebar_width/100) * btn_size 
        self.win = Tk()
        self.win.geometry(self.win_size) 
        self.win.title("Open Action Reciever")
        self.win.resizable(width=False, height=FALSE)
        #self.logo = PhotoImage()               #logo to be made
        #self.win.iconphoto(True, logo)
        self.win.config(background=bg_colour)
        self.sidebar_draw()
        self.actions_tab()
        self.win.mainloop()
        
    def clear_content(self):    #helper called from any drawing func
        for widget in self.content_frame.winfo_children():
            widget.destroy()
    
    def sidebar_draw(self):    
        self.sidebar = Frame(self.win,bg=self.sidebar_bg, width=self.sidebar_width, height=self.win_height)
        Button(self.sidebar,text="Actions", font=(self.font,self.fontsize),
                relief=RAISED, active_background=self.btn_active_colour, command=self.actions_tab).pack
        Button(self.sidebar,text="Intergrations", font=(self.font,self.fontsize),
                relief=RAISED, active_background=self.btn_active_colour, command=self.intergrations_tab).pack
        Button(self.sidebar,text="Connect", font=(self.font,self.fontsize),
                relief=RAISED, active_background=self.btn_active_colour, command=self.connect_tab).pack
        Button(self.sidebar,text="Settings", font=(self.font,self.fontsize),
                relief=RAISED,active_background=self.btn_active_colour, command=self.settings_tab).pack

    def actions_tab():
        ...
    
    def intergrations_tab():
        ...
    
    def connect_tab():
        ...
    
    def settings_tab():
        ...