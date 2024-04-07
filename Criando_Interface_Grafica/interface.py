import tkinter as tk


def imprimir():
    print('teste')


def criar_interface():
    tela = tk.Tk()
    tela.geometry('500x500')
    tela.title('Interface Grafica')

    texto = tk.Label(tela, text='Clique no botão abaixo', font=('Arial', 14))
    texto.pack(padx=10, pady=10)

    botao = tk.Button(tela, text='Clique Aqui', font=('Arial', 15), width=20, command=imprimir)
    botao.pack(pady=10)

    tela.mainloop()


if __name__ == '__main__':
    criar_interface()
