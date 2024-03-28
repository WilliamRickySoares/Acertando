from tkinter import *

app = Tk()
app.geometry('540x500')
app.resizable(False, False)
fonte_letras = "Comic Sans"
tamanho_letras = 15
letras_sorteadas = []


def refresh_window():
    # Redraw the window
    app.update()
    # app.update_idletasks()
    print("Refresh completed.")


def adicionar_chute(letter):
    if letter not in letras_sorteadas:
        letras_sorteadas.append(letter)
    letras_sorteadas.sort()
    print(letras_sorteadas)
    refresh_window()


def letra(letter, fonte, tamanho, s, x, y, h, w):
    Button(app, text = letter, font = (fonte, tamanho), state = s,
           command = lambda: adicionar_chute(letter)).place(x = x, y = y, height = h, width = w)


# letraA = 1
# if letraA == 1:
#     Button(app, text = "A", font = ("Comic Sans", 15), command = lambda: adicionar_chute('A'), state = _state). \
#         place(x = 10, y = 410, height = 40, width = 40)

if "A" in letras_sorteadas:
    letra("A", fonte_letras, tamanho_letras, s = DISABLED, x = 10, y = 410, h = 40, w = 40)
    print("Sim")
else:
    letra("A", fonte_letras, tamanho_letras, s = ACTIVE, x = 10, y = 410, h = 40, w = 40)
    print("Não")


# letra("B", fonte_letras, tamanho_letras, x=50, y=410, h=40, w=40)

# Button(app, text = "B", font = ("Comic Sans", 15)).place(x = 50, y = 410, height = 40, width = 40)
# Button(app, text = "C", font = ("Comic Sans", 15)).place(x = 90, y = 410, height = 40, width = 40)
# Button(app, text = "D", font = ("Comic Sans", 15)).place(x = 130, y = 410, height = 40, width = 40)
# Button(app, text = "E", font = ("Comic Sans", 15)).place(x = 170, y = 410, height = 40, width = 40)
# Button(app, text = "F", font = ("Comic Sans", 15)).place(x = 210, y = 410, height = 40, width = 40)
# Button(app, text = "G", font = ("Comic Sans", 15)).place(x = 250, y = 410, height = 40, width = 40)
# Button(app, text = "H", font = ("Comic Sans", 15)).place(x = 290, y = 410, height = 40, width = 40)
# Button(app, text = "I", font = ("Comic Sans", 15)).place(x = 330, y = 410, height = 40, width = 40)
# Button(app, text = "J", font = ("Comic Sans", 15)).place(x = 370, y = 410, height = 40, width = 40)
# Button(app, text = "L", font = ("Comic Sans", 15)).place(x = 410, y = 410, height = 40, width = 40)
# Button(app, text = "K", font = ("Comic Sans", 15)).place(x = 450, y = 410, height = 40, width = 40)
# Button(app, text = "M", font = ("Comic Sans", 15)).place(x = 490, y = 410, height = 40, width = 40)
#
# Button(app, text = "N", font = ("Comic Sans", 15)).place(x = 10, y = 450, height = 40, width = 40)
# Button(app, text = "O", font = ("Comic Sans", 15)).place(x = 50, y = 450, height = 40, width = 40)
# Button(app, text = "P", font = ("Comic Sans", 15)).place(x = 90, y = 450, height = 40, width = 40)
# Button(app, text = "Q", font = ("Comic Sans", 15)).place(x = 130, y = 450, height = 40, width = 40)
# Button(app, text = "R", font = ("Comic Sans", 15)).place(x = 170, y = 450, height = 40, width = 40)
# Button(app, text = "S", font = ("Comic Sans", 15)).place(x = 210, y = 450, height = 40, width = 40)
# Button(app, text = "T", font = ("Comic Sans", 15)).place(x = 250, y = 450, height = 40, width = 40)
# Button(app, text = "U", font = ("Comic Sans", 15)).place(x = 290, y = 450, height = 40, width = 40)
# Button(app, text = "V", font = ("Comic Sans", 15)).place(x = 330, y = 450, height = 40, width = 40)
# Button(app, text = "W", font = ("Comic Sans", 15)).place(x = 370, y = 450, height = 40, width = 40)
# Button(app, text = "X", font = ("Comic Sans", 15)).place(x = 450, y = 450, height = 40, width = 40)
# Button(app, text = "Y", font = ("Comic Sans", 15)).place(x = 410, y = 450, height = 40, width = 40)
# Button(app, text = "Z", font = ("Comic Sans", 15)).place(x = 490, y = 450, height = 40, width = 40)

app.mainloop()
