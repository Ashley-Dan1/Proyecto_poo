# =====================================================================
# CÓDIGO PURO DE LOS EJERCICIOS - BLOQUE 7: LISTAS
# =====================================================================

# ---------------------------------------------------------------------
# EJERCICIO 1: Crea una lista con 5 frutas, accede a la primera y última.
# ---------------------------------------------------------------------
class ContenedorFrutas:
    def __init__(self, lista_inicial: list):
        # Aseguramos que se guarde la lista provista
        self.frutas = lista_inicial

    def acceder_extremos(self):
        print("🍎 CONTROL DE INDEXACIÓN EN LISTAS")
        print("--------------------------------------------------")
        print(f"Lista completa de frutas: {self.frutas}")
        
        # Acceso por índice positivo (primero) e índice negativo (último)
        primera = self.frutas[0]
        ultima = self.frutas[-1]
        
        print(f"🥇 Primera fruta (Índice 0) : {primera}")
        print(f"🏁 Última fruta (Índice -1) : {ultima}")


class GestorFrutas:
    @staticmethod
    def ejecutar_demostracion(lista_web: list):
        contenedor = ContenedorFrutas(lista_web)
        contenedor.acceder_extremos()


# ---------------------------------------------------------------------
# EJERCICIO 2: Modifica el tercer elemento de la lista y añade una nueva fruta al final.
# ---------------------------------------------------------------------
class ManipuladorFrutas:
    def __init__(self, lista_inicial: list):
        self.frutas = list(lista_inicial)  # Clonamos para no alterar el original

    def modificar_y_expandir(self, nueva_fruta_pos3: str, fruta_final: str):
        print("⚙️ ALTERACIÓN Y MUTABILIDAD DE ELEMENTOS")
        print("--------------------------------------------------")
        print(f"Estado inicial: {self.frutas}")
        
        # Modificación del tercer elemento (Índice 2)
        self.frutas[2] = nueva_fruta_pos3
        print(f"🔄 Reemplazado índice 2 por '{nueva_fruta_pos3}': {self.frutas}")
        
        # Inserción al final usando el método append
        self.frutas.append(fruta_final)
        print(f"➕ Añadida fruta al final (.append): {self.frutas}")


class GestorModificaciones:
    @staticmethod
    def ejecutar_calculo(lista_base: list, reemplazo: str, adicional: str):
        manipulador = ManipuladorFrutas(lista_base)
        manipulador.modificar_y_expandir(reemplazo, adicional)


# ---------------------------------------------------------------------
# EJERCICIO 3: Elimina una fruta específica por su nombre y la última usando .pop().
# ---------------------------------------------------------------------
class DepuradorFrutas:
    def __init__(self, lista_inicial: list):
        self.frutas = list(lista_inicial)

    def extraer_elementos(self, fruta_a_remover: str):
        print("🗑️ ELIMINACIÓN DE NODOS EN LISTAS (.REMOVE Y .POP)")
        print("--------------------------------------------------")
        print(f"Lista de partida: {self.frutas}")
        
        # Eliminación por valor específico con control de existencia
        if fruta_a_remover in self.frutas:
            self.frutas.remove(fruta_a_remover)
            print(f"❌ Eliminada '{fruta_a_remover}' (.remove): {self.frutas}")
        else:
            print(f"⚠️ La fruta '{fruta_a_remover}' no se encontró para ser removida.")
            
        # Extracción del último elemento mediante pop
        if len(self.frutas) > 0:
            fruta_removida = self.frutas.pop()
            print(f"🍿 Extraída la última fruta (.pop): '{fruta_removida}'")
            print(f"📋 Estado final de la lista: {self.frutas}")
        else:
            print("⚠️ La lista está vacía, no se puede ejecutar .pop()")


class GestorDepuracion:
    @staticmethod
    def ejecutar_analisis(lista_base: list, fruta_eliminar: str):
        depurador = DepuradorFrutas(lista_base)
        depurador.extraer_elementos(fruta_eliminar)


# =====================================================================
# FUNCIONES DISPARADORAS (Conectan con el controlador de Flask)
# =====================================================================

def ejecutar_ejercicio1(lista):
    GestorFrutas.ejecutar_demostracion(lista)

def ejecutar_ejercicio2(lista, reemplazo, adicional):
    GestorModificaciones.ejecutar_calculo(lista, reemplazo, adicional)

def ejecutar_ejercicio3(lista, fruta_eliminar):
    GestorDepuracion.ejecutar_analisis(lista, fruta_eliminar)