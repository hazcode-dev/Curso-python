# ==========================================
# TEMA 4: LA FUNCIÓN input()
# ==========================================

# La función input() permite al usuario ingresar datos desde la consola.

# Ejemplo básico:
nombre = input("¿Cuál es tu nombre? ")
print("Hola", nombre)

# ==========================================
# 🔹 input() siempre devuelve un string (cadena de texto)
# ==========================================
# Si necesitas trabajar con números, convierte el resultado con int() o float()

# Ejemplo: pedir edad y convertirla
edad = input("¿Cuántos años tienes? ")
print("Tipo original:", type(edad))  # <class 'str'>

edad = int(edad)  # conversión a entero
print("Tipo convertido:", type(edad))  # <class 'int'>
print(f"El próximo año tendrás {edad + 1} años.")

# Puedes hacer todo en una sola línea:
altura = float(input("¿Cuál es tu altura en metros? "))
print(f"Tu altura es {altura} m")

# ==========================================
# 🔹 Interacción más elaborada
# ==========================================
curso = input("¿Qué curso estás llevando actualmente? ")
universidad = input("¿En qué universidad estudias? ")

print(f"Estás llevando {curso} en {universidad}.")

# ==========================================
# ⚠️ Errores comunes con input()
# ==========================================
# Si colocas letras cuando esperas números, fallará:
# edad = int(input("Edad: "))  # Si escribes "veinte", error

# Siempre valida o asume que el usuario ingresará datos correctos por ahora.

# ==========================================
# 🧪 PRUEBA RÁPIDA
# 1. Pide el nombre completo del usuario y su año de nacimiento.
# 2. Calcula su edad aproximada (año actual - nacimiento).
# 3. Muestra un mensaje como:
#    Hola Juan, tu edad estimada es 23 años.
