class Data:
    """
    Clase con métodos para operaciones y manipulaciones de estructuras de datos.
    Incluye implementaciones y algoritmos para arreglos, listas y otras estructuras.
    """
    
    def invertir_lista(self, lista):
        """
        Invierte el orden de los elementos en una lista sin usar reversed() o lista[::-1].
        
        Args:
            lista (list): Lista a invertir
            
        Returns:
            list: Lista con los elementos en orden inverso      
        """
        invertida = []
        for i in range(len(lista) - 1, -1, -1): 
            invertida.append(lista[i])
        return invertida
    
                             
    
    def buscar_elemento(self, lista, elemento):
        """
        Busca un elemento en una lista y devuelve su índice (o -1 si no existe).
        Implementación manual sin usar index().
        
        Args:
            lista (list): Lista donde buscar
            elemento: Elemento a buscar
            
        Returns:
            int: Índice del elemento o -1 si no se encuentra
        """
        for i in range(len(lista)):
            if lista[i] == elemento:
                return i
        return -1

    def eliminar_duplicados(self, lista:list) -> list:
        """
        Elimina elementos duplicados de una lista sin usar set().
        Mantiene el orden original de aparición.
        
        Args:
            lista (list): Lista con posibles duplicados
            
        Returns:
            list: Lista sin elementos duplicados 
        """
        resultado = []
        visto = []
        for i in lista:
            clave=(type(i), i)
            if clave not in resultado:
                resultado.append(clave)
                visto.append(i)
        return visto
    
    def merge_ordenado(self, lista1: list, lista2: list)-> list:
        """
        Combina dos listas ordenadas en una sola lista ordenada.
        
        Args:
            lista1 (list): Primera lista ordenada
            lista2 (list): Segunda lista ordenada
            
        Returns:
            list: Lista combinada y ordenada
        """
        lista_Ordenada= lista1 +lista2
        return sorted(lista_Ordenada)
    
    def rotar_lista(self, lista, k):
        """
        Rota los elementos de una lista k posiciones a la derecha.
        
        Args:
            lista (list): Lista a rotar
            k (int): Número de posiciones a rotar
            
        Returns:
            list: Lista rotada
        """
        n = len(lista) #mirar cuantos elementos tiene la lista 
        if (n>0):
            k = k % n # asegurar que k este dentro del rango de la longitud de la lista
            return lista[n-k:] + lista[:n-k]
        else:
            return lista
    
    def encuentra_numero_faltante(self, lista:list) -> int:
        """
        Encuentra el número faltante en una lista de enteros del 1 al n.
        
        Args:
            lista (list): Lista de enteros del 1 al n con un número faltante
            
        Returns:
            int: El número que falta en la secuencia
        """
        n = len(lista) + 1
        suma = n * (n+1) //  2
        suma_lista = sum(lista)
        return suma-suma_lista
    
    
    def es_subconjunto(self, conjunto1, conjunto2):
        """
        Verifica si conjunto1 es subconjunto de conjunto2 sin usar set.
        
        Args:
            conjunto1 (list): Posible subconjunto
            conjunto2 (list): Conjunto principal
            
        Returns:
            bool: True si conjunto1 es subconjunto de conjunto2, False en caso contrario
        """
        for elemento in conjunto1:
            if elemento not in conjunto2:
                return False 
        return True 
    
    def implementar_pila(self):
        """
        Implementa una estructura de datos tipo pila (stack) usando listas.
        
        Returns:
            dict: Diccionario con métodos push, pop, peek y is_empty
        """
        pila = []

        def push(elemento):
            pila.append(elemento)

        def pop():
            if pila:
                return pila.pop()
            return None 
        def peek ():
            if pila:
                return pila[-1]
            return None
        def is_empty():
            return len(pila) == 0
        
        return {
            'push': push,
            'pop': pop,
            'peek': peek,
            'is_empty': is_empty
        }
    
    def implementar_cola(self):
        """
        Implementa una estructura de datos tipo cola (queue) usando listas.
        
        Returns:
            dict: Diccionario con métodos enqueue, dequeue, peek y is_empty
        """
        cola =[]
        def enqueue(elemento):
            cola.append(elemento)

        def dequeue():
            if cola:
                return cola.pop(0)
            return None 
        def peek():
            if cola: 
                return cola[0]
            return None 
        def is_empty():
            return len(cola) == 0 
        
        return {
            'enqueue' : enqueue,
            'dequeue' : dequeue,
            'peek' : peek,
            'is_empty': is_empty
        }
    
    def matriz_transpuesta(self, matriz:list) -> list:
        """
        Calcula la transpuesta de una matriz.
        
        Args:
            matriz (list): Lista de listas que representa una matriz
            
        Returns:
            list: Matriz transpuesta
        """
        try:
            return [[fila[i] for fila in matriz] for i in range(len(matriz[0]))]
        except (TypeError, IndexError):
            return []