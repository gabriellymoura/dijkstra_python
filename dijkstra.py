
import numpy as np

class Grafo:
    def __init__(self):
        self.num = 19
        self.mat = np.zeros((self.num,self.num),dtype=int)
        self.visitado = np.zeros((self.num), dtype=int)
        self.anterior = [-1]*self.num
        self.distancia = [9999]*self.num

    def imprimir(self):
        for i in range (1,self.num):
            for j in range (1,self.num):
                print(self.mat[i][j], end='  ')
            print('\n')


    def imprimirVetor(self):
        print('Vetor Visitado: ')
        for j in range (1,self.num):
            print(self.visitado[j], end='  ')

    def insere(self, v1,v2,peso):
        self.mat[v1][v2] = peso
        self.mat[v2][v1] = peso

    def procura(self,dis, visi, n):
        menor = 0
        minimo = 9999
        for i in range (1,n):
            if(dis[i]<minimo and visi[i] == 0):
                minimo=dis[i]
                menor=i
        return menor

    def dijkstra1(self,inicial):
        aux = self.num
        self.distancia[inicial] = 0
        self.anterior[inicial] = 0
        while aux>0:
            menor = self.procura(self.distancia, self.visitado, self.num)
            for i in range (1,self.num):
                if (self.mat[menor][i] != 0):
                    vizinho = i
                    if (self.anterior[vizinho] < 0):
                        self.distancia[vizinho] = self.distancia[menor] + self.mat[menor][i]
                        self.anterior[vizinho] = menor
                    elif self.distancia[vizinho] > self.distancia[menor] + self.mat[menor][i]:
                        self.distancia[vizinho] = self.distancia[menor] + self.mat[menor][i]
                        self.anterior[vizinho] = menor
            self.visitado[menor] = 1
            aux = aux-1

g = Grafo()
g.__init__()
g.insere(1,2,5)
g.insere(1,3,1)
g.insere(3,4,2)
g.insere(4,5,3)
g.insere(3,6,3)
g.insere(6,7,1)
g.insere(7,2,5)
g.insere(5,8,1)
g.insere(8,6,1)
g.insere(2,9,3)
g.insere(7,10,2)
g.insere(9,11,1)
g.insere(11,10,2)
g.insere(8,12,2)
g.insere(10,12,2)
g.insere(11,13,2)
g.insere(12,14,2)
g.insere(14,15,3)
g.insere(14,16,2)
g.insere(13,16,2)
g.insere(15,17,3)
g.insere(13,17,4)
g.insere(17,18,1)
g.insere(16,18,1)

g.imprimir()
print('\n \n')

g.dijkstra1(1)

for j in range(1, g.num):
    print(j,'->', g.distancia[j], ' - ', g.anterior[j])

g.imprimirVetor()