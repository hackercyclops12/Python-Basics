BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

import tkinter as tk

root= tk.Tk()
root.title("Txt2bin - converter")
canvas1 = tk.Canvas(root, width = 400, height = 300,  relief = 'raised')
canvas1.pack()

label1 = tk.Label(root, text='Convert text to binary')
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=label1)

label2 = tk.Label(root, text='Enter text to convert to binary:')
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 100, window=label2)

entry1 = tk.Entry(root) 
canvas1.create_window(200, 140, window=entry1)

def getSquareRoot (): 
    conversion = entry1.get()  
    label3 = tk.Label(root, text= 'The binary version of ' + conversion + ' is:',font=('helvetica', 10))
    canvas1.create_window(200, 210, window=label3)
    answer = (' '.join(format(ord(x), 'b') for x in conversion))
    label4 = tk.Label(root, text = answer,font=('helvetica', 10, 'bold'))
    canvas1.create_window(200, 230, window=label4)   
button1 = tk.Button(text='Convert to binary', command=getSquareRoot, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 180, window=button1)

root.mainloop()

#algo   
