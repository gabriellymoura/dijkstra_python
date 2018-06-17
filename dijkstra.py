
import numpy as np


class Grafo:

    def __init__(self):
        self.num = 7
        self.mat = np.zeros((self.num,self.num),dtype=int)
        self.visitado = np.zeros((self.num), dtype=int)
        self.anterior = [-1]*self.num
        self.distancia = [9999]*self.num


    def imprimir(self):
        for i in range (1,7):
            for j in range (1,7):
                print(self.mat[i][j], end='  ')
            print('\n')


    def imprimirVetor(self):
        for j in range (1,7):
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


    def dijkstra(self,inicial):
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
g.insere(1,2,4)
g.insere(1,3,2)
g.insere(3,2,1)
g.insere(3,4,8)
g.insere(3,5,10)
g.insere(2,4,5)
g.insere(4,6,6)
g.insere(4,5,2)
g.insere(5,6,3)

g.imprimir()
print('\n \n')

g.dijkstra(1)

for i in range(1, g.num):
    print(i, '-> ', g.distancia[i], ' - ', g.anterior[i])



