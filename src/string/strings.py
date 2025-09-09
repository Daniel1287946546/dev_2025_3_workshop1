class Strings:
    """
    Clase con métodos para manipulación y operaciones con cadenas de texto.
    Incluye funciones para manipular, validar y transformar strings.
    """
    
    def es_palindromo(self, texto):
        """
        Verifica si una cadena es un palíndromo (se lee igual de izquierda a derecha y viceversa).
        
        Args:
            texto (str): Cadena a verificar
            
        Returns:
            bool: True si es palíndromo, False en caso contrario
        """
        texto_limpio = ''.join(c.lower() for c in texto if c.isalnum())
        return texto_limpio == texto_limpio[::-1] 
    
    def invertir_cadena(self, texto):
        """
        Invierte una cadena de texto sin usar slicing ni reversed().
        
        Args:
            texto (str): Cadena a invertir
            
        Returns:
            str: Cadena invertida
        """
        invertida = ""
        for i in range(len(texto) -1,-1,-1):
            invertida += texto[i]
        return invertida
    
    def contar_vocales(self, texto):
        """
        Cuenta el número de vocales en una cadena.
        
        Args:
            texto (str): Cadena para contar vocales
            
        Returns:
            int: Número de vocales en la cadena
        """
        vocales = "aeiouAEIOU"
        contador = 0 
        if not texto:
            return 0
        for letra in texto: 
            if letra in vocales:
                contador += 1
        return contador
    
    def contar_consonantes(self, texto):
        """
        Cuenta el número de consonantes en una cadena.
        
        Args:
            texto (str): Cadena para contar consonantes
            
        Returns:
            int: Número de consonantes en la cadena
        """
        vocales ="aeiouAEIOU"
        contador = 0 
        for letra in texto:
            if letra.isalpha() and letra not  in vocales:
                contador += 1 
        return contador 
    
    def es_anagrama(self, texto1, texto2):
        """
        Verifica si dos cadenas son anagramas (contienen exactamente los mismos caracteres).
        
        Args:
            texto1 (str): Primera cadena
            texto2 (str): Segunda cadena
            
        Returns:
            bool: True si son anagramas, False en caso contrario
        """
        t1 = texto1.replace(" ", "").lower()
        t2 = texto2.replace(" ", "").lower()

        return sorted(t1) == sorted(t2)
    
    def contar_palabras(self, texto):
        """
        Cuenta el número de palabras en una cadena.
        
        Args:
            texto (str): Cadena para contar palabras
            
        Returns:
            int: Número de palabras en la cadena
        """
        palabras = texto.split()
        return len(palabras)

    
    def palabras_mayus(self, texto):
        """
        Pon en Mayuscula la primera letra de cada palabra en una cadena.
        
        Args:
            texto (str): Cadena
            
        Returns:
            str: Cadena con la primera letra de cada palabra en mayúscula
        """
        resultado = ""
        nueva_palabra = True
        
        for c in texto:
            if c.isspace():
                resultado += c
                nueva_palabra = True
            elif nueva_palabra:
                resultado += c.upper()
                nueva_palabra = False
            else:
                resultado += c.lower()
        return resultado 
        


    
    def eliminar_espacios_duplicados(self, texto):
        """
        Elimina espacios duplicados en una cadena.
        
        Args:
            texto (str): Cadena con posibles espacios duplicados
            
        Returns:
            str: Cadena sin espacios duplicados
        """
        return ' '.join(texto.split())
    
    def es_numero_entero(self, texto):
        """
        Verifica si una cadena representa un número entero sin usar isdigit().
        
        Args:
            texto (str): Cadena a verificar
            
        Returns:
            bool: True si la cadena representa un número entero, False en caso contrario
        """
        try: 
            int(texto)
            return True 
        except ValueError:
            return False
    
    def cifrar_cesar(self, texto, desplazamiento):
        """
        Aplica el cifrado César a una cadena de texto.
        
        Args:
            texto (str): Cadena a cifrar
            desplazamiento (int): Número de posiciones a desplazar cada letra
            
        Returns:
            str: Cadena cifrada
        """
        resultado = ""

        for caracter in texto:
            if caracter.isalpha():
                base = ord('A') if caracter.isupper() else ord('a')
                nuevo_codigo = (ord(caracter) - base + desplazamiento) % 26 + base
                resultado += chr(nuevo_codigo)
            else:
                resultado += caracter  # conservar espacios, signos, etc.

        return resultado

    
    def descifrar_cesar(self, texto, desplazamiento):
        """
        Descifra una cadena cifrada con el método César.
        
        Args:
            texto (str): Cadena cifrada
            desplazamiento (int): Número de posiciones que se desplazó cada letra
            
        Returns:
            str: Cadena descifrada
        """
        resultado = ""

        for caracter in texto:
            if caracter.isalpha():
                base = ord('A') if caracter.isupper() else ord('a')
                nuevo_codigo = (ord(caracter) - base - desplazamiento) % 26 + base
                resultado += chr(nuevo_codigo)
            else:
                resultado += caracter  # conservar espacios, signos, etc.

        return resultado

    
    def encontrar_subcadena(self, texto, subcadena):
        """
        Encuentra todas las posiciones de una subcadena en un texto sin usar find() o index().
        
        Args:
            texto (str): Cadena principal
            subcadena (str): Subcadena a buscar
            
        Returns:
            list: Lista con las posiciones iniciales de cada ocurrencia
        """
        if not subcadena:
            return []
        
        posiciones = []
        longitud_sub = len(subcadena)
        longitud_texto = len(texto)

        for i in range(longitud_texto - longitud_sub + 1):
            if texto[i:i + longitud_sub] == subcadena:
                posiciones.append(i)

        return posiciones