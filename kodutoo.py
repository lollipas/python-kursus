from tkinter import *

aken = Tk()

k= Canvas(aken, width=500, height=500, bg='blue')
k.pack()   

k.create_rectangle((50, 500), (350, 280), fill = 'gray')
k.create_rectangle((100, 500), (200, 330), fill = 'lightgray')
k.create_rectangle((100, 500), (150,250), fill = 'yellow')

k.mainloop()
