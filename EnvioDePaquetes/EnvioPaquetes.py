import networkx as nx  # Importación del paquete NetworkX
import matplotlib.pyplot as plt  # Importación del paquete Matplotlib
import random as random


class Nodo:
    def __init__(self, extremo, anchoBanda, throughput, ruido, probabilidadCaida):
        self.extremo = extremo
        self.anchoBanda = anchoBanda
        self.throughput = throughput
        self.ruido = ruido
        self.probabilidadCaida = probabilidadCaida

    def getExtremo(self):
        return self.extremo

    def getAnchoBanda(self):
        return self.anchoBanda

    def getRuido(self):
        return self.ruido

    def getProbabilidadCaida(self):
        return self.probabilidadCaida

    def getThroughput(self):
        return self.throughput

    def setAnchoBanda(self, valorAnchoBanda):
        self.anchoBanda = valorAnchoBanda

    def setThroughput(self, valorThroughput):
        self.throughput = valorThroughput

    def setRuido(self, valorRuido):
        self.ruido = valorRuido

    def setProbabilidadCaida(self, valorProbabilidadCaida):
        self.probabilidadCaida = valorProbabilidadCaida

    def variarParametros(self):

        #print("Clock")

        if self.extremo == False:
            valorAnchoBandaMitad = random.randrange(13,500)
            self.setAnchoBanda(valorAnchoBandaMitad)
            self.setThroughput(valorAnchoBandaMitad)
        else:
            valorAnchoBandaExtremo = random.randrange(13, 300)
            self.setAnchoBanda(random.randrange(13, 300))
            self.setThroughput(random.uniform(valorAnchoBandaExtremo*0.25,valorAnchoBandaExtremo*0.75))
        self.setProbabilidadCaida(random.uniform(0.01,1))
        self.setRuido(random.randrange(0,50))

    def imprimirInformacion(self):
        print("Ancho de banda", self.anchoBanda)
        print("Ruido", self.ruido)
        print("Probabilidad de caida", self.probabilidadCaida)
        print("Througput", self.throughput)

def calcularHeuristica(nodo):
    valor = ((nodo.getAnchoBanda() * nodo.getThroughput()) - nodo.getRuido()) / nodo.getProbabilidadCaida()
    return valor

nodo1=Nodo(True,100,10,0.1,0.1)
nodo1.variarParametros()
nodo2=Nodo(True,100,10,0.1,0.1)
nodo2.variarParametros()
nodo3=Nodo(False,100,10,0.1,0.1)
nodo3.variarParametros()
nodo4=Nodo(False,100,10,0.1,0.1)
nodo4.variarParametros()
nodo5=Nodo(False,100,10,0.1,0.1)
nodo5.variarParametros()
nodo6=Nodo(False,100,10,0.1,0.1)
nodo6.variarParametros()
nodo7=Nodo(True,100,10,0.1,0.1)
nodo7.variarParametros()
nodo8=Nodo(True, 100,10,0.1,0.1)
nodo8.variarParametros()
G = nx.Graph()
G.add_node(1,pos=(1,1))
G.add_node(2,pos=(1.5,4))
G.add_node(3,pos=(2.4,2.3))
G.add_node(4,pos=(3.7,1))
G.add_node(5,pos=(3.6,4))
G.add_node(6,pos=(4.3,2.5))
G.add_node(7,pos=(5.4,4))
G.add_node(8,pos=(5.8,1))
aristas=[
    (1,3),
    (2,3),
    (3,4),
    (3,5),
    (3,6),
    (6,4),
    (6,5),
    (6,7),
    (6,8),
    (2,5),
    (5,7),
    (1,4),
    (4,8)
]
nodos=[
    nodo1,
    nodo2,
    nodo3,
    nodo4,
    nodo5,
    nodo6,
    nodo7,
    nodo8
]

def clock():
    for i in nodos:
        i.variarParametros()

G.add_edges_from(aristas)

origen=2
destino=8
recorrido = []
cantidadPaquetes = 4

for u in range(cantidadPaquetes):
    while len(nx.shortest_path(G,origen,destino,'weight',"dijkstra"))>1:
      recorrido.append(origen)
      origen=nx.shortest_path(G,origen,destino,'weight',"dijkstra")[1]
      print(nx.shortest_path(G,origen,destino,'weight',"dijkstra"))
      for i in range(len(aristas)):
        G[aristas[i][0]][aristas[i][1]]['weight']=(calcularHeuristica(nodos[aristas[i][0]-1])+calcularHeuristica(nodos[aristas[i][1]-1]))
      for j in range(8):
        print(str(aristas[j])+" "+str(G[aristas[j][0]][aristas[j][1]]['weight']))
      for k in range(len(nodos)):
        nodos[k].variarParametros()
    recorrido.append(destino)
    print("Paquete",u,recorrido)
    recorrido.clear()
    origen = 2
    destino = 8


pos=nx.get_node_attributes(G,'pos')
nx.draw(G,pos,with_labels=True)
labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
plt.show()
nx.shortest_path(G,2,8,'weight',"dijkstra")