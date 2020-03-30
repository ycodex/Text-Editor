from tkinter import filedialog as fd
from tkinter import *

filename= None
root=Tk("Editor")
text=Text(root)
text.grid()

def newfile():
    global fliename
    filename="Untitled"
    text.delete(0.0,END)
def saveas():
    global text
    t=text.get("1.0","end-1c")
    saveloc=fd.asksaveasfilename()
    file1=open(saveloc,"w+")
    file1.write(t)
    file1.close()
button=Button(root,text="Save",command=saveas)
button.grid()
root.mainloop()


