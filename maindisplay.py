import Tkinter
import time

window = Tkinter.Tk()
canvas = Tkinter.Canvas(window, height=800, width=1280)
canvas.pack()

dash = Tkinter.PhotoImage(file = "CenterCircle.gif")
image = canvas.create_image(640,400, image=dash)



for n in range(1,360):
    
    if n<181:
        arc = 240, 0, 1040, 800
        canvas.create_arc(arc, start = 181-n, extent = n-1, outline = 'blue', width = 8, tag='greenarc')
    else:
        arc = 640, 400, 1040, 800
        canvas.create_arc(arc, start = n-181, extent = 361-n, outline = 'blue', width = 8, tag='greenarc')
    
    
    canvas.update()
    #time.sleep(0.01)
    canvas.delete('greenarc')




window.mainloop() #this holds the window open
