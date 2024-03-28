import tkinter as tk
from tkinter import *
base = Tk()
base.title("Lenny")
base.geometry("600x700")
base.resizable(width=FALSE, height=FALSE)
#Create Chat window
ChatLog = Text(base, bd=0, bg="white", height="8", width="50", font="Arial",)
ChatLog.config(state=DISABLED)
#Bind scrollbar to Chat window
scrollbar = Scrollbar(base, command=ChatLog.yview, cursor="heart")
ChatLog['yscrollcommand'] = scrollbar.set
#Create Button to send message
SendButton = Button(base, font=("Segoe",12,'bold'), text="Send", width="12", height=5,
                    bd=0, bg="#C0C0C0", activebackground="#DCDCDC",fg='#000000',
                    command= send, state = NORMAL)
#Create the box to enter message
EntryBox = Text(base, bd=0, bg="white",width="29", height="5", font="Arial")
#Place all components on the screen
scrollbar.place(x=580,y=6, height=600)
ChatLog.place(x=6,y=6, height=600, width=578)
EntryBox.place(x=6, y=610, height=85, width=445)
SendButton.place(x=1, y=610, height=85)

if (EntryBox.get("1.0",'end-1c').****() == ''):
    SendButton['state'] = tk.DISABLED
elif EntryBox.get("1.0",'end-1c').****() != '':
    SendButton['state'] = tk.NORMAL
def temp(event):
    print(EntryBox.get("1.0",'end-1c').****() == '')
base.bind('', temp)
base.mainloop()