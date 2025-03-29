from graphviz import Digraph, backend
import os


class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None
        self.padre = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None
        self.cantidad = 0
        self.orden_insercion = []  # Nueva lista para guardar el orden de inserción

    def insertar(self, valor):
        # Validar si el valor ya existe en el árbol
        if valor in self.obtener_elementos():
            print(f"El valor {valor} ya existe en el árbol. Por favor, inserte otro número.")
            return

        self.orden_insercion.append(valor)  # Guardar el orden de inserción
        # Crear un nuevo nodo con el valor dado
        nuevo_nodo = Nodo(valor)
        self.cantidad += 1
        
        if not self.raiz:
            # Si el árbol está vacío, el nuevo nodo se convierte en la raíz
            self.raiz = nuevo_nodo
            self.visualizar_arbol()  # Generar la imagen del árbol
            return
            
        actual = self.raiz
        while True:
            if valor < actual.valor:
                if actual.izquierda is None:
                    # Insertar el nuevo nodo en el subárbol izquierdo
                    actual.izquierda = nuevo_nodo
                    nuevo_nodo.padre = actual
                    break
                actual = actual.izquierda
            else:
                if actual.derecha is None:
                    # Insertar el nuevo nodo en el subárbol derecho
                    actual.derecha = nuevo_nodo
                    nuevo_nodo.padre = actual
                    break
                actual = actual.derecha

        self.visualizar_arbol()  # Generar la imagen del árbol

    def obtener_elementos(self):
        # Obtener los elementos del árbol en orden ascendente
        elementos = []
        def inorden(nodo):
            if nodo:
                inorden(nodo.izquierda)
                elementos.append(nodo.valor)
                inorden(nodo.derecha)
        inorden(self.raiz)
        return elementos

    def obtener_elementos_insercion(self):
        return self.orden_insercion

    def cantidad_elementos(self):
        # Devolver la cantidad de elementos en el árbol
        return self.cantidad

    def visualizar_arbol(self, ruta_guardado='app/static/arbol_binario'):
        if not self.raiz:
            return "Árbol vacío"

        dot = Digraph()
        dot.attr('node', shape='circle')

        def agregar_nodos(dot, nodo):
            if nodo:
                dot.node(str(nodo.valor))
                if nodo.izquierda:
                    dot.edge(str(nodo.valor), str(nodo.izquierda.valor))
                    agregar_nodos(dot, nodo.izquierda)
                if nodo.derecha:
                    dot.edge(str(nodo.valor), str(nodo.derecha.valor))
                    agregar_nodos(dot, nodo.derecha)

        agregar_nodos(dot, self.raiz)
        try:
            # Asegúrate de que la carpeta 'static' exista
            os.makedirs(os.path.dirname(ruta_guardado), exist_ok=True)
            dot.render(ruta_guardado, format='png', view=False)
            return f"Visualización generada y guardada como '{ruta_guardado}.png'"
        except backend.ExecutableNotFound:
            return "Error: Graphviz no está instalado o no está en el PATH del sistema."

    def borrar_arbol(self):
        self.raiz = None
        self.cantidad = 0
        self.orden_insercion = []  # Limpiar también el orden de inserción
        self.visualizar_arbol()  # Generar la imagen del árbol vacío
        return "Árbol binario borrado completamente"
