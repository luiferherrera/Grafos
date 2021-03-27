import networkx as nx
import matplotlib.pyplot as plt
import itertools
import numpy as np
from interfaz import *


class mywindow(QtWidgets.QMainWindow, Ui_MainWindow):
    grafo = nx.Graph()
    aristas_camino = []
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btgrafo.clicked.connect(self.boton_grafo)
        self.btdigrafo.clicked.connect(self.boton_digrafo)
        self.btnodo.clicked.connect(self.ingresar_nodo)
        self.btarista.clicked.connect(self.ingresar_arista)
        self.btcamino.clicked.connect(self.camino)


    def camino(self):
        if not self.grafo.is_directed():
            self.dijkstra()
            self.matriz_adyacencia()
            self.matriz_incidencia()
            self.circuito_euleriano()
            self.camino_euleriano()
            self.hamiltoniano_grafo()
            self.planar()
            self.mostar_grafo()

        if self.grafo.is_directed():
            self.dijkstra()
            self.matriz_adyacencia()
            self.matriz_incidencia()
            self.circuito_euleriano()
            self.camino_euleriano()
            self.hamiltoniano_digrafo()
            self.planar()
            self.mostar_grafo()

    def matriz_adyacencia(self):
        print("")
        print("Matriz De Adyacencia: ")
        ad_lista = nx.adjacency_matrix(self.grafo)
        ad_matriz = ad_lista.todense()
        self.lbadyacencia.setText(str(ad_matriz))

    def matriz_incidencia(self):
        print("")
        print("Matriz De Incidencia: ")
        in_lista = nx.incidence_matrix(self.grafo)
        in_matriz = in_lista.todense()
        self.lbincidencia.setText(str(in_matriz))

    def circuito_euleriano(self):
        if nx.algorithms.is_eulerian(self.grafo):
            print("")
            self.lbcircuito.setText("El Grafo ES De Tipo Circuito Euleriano")
        else:
            self.lbcircuito.setText("El Grafo  NO ES De Tipo Circuito Euleriano")

    def camino_euleriano(self):
        if nx.algorithms.has_eulerian_path(self.grafo):
            print("")
            self.lbcamino.setText("El Grafo Es De Tipo Camino Euleriano")
        else:
            self.lbcamino.setText("El Grafo  NO ES De Tipo Camino Euleriano")

    def hamiltoniano_grafo(self):
        print("")
        n = self.grafo.number_of_nodes()
        if not nx.algorithms.is_connected(self.grafo):
            self.lbhamiltoniano.setText("No se puede comprobar que el grafo sea Hamiltoniano ya que no es conexo")
            return

        if n < 3:
            self.lbhamiltoniano.setText("El Grafo no es Hamiltoniano ya que no posee nodos suficientes")
            return

        for nodo in self.grafo.nodes():
            if self.grafo.degree(nodo) < (n / 2):
                self.lbhamiltoniano.setText("Segun el Teorema de Dirac el Grafo no es Hamiltoniano")
                return

        for nodo1 in self.grafo.nodes():
            for nodo2 in self.grafo.nodes:
                if (nodo1 != nodo2) and (self.grafo.has_edge(nodo1, nodo2) is False):
                    q1 = self.grafo.degree(nodo1)
                    q2 = self.grafo.degree(nodo2)
                    if (q1 + q2) < n:
                        self.lbhamiltoniano.setText("Segun el Teorema de Ore el Grafo no es Hamiltoniano")
                        return

        self.lbhamiltoniano.setText("El Grafo posee Camino y Circuito Hamiltoniano")

    def hamiltoniano_digrafo(self):
        n = self.grafo.number_of_nodes()
        if not nx.algorithms.is_strongly_connected(self.grafo):
            self.lbhamiltoniano.setText("No se puede comprobar que el grafo sea Hamiltoniano ya que no es conexo")
            return

        if n < 3:
            self.lbhamiltoniano.setText("El Grafo no es Hamiltoniano ya que no posee nodos suficientes")
            return

        for nodo in self.grafo.nodes():
            if self.grafo.degree(nodo) < (n / 2):
                self.lbhamiltoniano.setText("Segun el Teorema de Ghouila-Houiri el Grafo no es Hamiltoniano")
                return

        for nodo1 in self.grafo.nodes():
            for nodo2 in self.grafo.nodes:
                if (nodo1 != nodo2) and (self.grafo.has_edge(nodo1, nodo2) is False):
                    q1 = self.grafo.degree(nodo1)
                    q2 = self.grafo.degree(nodo2)
                    if (q1 + q2) < n:
                        self.lbhamiltoniano.setText("Segun el Teorema de Meyniel el Grafo no es Hamiltoniano")
                        return

        self.lbhamiltoniano.setText("El Grafo posee Camino y Circuito Hamiltoniano")
        return

    def planar(self):
        if nx.algorithms.check_planarity(self.grafo):
            self.lbplanar.setText("El Grafo Es Planar")

    def dijkstra(self):
        a = self.txtsalidacamino.text()
        b = self.txtcaminollegada.text()
        peso, nodo = nx.shortest_paths.single_source_dijkstra(self.grafo, a, b)
        i = 1
        for u in nodo:
            j = 1
            for v in nodo:
                if u != v and j == (i+1):
                    if self.grafo.has_edge(u, v):
                        self.aristas_camino.append((u, v))
                j = j+1
            i = i + 1
        print("El camino mas corto entre los nodos es: " + str(nodo))
        print("El peso del Camino es de: " + str(peso))
        return self.aristas_camino

    def mostar_grafo(self):
        if nx.check_planarity(self.grafo):
            self.color_regiones()
        else:
            colores_dict = {0: 'blue', 1: 'red', 2: 'green', 3: 'yellow'}
            colores = []
            coloreado = self.coloreado_nodos()
            pos = nx.drawing.spring_layout(self.grafo)
            labels = nx.get_edge_attributes(self.grafo, 'weight')

            for i, j in coloreado.items():
                colores.append(colores_dict[coloreado[i]])

            nx.draw_networkx(self.grafo, pos, with_labels=True, node_color=colores)
            nx.draw_networkx_edges(self.grafo, pos, self.aristas_camino, edge_color='blue', width=2.0)
            nx.draw_networkx_edge_labels(self.grafo, pos, edge_labels=labels)
            plt.show()


    def color_regiones(self):
        if self.grafo.is_directed():
            grafo2 = self.grafo.to_undirected()
            regiones = nx.cycle_basis(grafo2)
        else:
            regiones = nx.cycle_basis(self.grafo)
        pos = nx.drawing.planar_layout(self.grafo)

        labels = nx.get_edge_attributes(self.grafo, 'weight')
        nx.draw_networkx(self.grafo, pos, with_labels=True, node_color="green")

        nx.draw_networkx_edges(self.grafo, pos, self.aristas_camino, edge_color='blue', width=2.0)
        nx.draw_networkx_edge_labels(self.grafo, pos, edge_labels=labels)
        plt.show()

        nodelist = list(self.grafo)
        xy = np.asarray([pos[v] for v in nodelist])

        for region in regiones:
            cord_x = []
            cord_y = []
            for nodo in region:
                for num, n in enumerate(pos):
                    for num2, (x, y) in enumerate(xy):
                        if num == num2:
                            if n == nodo:
                                cord_x.append(x)
                                cord_y.append(y)
            plt.fill(cord_x, cord_y)

        nx.draw_networkx(self.grafo, pos, node_color='purple', font_color='white', width=1.5)
        plt.show()

    def coloreado_nodos(self):
        colores = {}
        nodos = self.grafo.nodes()
        for u in nodos:
            colores_vecinos = {colores[v] for v in self.grafo[u] if v in colores}
            for color in itertools.count():
                if color not in colores_vecinos:
                    break
            colores[u] = color
        return colores

    def ingresar_nodo(self):
        nodo = self.txtnombrenodo.text()
        self.grafo.add_node(nodo)
        self.txtnombrenodo.clear()
        self.txtnombrenodo.setFocus()


    def ingresar_arista(self):
        u = self.txtsalida.text()
        v = self.txtllegada.text()
        peso = int(self.txtpeso.text())
        self.grafo.add_edge(u, v, weight=peso)
        self.txtsalida.clear()
        self.txtllegada.clear()
        self.txtpeso.clear()
        self.txtsalida.setFocus()



    def boton_grafo(self):
        if self.grafo.is_directed():
            grafo2 = self.grafo.to_undirected()
            self.grafo = grafo2



    def boton_digrafo(self):
        if not self.grafo.is_directed():
            grafo2 = self.grafo.to_directed()
            self.grafo = grafo2







