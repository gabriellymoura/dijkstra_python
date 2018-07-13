
from tkinter import *
from dijkstra import *
import time

CANVASL = 500 #largura usada no canvas
CANVASA = 350 #altura usada no canvas
#cores usada
creme ='#4682B4' #mudei pra aazul

class Interface(object):
    def __init__(self, i):
        self.g= Grafo() # crio um objeto do tipo grafo pra pegar os elementos do grafo

        #FONTES
        self.fonte1 = ('Arial', '20', 'bold')
        self.fonte2 = ('Arial', '8', 'bold')
        self.fonte3 = ('Arial', '10', 'bold')
        self.fonte4 = ('Arial', '12', 'bold')
        self.fonte5 = ('Arial', '25', 'bold')

        #FRAMES
        self.frame1 = Frame(i)
        self.frame1['bg'] = creme
        self.frame1_5 = Frame(i)
        self.frame1_5['bg'] = creme
        self.frame2 = Frame(i)
        self.frame2['bg'] = creme
        self.frame3 = Frame(i)
        self.frame3['bg'] = creme
        self.frame3_5 = Frame(i)
        self.frame3_5['bg'] = creme
        self.frame3_6 = Frame(i)
        self.frame3_6['bg'] = creme
        self.frame4_1 = Frame(i)
        self.frame4_1['bg'] = creme
        self.frame4 = Frame(i)
        self.frame4['bg'] = creme
        self.frame5 = Frame(i)
        self.frame5['bg'] = creme
        self.frame6 = Frame(i)
        self.frame6['bg'] = creme
        self.frame7 = Frame(i)
        self.frame7['bg'] = creme
        self.frame8 = Frame(i)
        self.frame8['bg'] = creme
        self.frame9 = Frame(i)
        self.frame9['bg'] = creme
        self.frame10 = Frame(i)
        self.frame10['bg'] = creme
        self.frame11 = Frame(i)
        self.frame11['bg'] = creme

        #TEXTO
        self.texto = Label(self.frame1, text='LABIRINTO COM DIJKSTRA', bg= creme, fg='darkred', font = self.fonte1)  # adciona texto
        self.texto2 = Label(self.frame1_5, text='Chegue até o queijo pelo caminho mais curto. Siga através dos números.', bg= creme, fg='darkred', font = self.fonte4)
        self.numeros = Label(self.frame2, text='1,3,6,8,12,14,16,18', bg=creme, fg='darkred', font=self.fonte4)  # texto com a resposta

        #MATRIZ
        self.minitexto = Label(self.frame4_1, text='Matriz: ', bg=creme, fg='darkred', font=self.fonte1)
        for r in range(1, g.num):
            for c in range(1, g.num):  #.grid deixa os numeros organizados em forma de matriz #borderwidth é espaçamento entre os numeros
                self.matr = Label(self.frame4, text=g.mat[r][c], borderwidth=3, bg = creme, fg = 'darkred', font = self.fonte4).grid(row= r,column = c )
        #VERTICES
        self.minitexto1 = Label(self.frame5, text='Vertices: ', bg=creme, fg='darkred', font=self.fonte1)
        subframe1 = Frame(self.frame6)
        for j in range(1, g.num):
            if j % 18 == 0:
                subframe1.pack()  #subdividir pra ficar de forma organizada
            self.vertices = Label(subframe1, text=j, bg=creme, fg='darkred', font=self.fonte4)
            self.vertices.pack(side=LEFT)
        #MENOR CAMINHO
        self.minitexto2 = Label(self.frame7, text='Distancia: ', bg=creme, fg='darkred', font=self.fonte1)
        subframe1 = Frame(self.frame8)
        for j in range(1, g.num):
            if j % 18 == 0:
                subframe1.pack()
            self.distanci = Label(subframe1, text=g.distancia[j], bg=creme, fg='darkred', font=self.fonte4)
            self.distanci.pack(side=LEFT)
        #ANTERIORES
        self.minitexto3 = Label(self.frame9, text='Anteriores: ', bg=creme, fg='darkred', font=self.fonte1)
        subframe1 = Frame(self.frame10)
        for j in range(1, g.num):
            if j % 18 == 0:
                subframe1.pack()
            self.anterior = Label(subframe1, text=g.anterior[j], bg=creme, fg='darkred', font=self.fonte4)
            self.anterior.pack(side=LEFT)

        #IMAGENS
        logo = PhotoImage(file='teste.gif') #imagem do labirinto que foi usada, formato .gif
        self.logo = Label(self.frame11,bg =creme)  # width=300, height=300
        self.logo['image'] = logo
        self.logo.image = logo

        #LABIRINTO
        self.canvas = Canvas(self.frame2, bg='black', width=CANVASL, height=CANVASA) #criação do canvas

        #self.lista = []# lista com retangulos
        l, c, e = 7, 10, 2  # linhas, colunas, espaçamento
        b, h, y0 = 48, 48, 0 #base do retangulo, altura do retangulo e y inicial
        for i in range(l):
            for j in range(c): #criando 70 quadrados brancos no canvas
                lista = self.canvas.create_rectangle(b * j + (j + 1) * e, i * h + (i + 1) * e + y0, b * j + (j + 1) * e + b, i * h + (i + 1) * e + y0 + h, fill='white')
                #self.lista.append(lista)

        #LINHA 0
        self.canvas.create_rectangle(b * 1 + (1 + 1) * e, 0 * h + (0 + 1) * e + y0, b * 1 + (1 + 1) * e + b, 0 * h + (0 + 1) * e + y0 + h, fill='red')
        self.canvas.create_rectangle(b * 2 + (2 + 1) * e, 0 * h + (0 + 1) * e + y0, b * 2 + (2 + 1) * e + b, 0 * h + (0 + 1) * e + y0 + h, fill='red')
        self.canvas.create_rectangle(b * 6 + (6 + 1) * e, 0 * h + (0 + 1) * e + y0, b * 6 + (6 + 1) * e + b, 0 * h + (0 + 1) * e + y0 + h, fill='red')
        self.canvas.create_rectangle(b * 7 + (7 + 1) * e, 0 * h + (0 + 1) * e + y0, b * 7 + (7 + 1) * e + b, 0 * h + (0 + 1) * e + y0 + h, fill='red')
        self.canvas.create_rectangle(b * 8 + (8 + 1) * e, 0 * h + (0 + 1) * e + y0, b * 8 + (8 + 1) * e + b, 0 * h + (0 + 1) * e + y0 + h, fill='red')
        self.canvas.create_rectangle(b * 9 + (9 + 1) * e, 0 * h + (0 + 1) * e + y0, b * 9 + (9 + 1) * e + b, 0 * h + (0 + 1) * e + y0 + h, fill='red')
        #LINHA 1
        self.canvas.create_rectangle(b * 4 + (4 + 1) * e, 1 * h + (1 + 1) * e + y0, b * 4 + (4 + 1) * e + b, 1 * h + (1 + 1) * e + y0 + h, fill='red')
        #LINHA 2
        self.canvas.create_rectangle(b * 1 + (1 + 1) * e, 2 * h + (2 + 1) * e + y0, b * 1 + (1 + 1) * e + b, 2 * h + (2 + 1) * e + y0 + h, fill='red')
        self.canvas.create_rectangle(b * 2 + (2 + 1) * e, 2 * h + (2 + 1) * e + y0, b * 2 + (2 + 1) * e + b, 2 * h + (2 + 1) * e + y0 + h, fill='red')
        self.canvas.create_rectangle(b * 4 + (4 + 1) * e, 2 * h + (2 + 1) * e + y0, b * 4 + (4 + 1) * e + b, 2 * h + (2 + 1) * e + y0 + h, fill='red')
        self.canvas.create_rectangle(b * 6 + (6 + 1) * e, 2 * h + (2 + 1) * e + y0, b * 6 + (6 + 1) * e + b, 2 * h + (2 + 1) * e + y0 + h, fill='red')
        self.canvas.create_rectangle(b * 8 + (8 + 1) * e, 2 * h + (2 + 1) * e + y0, b * 8 + (8 + 1) * e + b, 2 * h + (2 + 1) * e + y0 + h, fill='red')
        #LINHA 3
        self.canvas.create_rectangle(b * 1 + (1 + 1) * e, 3 * h + (3 + 1) * e + y0, b * 1 + (1 + 1) * e + b, 3 * h + (3 + 1) * e + y0 + h, fill='red')
        self.canvas.create_rectangle(b * 2 + (2 + 1) * e, 3 * h + (3 + 1) * e + y0, b * 2 + (2 + 1) * e + b, 3 * h + (3 + 1) * e + y0 + h, fill='red')
        self.canvas.create_rectangle(b * 6 + (6 + 1) * e, 3 * h + (3 + 1) * e + y0, b * 6 + (6 + 1) * e + b, 3 * h + (3 + 1) * e + y0 + h, fill='red')
        #LINHA 4
        self.canvas.create_rectangle(b * 4 + (4 + 1) * e, 4 * h + (4 + 1) * e + y0, b * 4 + (4 + 1) * e + b, 4 * h + (4 + 1) * e + y0 + h, fill='red')
        self.canvas.create_rectangle(b * 6 + (6 + 1) * e, 4 * h + (4 + 1) * e + y0, b * 6 + (6 + 1) * e + b, 4 * h + (4 + 1) * e + y0 + h, fill='red')
        self.canvas.create_rectangle(b * 8 + (8 + 1) * e, 4 * h + (4 + 1) * e + y0, b * 8 + (8 + 1) * e + b, 4 * h + (4 + 1) * e + y0 + h, fill='red')
        #LINHA 5
        self.canvas.create_rectangle(b * 1 + (1 + 1) * e, 5 * h + (5 + 1) * e + y0, b * 1 + (1 + 1) * e + b, 5 * h + (5 + 1) * e + y0 + h, fill='red')
        self.canvas.create_rectangle(b * 2 + (2 + 1) * e, 5 * h + (5 + 1) * e + y0, b * 2 + (2 + 1) * e + b, 5 * h + (5 + 1) * e + y0 + h, fill='red')
        self.canvas.create_rectangle(b * 8 + (8 + 1) * e, 5 * h + (5 + 1) * e + y0, b * 8 + (8 + 1) * e + b, 5 * h + (5 + 1) * e + y0 + h, fill='red')
        #LINHA 6
        self.canvas.create_rectangle(b * 4 + (4 + 1) * e, 6 * h + (6 + 1) * e + y0, b * 4 + (4 + 1) * e + b, 6 * h + (6 + 1) * e + y0 + h, fill='red')
        self.canvas.create_rectangle(b * 6 + (6 + 1) * e, 6 * h + (6 + 1) * e + y0, b * 6 + (6 + 1) * e + b, 6 * h + (6 + 1) * e + y0 + h, fill='red')

        # Numeros
        self.v1 = self.canvas.create_text(25, 175, fill='black', text='1',font=self.fonte5)
        self.v2 = self.canvas.create_text(175, 75, fill='black', text='2', font=self.fonte5)
        self.v3 = self.canvas.create_text(25, 225, fill='black', text='3', font=self.fonte5)
        self.v4 = self.canvas.create_text(25, 325, fill='black', text='4', font=self.fonte5)
        self.v5 = self.canvas.create_text(175, 325, fill='black', text='5', font=self.fonte5)
        self.v6 = self.canvas.create_text(175, 225, fill='black', text='6', font=self.fonte5)
        self.v7 = self.canvas.create_text(175, 175, fill='black', text='7', font=self.fonte5)
        self.v8 = self.canvas.create_text(175, 275, fill='black', text='8', font=self.fonte5)
        self.v9 = self.canvas.create_text(275, 25, fill='black', text='9', font=self.fonte5)
        self.v10 = self.canvas.create_text(275, 175, fill='black', text='10', font=self.fonte5)
        self.v11 = self.canvas.create_text(275, 75, fill='black', text='11', font=self.fonte5)
        self.v12 = self.canvas.create_text(275, 275, fill='black', text='12', font=self.fonte5)
        self.v13 = self.canvas.create_text(375, 75, fill='black', text='13', font=self.fonte5)
        self.v14 = self.canvas.create_text(375, 275, fill='black', text='14', font=self.fonte5)
        self.v15 = self.canvas.create_text(475, 325, fill='black', text='15', font=self.fonte5)
        self.v16 = self.canvas.create_text(375, 175, fill='black', text='16', font=self.fonte5)
        self.v17 = self.canvas.create_text(475, 175, fill='black', text='17', font=self.fonte5)
        self.v18 = self.canvas.create_text(425, 175, fill='black', text='18', font=self.fonte5)

        self.rato = self.canvas.create_oval(0, 150, 50, 200, fill='darkblue') #rato
        self.queijo = self.canvas.create_arc(365,150,450,240, fill='yellow') #queijo

        #self.jogando = True

        #BOTÕES
        self.ativa = False # elemento que determina se a função está ativada ou não, nesse caso a função mostrar elementos
        self.elementos = Button(self.frame3_5, text = 'Mostrar Elementos',bg=creme, fg='darkred', font=self.fonte4, command = self.mostraElementos) #botão que mostra os elementos
        self.start = Button(self.frame3_6, text = 'RESTART', bg = creme, font = self.fonte4, fg = 'darkred',command =  self.começa) # botão que recomeça o jogo
        self.esquerda = Button(self.frame3_6, text='←', bg=creme, font=self.fonte4, fg='darkred', command=self.começaEsquerda) #botão esquerda
        self.direito = Button(self.frame3_6, text = '→', bg = creme, font = self.fonte4, fg = 'darkred', command = self.começaDIreita) #botão direita
        self.baixo = Button(self.frame3_6, text='↓', bg=creme, font=self.fonte4, fg='darkred', command = self.começaBaixo) #botão para baixo
        self.cima = Button(self.frame3_6, text='↑', bg=creme, font=self.fonte4, fg='darkred', command = self.começaCima) #botão para cima
        self.resp = False   # elemento que determina se a função está ativada ou não, nesse caso a função para mostar a resposta
        self.resposta = Button(self.frame2, text = 'Solução', bg=creme, font=self.fonte4, fg='darkred', command = self.mostraResposta) #botão que mostar a resposta

        #funcionamento do teclado, usando bind
        self.esquerda.focus_force()
        self.esquerda.bind('<Left>', self.começaEsquerda1)
        self.direito.bind('<Right>', self.começaDIreita1)
        self.baixo.bind('<Down>', self.começaBaixo1)
        self.cima.bind('<Up>', self.começaCima1)
        self.elementos.bind('<Return>', self.mostraElementos1)

        #EMPACOTANDO NA TELA
        self.frame3_5.pack()   #Foi empacotado aqui os frames que eu quis que aparecesse logo de cara, os outros estão "ocultos"
        self.frame1.pack()
        self.frame1_5.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame3_6.pack()

        self.minitexto.pack(side = LEFT)
        self.minitexto1.pack()
        self.minitexto2.pack()
        self.minitexto3.pack()
        self.texto.pack()
        self.texto2.pack()

        self.logo.pack(side = RIGHT)
        self.elementos.pack()
        self.start.pack()
        self.canvas.pack()
        self.esquerda.pack(side=LEFT)
        self.direito.pack(side = LEFT)
        self.baixo.pack(side  = LEFT)
        self.cima.pack(side = LEFT)
        self.resposta.pack(side = RIGHT)

        #variaveis auxiliares
        self.aux1 = 0
        self.aux2 = 0
        p = (25, 25)
        self.b_vx = self.b_vy = 25 #velocidade de movimentação no sentido de x e y
        self.b_x, self.b_y = p # valor da coordenada de x e y

    def mostraElementos(self): # esconde as frames inicias e mostra as outras
        self.ativa = not self.ativa
        if self.ativa:
            #frames que quero mostrar #frames dos elementos
            self.trocaTexto()
            self.frame4_1.pack(side=LEFT)
            self.frame4.pack(side=LEFT)
            self.frame5.pack()
            self.frame6.pack()
            self.frame7.pack()
            self.frame8.pack()
            self.frame9.pack()
            self.frame10.pack()
            self.frame11.pack()

            #frames que quero esconder #frames do labirinto
            self.frame1.pack_forget() # é como se 'escondesse' o frame
            self.frame1_5.pack_forget()
            self.frame2.pack_forget()
            self.frame3.pack_forget()
            self.frame3_6.pack_forget()

        else:
            self.trocaTexto()
            self.frame4.pack_forget()
            self.frame4_1.pack_forget()
            self.frame5.pack_forget()
            self.frame6.pack_forget()
            self.frame7.pack_forget()
            self.frame8.pack_forget()
            self.frame9.pack_forget()
            self.frame10.pack_forget()
            self.frame11.pack_forget()

            self.frame1.pack()
            self.frame1_5.pack()
            self.frame2.pack()
            self.frame3.pack()
            self.frame3_6.pack()
            self.frame1.pack()
            self.frame1_5.pack()
            self.frame2.pack()
            self.frame3.pack()
            self.frame3_6.pack()

    def mostraElementos1(self, event): #função ativada a partir do teclado
        self.mostraElementos()

    def trocaTexto(self): #troca o texto de elementos
        if self.ativa:
            self.elementos['text'] = 'Ocultar Elementos'
        else:
            self.elementos['text'] = 'Mostrar Elementos'

    def começaDIreita(self):
        self.canvas.move(self.rato, self.b_vx, 0) #se move no sentido x positivo
        self.canvas.update()
        self.b_x += self.b_vx
        self.b_y += 0
        if self.b_x > 425-30 and self.b_y > 175-30: #se atingir a posição do queijo
            self.v20 = self.canvas.create_text(425, 175, fill='green', text='GANHOU', font=self.fonte5)
            #self.aux2 += 1
        if self.b_x > CANVASL -50: # or self.b_x < 0: #delimita o espaço, se atingir os limites do labirinto
            self.v20 = self.canvas.create_text(425, 175, fill='darkred', text='PERDEU', font=self.fonte5)
            #self.aux2 += 1
    def começaEsquerda(self):
        self.canvas.move(self.rato, self.b_vx*-1, 0) #se move no sentido x negativo
        self.b_x += self.b_vx*-1
        self.b_y += 0
        self.canvas.update()
        if self.b_x > 425-30 and self.b_y > 175-30:
            self.v20 = self.canvas.create_text(425, 175, fill='green', text='GANHOU', font=self.fonte5)
            #self.aux2 += 1
        if self.b_x <0:
            self.v20 = self.canvas.create_text(425, 175, fill='darkred', text='PERDEU', font=self.fonte5)
            #self.aux2 += 1
    def começaBaixo(self): #se move no sentido y positivo
        self.canvas.move(self.rato, 0, self.b_vy)
        self.b_x += 0
        self.b_y += self.b_vy
        if self.b_x == 425-30 and self.b_y == 175-30:
            self.v20 = self.canvas.create_text(425, 175, fill='green', text='GANHOU', font=self.fonte5)
            #self.aux2 += 1
        if self.b_y <0:
            self.v20 = self.canvas.create_text(425, 175, fill='darkred', text='PERDEU', font=self.fonte5)
            #self.aux2 += 1
    def começaCima(self): #se mpove no sentido y negativo
        self.canvas.move(self.rato, 0, self.b_vy*-1)
        self.b_x += 0
        self.b_y += self.b_vy
        if self.b_x > 425-30 and self.b_y > 175-30:
            self.v20 = self.canvas.create_text(425, 175, fill='green', text='GANHOU', font=self.fonte5)
            #self.aux2 += 1
        if self.b_y > CANVASA-50: # or self.b_x < 0: #delimita o espaço
            self.v20 =self.canvas.create_text(425, 175, fill='darkred', text='PERDEU', font=self.fonte5)
           # self.aux2 += 1

    def começaDIreita1(self, event):#função ativada a partir do teclado
        self.começaDIreita()
    def começaEsquerda1(self, event):#função ativada a partir do teclado
        self.começaEsquerda()
    def começaBaixo1(self, event):#função ativada a partir do teclado
        self.começaBaixo()
    def começaCima1(self, event):#função ativada a partir do teclado
        self.começaCima()

    def mostraResposta(self): #o rato se move até o queijo
        for i in range(2):
            self.canvas.move(self.rato,0,self.b_vy)
            time.sleep(0.1)
            self.canvas.update()
        for i in range(6):
            self.canvas.move(self.rato, self.b_vx, 0)
            time.sleep(0.1)
            self.canvas.update()
        for i in range(2):
            self.canvas.move(self.rato,0,self.b_vy)
            time.sleep(0.1)
            self.canvas.update()
        for i in range(8):
            self.canvas.move(self.rato, self.b_vx, 0)
            time.sleep(0.1)
            self.canvas.update()
        for i in range(4):
            self.canvas.move(self.rato,0,-1*self.b_vy)
            time.sleep(0.1)
            self.canvas.update()
        for i in range(2):
            self.canvas.move(self.rato, self.b_vx, 0)
            time.sleep(0.1)
            self.canvas.update()
        self.v19 = self.canvas.create_text(425, 175, fill='green', text='CHEGOU', font=self.fonte1)
        self.aux1 +=1
        self.numeros.pack(side = RIGHT)

    def começa(self): #recomeça com o rato no inicio
        self.v20 = self.canvas.create_text(425, 175, fill='green', text=' ')
        self.canvas.delete(self.v20)
        self.numeros.pack_forget()
        self.canvas.delete(self.rato)
        if self.aux1>=1:
            self.canvas.delete(self.v19)
        self.rato = self.canvas.create_oval(0, 150, 50, 200, fill='darkblue')

#g = Grafo()
inter = Tk()
Interface(inter)
inter.title('Labirinto')
inter.geometry('800x630')
inter['bg'] = creme
inter.mainloop()