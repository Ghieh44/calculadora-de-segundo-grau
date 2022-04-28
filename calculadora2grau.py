#importações
#By Ghieh44
from tkinter import *

#inicio da tela
janela = Tk()

#nome da tela
janela.title('expressão segundo grau')

#tamanho da tela
janela.geometry('300x400')

#chamando antes para poder limpar depois
resposta = Label(janela)

#criando os frames
frame1 = Frame(janela, borderwidth=1, relief='solid')
frame1.place(x=0, y=0, width=300, height= 100)

frame2 = Frame(janela, borderwidth=1, relief='solid')
frame2.place(x=0, y=100, width=150, height=300)

frame3 = Frame(janela, borderwidth=1, relief='solid')
frame3.place(x=150, y=100, width=150, height=300)
        
#função que vai dar x1 e x2
def xx():
    #limpando o label
    global resposta
    resposta.destroy()
    
    #recebendo os valores
    a = float(atext.get())
    b = float(btext.get())
    c = float(ctext.get())
    
    #calculando o delta
    delta = ((b*b) - 4*a*c)
    
    #se o delta for negativo
    if delta < 0:
        resposta = Label(frame3, text="""essa equação não
possui raizes reais
logo não tem
resposta""")
        #definindo o local da resposta
        resposta.place(x=25, y=150)
    
    #se não    
    else:
        x1 = (-b + delta ** (1/2))/(2*a)
        x2 = (-b - delta ** (1/2))/(2*a)
        resposta = Label(frame3, text= f"""
x1 = {x1}

x2 = {x2}
        """)
        #definindo o local da resposta
        resposta.place(x=50, y=150)


#explicação para leigos
txt_orient = Label(frame1, text="""segundo a regra de equação de segundo grau
a expressão é Ax² + Bx + C
by Ghieh44""")
txt_orient.place(x=25, y=20)

#indicando onde colocar os valores
txt_orient1 = Label(frame2, text="""digite os valores
requisitados""")
txt_orient1.place(x=25, y=10)

#entrada do valor A
atext = Entry(frame2)
atext.place(x=10, y=150 )
atext.insert(0, 'valor de A')
atext.configure(state=DISABLED)
def on_click1(event):
        atext.configure(state=NORMAL)
        atext.delete(0, END)
atext.bind('<Button-1>', on_click1)

#entrada do valor B
btext = Entry(frame2)
btext.place(x= 10, y= 170)
btext.insert(0, 'valor de B')
btext.configure(state=DISABLED)
def on_click2(event):
    btext.configure(state=NORMAL)
    btext.delete(0, END)
btext.bind('<Button-1>', on_click2)

#entrada do valor C
ctext = Entry(frame2)
ctext.place(x= 10, y= 190)
ctext.insert(0, 'valor de C')
ctext.configure(state=DISABLED)
def on_click3(event):
    ctext.configure(state=NORMAL)
    ctext.delete(0, END)
ctext.bind('<Button-1>', on_click3)

#botão para calcular
botao = Button(frame3, text='clique para calcular', command=xx)
botao.place(x= 25, y= 20)


#funcionar a tela
janela.mainloop()