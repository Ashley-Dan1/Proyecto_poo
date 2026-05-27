# =====================================================================
# CÓDIGO PURO DE LOS EJERCICIOS - BLOQUE 16: ARCHIVOS (I/O)
# =====================================================================
import os

# ---------------------------------------------------------------------
# EJERCICIO 1: Escribe "Hola Mundo" en un archivo llamado "datos.txt".
# ---------------------------------------------------------------------
class EscritorArchivos:
    def __init__(self, nombre_archivo: str):
        self.ruta = nombre_archivo

    def escribir_linea_texto(self, contenido: str):
        print("💾 PERSISTENCIA DE DATOS: ESCRITURA EN DISCO ('w')")
        print("--------------------------------------------------")
        print(f"Destino: '{self.ruta}' | Contenido a guardar: '{contenido}'")
        
        # El administrador de contexto 'with' garantiza el cierre automático del flujo
        with open(self.ruta, "w", encoding="utf-8") as archivo:
            archivo.write(contenido)
            
        print("✅ ¡Archivo creado y guardado con éxito en la memoria del servidor!")


class GestorEscritura:
    @staticmethod
    def ejecutar_demostracion(nombre_archivo: str, texto: str):
        escritor = EscritorArchivos(nombre_archivo)
        escritor.escribir_linea_texto(texto)


# ---------------------------------------------------------------------
# EJERCICIO 2: Lee el archivo "datos.txt" e imprime su contenido.
# ---------------------------------------------------------------------
class LectorArchivos:
    def __init__(self, nombre_archivo: str):
        self.ruta = nombre_archivo

    def leer_contenido_completo(self):
        print("📖 LECTURA DE DATOS PERSISTENTES ('r')")
        print("--------------------------------------------------")
        print(f"Intentando leer desde el origen: '{self.ruta}'")
        
        # Validamos primero la existencia física del archivo para mitigar errores
        if not os.path.exists(self.ruta):
            print(f"❌ Error controlado: El archivo '{self.ruta}' no existe en este directorio.")
            return None
            
        with open(self.ruta, "r", encoding="utf-8") as archivo:
            contenido_leido = archivo.read()
            
        print("➡️ Contenido recuperado desde el disco duro:")
        print(f"--- INICIO ARCHIVO ---\n{contenido_leido}\n--- FIN ARCHIVO ---")
        return contenido_leido


class GestorLectura:
    @staticmethod
    def ejecutar_calculo(nombre_archivo: str):
        lector = LectorArchivos(nombre_archivo)
        lector.leer_contenido_completo()


# ---------------------------------------------------------------------
# EJERCICIO 3: Añade una nueva línea al archivo sin borrar lo anterior.
# ---------------------------------------------------------------------
class AnexadorArchivos:
    def __init__(self, nombre_archivo: str):
        self.ruta = nombre_archivo

    def agregar_linea_final(self, contenido_nuevo: str):
        print("➕ AMPLIACIÓN DE ARCHIVOS: MODO ANEXAR ('a')")
        print("--------------------------------------------------")
        print(f"Modificando: '{self.ruta}' | Línea a incorporar: '{contenido_nuevo}'")
        
        # El modo 'a' (append) se posiciona al final del archivo sin destruir el contenido previo
        with open(self.ruta, "a", encoding="utf-8") as archivo:
            # Aseguramos un salto de línea previo para mantener el orden secuencial
            archivo.write("\n" + contenido_nuevo)
            
        print("✅ ¡Línea añadida al final del archivo existente de manera segura!")


class GestorAnexado:
    @staticmethod
    def ejecutar_analisis(nombre_archivo: str, texto_anexo: str):
        anexador = AnexadorArchivos(nombre_archivo)
        anexador.agregar_linea_final(texto_anexo)


# =====================================================================
# FUNCIONES DISPARADORAS (Conectan con el controlador de Flask)
# =====================================================================

def ejecutar_ejercicio1(nombre, texto):
    GestorEscritura.ejecutar_demostracion(nombre, texto)

def ejecutar_ejercicio2(nombre):
    GestorLectura.ejecutar_calculo(nombre)

def ejecutar_ejercicio3(nombre, texto_anexo):
    GestorAnexado.ejecutar_analisis(nombre, texto_anexo)