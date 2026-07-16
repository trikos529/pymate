from tkinter import *

class UI:
    bg_colour = "#ffffff" #default colour dialog to change 
    text_colour ="#000000"#default text colour
    btn_colour  ="#919191"#default btn/wigdeat area
    win_width ="800" #can be read from json config which can be placed in %apdata% 
    win_height ="600"#can be read from json config which can be placed in %apdata% 
    win_sieze = win_width + "x" + win_height

    # Create Window
    win = Tk()
    win.geometry(win_sieze) #we can read it from json config 
    win.title("Open Action Reciever")
    win.resizable(width=False,height=FALSE)
    #logo = PhotoImage()               #logo to be made
    #win.iconphoto(True, logo)
    win.config(background=bg_colour)
    

    win.mainloop()