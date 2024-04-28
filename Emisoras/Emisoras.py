import networkx as nx  # Importación del paquete NetworkX
import matplotlib.pyplot as plt  # Importación del paquete Matplotlib
import random as random

Televisoras = nx.Graph()
Televisoras.add_node(1,pos=(6,6))
Televisoras.add_node(2,pos=(8,5))
Televisoras.add_node(3,pos=(8,2))
Televisoras.add_node(4,pos=(6,1))
Televisoras.add_node(5,pos=(4,2))
Televisoras.add_node(6,pos=(4,5))

aristas=[
    (1,2,85),
    (1,3,175),
    (1,4,200),
    (1,5,50),
    (1,6,100),
    (2,3,125),
    (2,4,175),
    (2,5,100),
    (2,6,160),
    (3,4,100),
    (3,5,200),
    (3,6,250),
    (4,5,210),
    (4,6,220),
    (5,6,100)
]

indiceColores = {0: 'red', 1: 'blue', 2: 'green', 3: 'yellow', 4: 'magenta', 5: 'white', 6: 'orange', 7: 'cyan'}
def colorear_grafo(grafo):
    # Inicializar el diccionario de colores
    color_map = {}

    # Iterar sobre cada nodo del grafo
    for nodo in grafo.nodes():
        colores_disponibles = list(range(len(grafo.nodes())))

        # Eliminar los colores ya utilizados por los nodos vecinos
        for vecino in grafo.neighbors(nodo):
            if vecino in color_map:
                if color_map[vecino] in colores_disponibles:
                    colores_disponibles.remove(color_map[vecino])

        # Asignar el primer color disponible al nodo
        color_map[nodo] = colores_disponibles[0]

    return color_map

corriendo = True

while(corriendo):
    eleccion=input("Desea ingresar más nodos?")
    if eleccion=="Si" or eleccion=="si":
      Televisoras.add_node(Televisoras.number_of_nodes()+1,pos=(random.randrange(0,10),random.randrange(0,10)))
      numaristas=int(input("Cuántas aristas salen del nodo?:"))
      for i in range(numaristas):
        conexion=int(input("A qué nodo se conecta?:"))
        peso=int(input("A qué distancia está del nodo?:"))
        Televisoras.add_edge(Televisoras.number_of_nodes(),conexion)
        Televisoras[Televisoras.number_of_nodes()][conexion]['weight']=peso
    else:
        corriendo = False
    Televisoras.add_weighted_edges_from(aristas)

#color_list = ["red","cyan","red","red","darkblue","cyan","orange"]
color_list = []
otro = colorear_grafo(Televisoras)
print(otro)

for i in otro:
    color_list.append(indiceColores[otro[i]])

pos=nx.get_node_attributes(Televisoras,'pos')
nx.draw(Televisoras,pos,node_color=color_list,with_labels=True)
labels = nx.get_edge_attributes(Televisoras,'weight')
nx.draw_networkx_edge_labels(Televisoras,pos,edge_labels=labels)
plt.show()