'''def ingresar_nodos(grafo):
    print("")
    n = int(input("Cantidad de nodos del grafo: "))
    for i in range(n):
        nodo = input("Ingresar el nombre del nodo " + str(i + 1) + " : ")
        grafo.add_node(nodo)


def ingresar_arista(grafo):
    print("")
    n = int(input("Cantidad de Aritas del grafo: "))
    for i in range(n):
        u = input('Ingrese el nodo de salida de la arista ' + str(i + 1) + ": ")
        v = input('Ingrese el nodo de llegada de la arista ' + str(i + 1) + ": ")
        peso = int(input("Ingrese el peso de la arista: "))
        grafo.add_edge(u, v, weight=peso)


def matriz_adyacencia(grafo):
    print("")
    print("Matriz De Adyacencia: ")
    ad_lista = nx.adjacency_matrix(grafo)
    ad_matriz = ad_lista.todense()
    print(ad_matriz)


def matriz_incidencia(grafo):
    print("")
    print("Matriz De Incidencia: ")
    in_lista = nx.incidence_matrix(grafo)
    in_matriz = in_lista.todense()
    print(in_matriz)


def mostar_grafo(grafo, aristas_camino):
    if nx.check_planarity(grafo):
        color_regiones(grafo, aristas_camino)
    else:
        colores_dict = {0: 'blue', 1: 'red', 2: 'green', 3: 'yellow'}
        colores = []
        coloreado = coloreado_nodos(grafo)
        pos = nx.drawing.spring_layout(grafo)
        labels = nx.get_edge_attributes(grafo, 'weight')

        for i, j in coloreado.items():
            colores.append(colores_dict[coloreado[i]])

        quitar_cuadro()
        plt.text(0.95, 0.87, 'Adyacencia\n' + str(matriz_adyacencia(grafo)), transform=plt.gca().transAxes)
        plt.text(-0.15, 0.87, 'Incidencia\n' + str(matriz_incidencia(grafo)), transform=plt.gca().transAxes)

        nx.draw_networkx(grafo, pos, with_labels=True, node_color=colores)
        nx.draw_networkx_edges(grafo, pos, aristas_camino, edge_color='blue', width=2.0)
        nx.draw_networkx_edge_labels(grafo, pos, edge_labels=labels)
        plt.show()


def color_regiones(grafo, aristas_camino):
    if grafo.is_directed():
        grafo2 = grafo.to_undirected()
        regiones = nx.cycle_basis(grafo2)
    else:
        regiones = nx.cycle_basis(grafo)
    pos = nx.drawing.planar_layout(grafo)

    quitar_cuadro()
    plt.text(0.95, 0.87, 'Adyacencia\n' + str(matriz_adyacencia(grafo)), transform=plt.gca().transAxes)
    plt.text(-0.15, 0.87, 'Incidencia\n' + str(matriz_incidencia(grafo)), transform=plt.gca().transAxes)

    labels = nx.get_edge_attributes(grafo, 'weight')
    nx.draw_networkx(grafo, pos, with_labels=True, node_color="green")

    nx.draw_networkx_edges(grafo, pos, aristas_camino, edge_color='blue', width=2.0)
    nx.draw_networkx_edge_labels(grafo, pos, edge_labels=labels)
    plt.show()

    nodelist = list(grafo)
    xy = np.asarray([pos[v] for v in nodelist])

    for region in regiones:
        cord_x = []
        cord_y = []
        for nodo in region:
            for num, n in enumerate(pos):
                for num2, (x, y) in enumerate(xy):
                    if num == num2:
                        if n == nodo:
                            cord_x.append(x)
                            cord_y.append(y)
        plt.fill(cord_x, cord_y)

    nx.draw_networkx(grafo, pos, node_color='purple', font_color='white', width=1.5)
    plt.show()


def circuito_euleriano(grafo):
    if nx.algorithms.is_eulerian(grafo):
        print("")
        print("El Grafo ES De Tipo Circuito Euleriano")
    else:
        return


def camino_euleriano(grafo):
    if nx.algorithms.has_eulerian_path(grafo):
        print("")
        print("El Grafo Es De Tipo Camino Euleriano")


def hamiltoniano_grafo(grafo):
    print("")
    n = grafo.number_of_nodes()
    if not nx.algorithms.is_connected(grafo):
        print("No se puede comprobar que el grafo sea Hamiltoniano ya que no es conexo")
        return

    if n < 3:
        print("El Grafo no es Hamiltoniano ya que no posee nodos suficientes")
        return

    for nodo in grafo.nodes():
        if grafo.degree(nodo) < (n / 2):
            print("Segun el Teorema de Dirac el Grafo no es Hamiltoniano")
            return

    for nodo1 in grafo.nodes():
        for nodo2 in grafo.nodes:
            if (nodo1 != nodo2) and (grafo.has_edge(nodo1, nodo2) is False):
                q1 = grafo.degree(nodo1)
                q2 = grafo.degree(nodo2)
                if (q1 + q2) < n:
                    print("Segun el Teorema de Ore el Grafo no es Hamiltoniano")
                    return

    print("El Grafo posee Camino y Circuito Hamiltoniano")
    return


def hamiltoniano_digrafo(grafo):
    n = grafo.number_of_nodes()
    if not nx.algorithms.is_strongly_connected(grafo):
        print("No se puede comprobar que el grafo sea Hamiltoniano ya que no es conexo")
        return

    if n < 3:
        print("El Grafo no es Hamiltoniano ya que no posee nodos suficientes")
        return

    for nodo in grafo.nodes():
        if grafo.degree(nodo) < (n / 2):
            print("Segun el Teorema de Ghouila-Houiri el Grafo no es Hamiltoniano")
            return

    for nodo1 in grafo.nodes():
        for nodo2 in grafo.nodes:
            if (nodo1 != nodo2) and (grafo.has_edge(nodo1, nodo2) is False):
                q1 = grafo.degree(nodo1)
                q2 = grafo.degree(nodo2)
                if (q1 + q2) < n:
                    print("Segun el Teorema de Meyniel el Grafo no es Hamiltoniano")
                    return

    print("El Grafo posee Camino y Circuito Hamiltoniano")
    return


def planar(grafo):
    if nx.algorithms.check_planarity(grafo):
        print("")
        print("El Grafo Es Planar")


def coloreado_nodos(grafo):
    colores = {}
    nodos = grafo.nodes()
    for u in nodos:
        colores_vecinos = {colores[v] for v in grafo[u] if v in colores}
        for color in itertools.count():
            if color not in colores_vecinos:
                break
        colores[u] = color
    return colores


def dijkstra(grafo, aristas_camino):
    a = input("ingrese el nodo de salida para el camino mas corto: ")
    b = input("Ingrese el nodo de destino para el camino mas corto: ")
    peso, nodo = nx.shortest_paths.single_source_dijkstra(grafo, a, b)
    i = 1
    for u in nodo:
        j = 1
        for v in nodo:
            if u != v and j == (i+1):
                if grafo.has_edge(u, v):
                    aristas_camino.append((u, v))
            j = j+1
        i = i + 1
        print(aristas_camino)
    print("El camino mas corto entre los nodos es: " + str(nodo))
    print("El peso del Camino es de: " + str(peso))
    return aristas_camino


def quitar_cuadro():
    ax = plt.axes()
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
'''

if __name__ == '__main__':

    app = QtWidgets.QApplication([])

    application = mywindow()

    application.show()

    app.exec_()

'''    while True:
        s = input("Que tipo desea construir (1-Grafo/2-Digrafo): ")
        aristas_camino = []
        if s == "1":
            grafo = nx.Graph()
            ingresar_nodos(grafo)
            ingresar_arista(grafo)
            dijkstra(grafo, aristas_camino)
            circuito_euleriano(grafo)
            camino_euleriano(grafo)
            hamiltoniano_grafo(grafo)
            planar(grafo)
            mostar_grafo(grafo, aristas_camino)
            break
        elif s == "2":
            grafo = nx.DiGraph()
            ingresar_nodos(grafo)
            ingresar_arista(grafo)
            dijkstra(grafo, aristas_camino)
            circuito_euleriano(grafo)
            camino_euleriano(grafo)
            hamiltoniano_digrafo(grafo)
            planar(grafo)
            mostar_grafo(grafo, aristas_camino)
            break'''
