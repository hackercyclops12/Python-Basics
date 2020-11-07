import tkinter as tk
import hashlib

root= tk.Tk()
root.title(' smHASHer - Text 2 MD5 converter')
canvas1 = tk.Canvas(root, width = 400, height = 300,  relief = 'raised')
canvas1.pack()

label1 = tk.Label(root, text='Encrypt to MD5')
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=label1)

label2 = tk.Label(root, text='What would you like to convert to MD5?')
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 100, window=label2)

entry1 = tk.Entry (root) 
canvas1.create_window(200, 140, window=entry1)

def getSquareRoot ():
    
    x1 = entry1.get()
    
    label3 = tk.Label(root, text= 'The MD5 equivilent of ' + x1 + ' is:',font=('helvetica', 10))
    canvas1.create_window(200, 210, window=label3)
    
    result = hashlib.md5(x1.encode())   
    x2 = result.hexdigest()
    
    label4 = tk.Label(root, text= x2 ,font=('helvetica', 10, 'bold'))
    canvas1.create_window(200, 230, window=label4)
    
button1 = tk.Button(text='Convert to MD5', command=getSquareRoot, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 180, window=button1)

root.mainloop()