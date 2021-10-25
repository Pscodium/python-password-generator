import tkinter as tk 
from tkinter import *
import random

color1 = '#ffffff' #branco
color2 = '#000000' #preto
color3 = '#9e34e5' #roxo
color4 = '#11eeb7' #verde
color5 = '#dedede' #cinza

#CRIADOR DE JANELAS
window = tk.Tk()
window.title('Gerador de Senhas')
window.geometry('300x300')
window.configure(bg=color1)
window.focus_force()


vLetters = IntVar()
vNums = IntVar()
vAlpha = IntVar()


# FUNÇÃO BOTÃO PRESSIONADO, AS CONDICIONAIS CHAMAM AS FUNÇÕES DAS SENHAS
def button_pressed():

    if vLetters.get() == 1:
        ps_letter()
    elif vNums.get() == 1:
        ps_num()    
    elif vAlpha.get() == 1:
        ps_alpha()


# FUNÇÃO GERADOR DE SENHA ALFABÉTICA
def ps_letter():


    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
        'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'z']

    first = random.choice(letters)
    password = (first.upper() + random.choice(letters) + random.choice(letters) + random.choice(letters) + random.choice(letters) + random.choice(letters)+random.choice(letters) + random.choice(letters))
    
    text_box = tk.Text(down_frame_window, height=1, width=10, padx=30, pady=3, bg=color5)
    text_box.insert(1.0, password)
    text_box.tag_configure("center", justify="center")
    text_box.tag_add("center", 1.0, "end")
    text_box.place(x=75,y=150)

   

# FUNÇÃO GERADOR DE SENHA NUMÉRICA
def ps_num():


    x = random.randint(111, 999)
    y = random.randint(1, 99)
    password = (str(x)+str(y)+str(x))


    text_box = tk.Text(down_frame_window, height=1, width=10, padx=30, pady=3, bg=color5)
    text_box.insert(1.0, password)
    text_box.tag_configure("center", justify="center")
    text_box.tag_add("center", 1.0, "end")
    text_box.place(x=75,y=150)



# FUNÇÃO GERADOR DE SENHA ALFANUMÉRICA
def ps_alpha():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
        'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'z']
    
    x = random.randint(111, 999)
    y = random.randint(1, 99)
    first = random.choice(letters)
    password = (first.upper() + random.choice(letters) + str(x) + random.choice(letters) + str(y) + random.choice(letters))

    text_box = tk.Text(down_frame_window, height=1, width=10, padx=30, pady=3, bg=color5)
    text_box.insert(1.0, password)
    text_box.tag_configure("center", justify="center")
    text_box.tag_add("center", 1.0, "end")
    text_box.place(x=75,y=150)



#DIVIDINDO A TELA EM DUAS WIDE FRAMES
up_frame_window = Frame(window, width=300, height=50, bg=color1, pady=0, padx=0, relief='flat')
up_frame_window.grid(row=0, column=0, sticky=NSEW)

down_frame_window = Frame(window, width=300, height=250, bg=color1, pady=0, padx=0, relief='flat')
down_frame_window.grid(row=1, column=0, sticky=NSEW)


# FRAME DE CIMA
#TITULO DENTRO DA JANELA
app_name = Label(up_frame_window, text='Gerador de Senhas', width=23, height=1, padx=0, relief='flat', anchor='center', font=('Raleway 16 bold'), bg=color1, fg=color2)
app_name.place(x=0, y=0)

app_line = Label(up_frame_window, text='', width=400, height=1, padx=0, relief='flat', anchor='center', font=('Raleway 1'), bg=color3, fg=color2)
app_line.place(x=0, y=35)

#SENHA LETRAS
leters_line = Label(down_frame_window, text='Senha com Letras', height=1, padx=0, relief='flat', anchor='center', font=('Raleway 10 bold'), bg=color1, fg=color2)
leters_line.grid(row=0, column=0, sticky=NSEW, pady=10, padx=3)

letters_input =Checkbutton(down_frame_window,text='',variable=vLetters, onvalue=1, offvalue=0, bg=color1, activebackground=color1)
letters_input.grid(row=0, column=2, sticky=NSEW, pady=10, padx=3)

#SENHA NÚMEROS
num_line = Label(down_frame_window, text='Senha com Números', height=1, padx=0, relief='flat', anchor='center', font=('Raleway 10 bold'), bg=color1, fg=color2)
num_line.grid(row=1, column=0, sticky=NSEW, pady=10, padx=3)

num_input =Checkbutton(down_frame_window,text='',variable=vNums, onvalue=1, offvalue=0, bg=color1, activebackground=color1)
num_input.grid(row=1, column=2, sticky=NSEW, pady=10, padx=3)


#SENHA NÚMEROS
num_line = Label(down_frame_window, text='Senha Alfanumérica', height=1, padx=0, relief='flat', anchor='center', font=('Raleway 10 bold'), bg=color1, fg=color2)
num_line.grid(row=2, column=0, sticky=NSEW, pady=10, padx=3)

num_input =Checkbutton(down_frame_window,text='',variable=vAlpha, onvalue=1, offvalue=0, bg=color1, activebackground=color1)
num_input.grid(row=2, column=2, sticky=NSEW, pady=10, padx=3)



#RESULTADO
result_button = Button(down_frame_window, text='Gerar Senha', width=34, height=2, command=button_pressed, overrelief=SOLID, relief='raised', border=0, anchor='center', font=('Raleway 10 bold'), bg=color3, fg=color1)
result_button.grid(row=4, column=0, sticky=NSEW, pady=70, padx=10, columnspan=60)



#INICIA A TELA EM LOOP
window.mainloop()