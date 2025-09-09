class Games:
    def piedra_papel_tijera(self, jugador1:str, jugador2:str) ->str:
        """
        Determina el ganador del juego piedra, papel o tijera.
        
        Args:
            jugador1 (str): Elección del jugador 1 ("piedra", "papel", "tijera")
            jugador2 (str): Elección del jugador 2 ("piedra", "papel", "tijera")
            
        Returns:
            str: "jugador1", "jugador2" o "empate"
            
        Reglas:
            - Piedra vence a tijera
            - Tijera vence a papel
            - Papel vence a piedra
        """
        jugador1 = jugador1.lower() #Para que lea las minusculas y las mayusculas 
        jugador2 = jugador2.lower()

        reglas = {
            "piedra":"tijera",
            "tijera":"papel",
            "papel":"piedra"
        }
        if jugador1 == jugador2:
            return "empate"
        elif reglas.get(jugador1) == jugador2:
            return "jugador1"
        elif reglas.get(jugador2) == jugador1:
            return "jugador2"
        else: 
            return "invalid" 
        pass
    
    def adivinar_numero_pista(self, numero_secreto, intento):
        """
        Proporciona pistas para un juego de adivinanza de números.
        
        Args:
            numero_secreto (int): El número que se debe adivinar
            intento (int): El número propuesto por el jugador
            
        Returns:
            str: "correcto", "muy alto" o "muy bajo"
        """

        if numero_secreto == intento:
            return "correcto"
        elif intento > numero_secreto:
            return "muy alto"
        elif intento < numero_secreto:
            return "muy bajo"
        else:
            return "invalido"
    
    def ta_te_ti_ganador(self, tablero:list) -> str:
        """
        Verifica si hay un ganador en un tablero de tic-tac-toe.
        
        Args:
            tablero (list): Matriz 3x3 con valores "X", "O" o " " (espacio vacío)
            
        Returns:
            str: "X", "O", "empate" o "continua"
            
        Ejemplo:
            [["X", "X", "X"],
             ["O", "O", " "],
             [" ", " ", " "]] -> "X"
        """
        for row in tablero:
            if row[0] == row[1] == row[2] and row[0] != ' ':
                return row[0]
        
        for col in range(3):
            if tablero[0][col] == tablero[1][col] == tablero[2][col] and tablero[0][col] != ' ':
                return tablero[0][col]
        
        if tablero[0][0] == tablero[1][1] == tablero[2][2] and tablero[0][0] != ' ': #holaaaaaaaa
            return tablero [0][0]
        
        if tablero[0][2] == tablero[1][1] == tablero[2][0] and tablero [0][2] != ' ':
            return tablero[0][2]
        
        for row in tablero:
            for cell in row:
                if cell == ' ':
                    return "continua"
        
        return "empate"
    
    def generar_combinacion_mastermind(self, longitud: int , colores_disponibles: list) -> list:
        import random
        """
        Genera una combinación aleatoria para el juego Mastermind.
        
        Args:
            longitud (int): Número de posiciones en la combinación
            colores_disponibles (list): Lista de colores disponibles
            
        Returns:
            list: Combinación de colores de la longitud especificada
            
        Ejemplo:
            generar_combinacion_mastermind(4, ["rojo", "azul", "verde"]) 
            -> ["rojo", "azul", "rojo", "verde"]
        """
        return [random.choice(colores_disponibles) for _ in range(longitud)]
        
    
    def validar_movimiento_torre_ajedrez(self, desde_fila: int, desde_col:int , hasta_fila:int, hasta_col:int, tablero:list) -> bool:
        """
        Valida si un movimiento de torre en ajedrez es legal.
        
        Args:
            desde_fila (int): Fila inicial (0-7)
            desde_col (int): Columna inicial (0-7)
            hasta_fila (int): Fila destino (0-7)
            hasta_col (int): Columna destino (0-7)
            tablero (list): Matriz 8x8 representando el tablero
            
        Returns:
            bool: True si el movimiento es válido, False si no
            
        Reglas:
            - La torre se mueve horizontal o verticalmente
            - No puede saltar sobre otras piezas
        """
        if not ( 0 <= desde_fila < 8 and 0 <= desde_col < 8 and 
                0 <= hasta_fila <8 and 0<= hasta_col < 8 ):
            return False 
        
        if desde_fila == hasta_fila and desde_col == hasta_col:
            return False 
            
        if desde_fila != hasta_fila and desde_col != hasta_col:
            return False
        
        if desde_fila == hasta_fila:
            paso = 1 if hasta_col > desde_col else -1 
            for col in range (desde_col + paso, hasta_col, paso):
                if tablero[desde_fila] [col] != " ":
                    return False 
        elif desde_col == hasta_col:
            paso = 1 if hasta_fila > desde_fila else -1 
            for fila in range(desde_fila + paso, hasta_fila, paso):
                if tablero [fila][desde_col] != " ":
                    return False 
        return True 