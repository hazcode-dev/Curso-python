# ==========================================
# TEMA 5: CONVERSIÓN DE TIPOS DE DATOS
# ==========================================

# En Python puedes convertir entre diferentes tipos de datos usando
# funciones  integradas.

# ==========================================
# 🔹 int() → convierte a entero (si es posible)
# ==========================================
numero_texto = "10"
numero_entero = int(numero_texto)
print("Texto convertido a entero:", numero_entero)

# También funciona con floats en forma de texto:
decimal_texto = "3.14"
decimal_entero = int(float(decimal_texto))  # primero convertir a float
print("Decimal redondeado hacia abajo:", decimal_entero)

# ==========================================
# 🔹 float() → convierte a número decimal
# ==========================================
numero = "5.89"
decimal = float(numero)
print("Texto a decimal:", decimal)

# ==========================================
# 🔹 str() → convierte cualquier tipo a cadena
# ==========================================
edad = 22
mensaje = "Tu edad es " + str(edad)
print(mensaje)

# ==========================================
# 🔹 bool() → convierte a booleano
# ==========================================
# Regla general:
# - False: 0, "", None, [], {}, ()
# - True: cualquier otro valor

print(bool(0))  # False
print(bool(1))  # True
print(bool(""))  # False
print(bool("hola"))  # True

# ==========================================
# 🔹 input() + conversión combinada
# ==========================================
# Pedir datos numéricos y operar con ellos

n1 = float(input("Ingresa el primer número: "))
n2 = float(input("Ingresa el segundo número: "))
suma = n1 + n2
print(f"La suma de ambos es: {suma}")

# ==========================================
# 🧪 PRUEBA RÁPIDA
# 1. Pide al usuario dos números enteros.
# 2. Convierte los valores y muestra:
#    - Suma
#    - Resta
#    - Multiplicación
#    - División (formato decimal, no redondeado)
