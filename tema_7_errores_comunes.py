# ==========================================
# TEMA 7: ERRORES COMUNES EN PYTHON
# ==========================================

# Todos los programadores cometen errores. Lo importante es saber cómo
# entenderlos y corregirlos.

# ==========================================
# 🔹 1. Error de sintaxis (SyntaxError)
# ==========================================

# print("Hola"   ❌ Falta el paréntesis de cierre

# Solución:
print("Hola")  # ✅

# ==========================================
# 🔹 2. Error de nombre (NameError)
# ==========================================

# print(edad)  ❌ No se ha definido la variable 'edad'

# Solución:
edad = 20
print(edad)  # ✅

# ==========================================
# 🔹 3. Error de tipo (TypeError)
# ==========================================

# nombre = "Juan"
# edad = 22
# print(nombre + edad)  ❌ No se puede sumar str + int

# Solución:
# print(nombre + str(edad))  # ✅ - es codigo pero para que no de problemas
# lo puse como comentario

# ==========================================
# 🔹 4. Error de valor (ValueError)
# ==========================================

# int("hola")  ❌ No se puede convertir texto no numérico a entero

# Solución:
numero = "5"
print(int(numero))  # ✅

# ==========================================
# 🔹 5. División por cero (ZeroDivisionError)
# ==========================================

# resultado = 10 / 0  ❌ No se puede dividir entre cero

# Solución:
divisor = 2
if divisor != 0:
    resultado = 10 / divisor
    print(resultado)
else:
    print("No se puede dividir entre cero")

# ==========================================
# 🔹 6. Error de índice (IndexError)
# ==========================================

lista = [1, 2, 3]
# print(lista[5])  ❌ No existe ese índice

print(lista[0])  # ✅
