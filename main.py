from tkinter import *
from pytube import YouTube
from tkinter import filedialog
from pytube.exceptions import RegexMatchError

janela = Tk()
janela.title('Download YouTube.com')

def  download(link_):
    if link_:
        try:
            pasta = filedialog.askopenfilename()
            YouTube(link_).streams.get_highest_resolution().download(pasta)
            alerta()
        except RegexMatchError:
            erro()
    else:
        erro()


def alerta():
    janela_msg = Toplevel()
    janela_msg.title('Aviso')
    janela_msg.geometry('600x400')

    Label(janela_msg, text='Dowload concluido com sucesso!!', font='arial 12', pady=30).pack()
    Button(janela_msg, text='OK', command=janela_msg.destroy).pack()

def erro():
    janela_msg = Toplevel()
    janela_msg.title('Aviso')
    janela_msg.geometry('600x400')

    Label(janela_msg, text='Erro, confira seu link e tente novamente!!', font='arial 12', pady=30).pack()
    Button(janela_msg, text='OK', command=janela_msg.destroy).pack()


quadro = Frame(janela)
quadro.pack()

Label(quadro, text='Insira a URL para download: ', font='arial 12 bold').pack(side='left')
link = Entry(quadro, font='arial 20', width=50)
link.pack(side='left')

Button(quadro, bg='red', text='>>>', bd=1, fg='white', width=4, height=2, command=lambda: download(link.get())).pack()
janela.mainloop()


