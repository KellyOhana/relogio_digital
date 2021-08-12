from tkinter import *
import pyttsx3
import tkinter.font as tkFont
from datetime import datetime
# import pyglet

# pyglet.font.add_file('alarm clock.ttf')

Diasemana = ('segunda feira', 'terceira feira', 'quarta feira',
             'quinta feira', 'sexta feira', 'sabado', 'domingo')
Meses = ('janeiro', 'fevereiro', 'mar', 'abril', 'maio', 'junho',
         'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro')


cores = ("#3d3d3d", "#fafcff", "#21c25c", "#eb463b", "#808080", "#3080f0")

fundo = cores[5]
cor = cores[1]
i = 0
j = 0


def troca_cores():
    global i
    fundo = cores[i]
    if i < 5:
        i += 1
    else:
        i = 0
    janela.configure(background=fundo)
    l1.configure(bg=fundo)
    l2.configure(bg=fundo)


def troca_num():
    global j
    cor = cores[j]
    if j < 5:
        j += 1
    else:
        j = 0
    l1.configure(fg=cor)
    l2.configure(fg=cor)


def fala():
    tempolido = datetime.now()
    horalida = tempolido.strftime("%H:%M")
    dia_semana = datetime.today().weekday()
    dia = tempolido.day
    mes = tempolido.month - 1
    engine = pyttsx3.init()
    engine.say(horalida)
    engine.say(Diasemana[dia_semana] + str(dia) + " de " + Meses[mes])
    engine.runAndWait()


def aumenta_tamanho():
    fontsize = fontStyle['size']
    fontStyle.configure(size=fontsize + 2)
    fontsize2 = fontStyle2['size']
    fontStyle2.configure(size=fontsize2 + 2)


def dimunui_tamanho():
    fontsize = fontStyle['size']
    fontStyle.configure(size=fontsize - 2)
    fontsize2 = fontStyle2['size']
    fontStyle2.configure(size=fontsize2 - 2)


janela = Tk()
janela.title("Relógio")
# janela.geometry('450x200')
# janela.resizable(width=FALSE, height=FALSE)
janela.configure(background=fundo)


def relogio():
    tempo = datetime.now()
    hora = tempo.strftime("%H:%M:%S")
    dia_semana = datetime.today().weekday()
    dia = tempo.day
    mes = tempo.month - 1

    ano = tempo.strftime("%Y")

    l1.config(text=hora)
    l1.after(200, relogio)
    l2.config(text=Diasemana[dia_semana] + "   " + str(dia) + "/" + Meses[mes] + "/" + ano)


# botoes
botao = Button(janela, text="Trocar fundo", command=troca_cores)
botao.grid(row=3, column=0, sticky=NW, padx=5, pady=5)

botao_num = Button(janela, text="Trocar numero", command=troca_num)
botao_num.grid(row=3, column=0, sticky=NW, padx=90, pady=5)

botaofala = Button(janela, text="Falar", command=fala)
botaofala.grid(row=3, column=0, pady=5)

botaoaumenta = Button(janela, text=" + ", command=aumenta_tamanho)
botaoaumenta.grid(row=3, column=0, sticky=NE, padx=30, pady=5)

botaodimi = Button(janela, text=" - ", command=dimunui_tamanho)
botaodimi.grid(row=3, column=0, sticky=NE, padx=5, pady=5)

fontStyle = tkFont.Font(family="times", size=80)
fontStyle2 = tkFont.Font(family="times", size=20)
l1 = Label(janela, text="00:00:00", font=fontStyle, bg=fundo, fg=cor)
l1.grid(row=0, column=0, sticky=NW, padx=5)
l2 = Label(janela, font=fontStyle2, bg=fundo, fg=cor)
l2.grid(row=1, column=0, sticky=NW, padx=5)


# executando
relogio()
janela.mainloop()
