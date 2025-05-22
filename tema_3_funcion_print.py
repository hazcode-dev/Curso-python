# ==========================================
# TEMA 3: LA FUNCIÓN print()
# ==========================================

# La función print() se utiliza para mostrar información en la consola.

# Ejemplo básico:
print("Hola, mundo")

# También puedes mostrar varias cosas separadas por comas:
nombre = "Juan"
edad = 22
print("Mi nombre es", nombre, "y tengo", edad, "años.")

# ==========================================
# 🔹 Uso de f-strings (formato recomendado desde Python 3.6)
# ==========================================
# Permite insertar variables dentro del texto usando { }

print(f"Hola, me llamo {nombre} y tengo {edad} años.")

# Puedes también realizar operaciones dentro del f-string:
print(f"El próximo año tendré {edad + 1} años.")

# ==========================================
# 🔹 Salto de línea (\n) y tabulación (\t)
# ==========================================
print("Primera línea\nSegunda línea")
print("Nombre:\tJuan")
print("Edad:\t22")

# ==========================================
# 🔹 Concatenación con +
# ==========================================
# Solo funciona con cadenas (str)

curso = "Python"
print("Estoy aprendiendo " + curso)

# Si combinas cadenas con enteros sin conversión → error:
# print("Tengo " + edad + " años")  ❌ ERROR

# Solución: convertir a cadena con str()
print("Tengo " + str(edad) + " años")  # ✅

# ==========================================
# 🧪 PRUEBA RÁPIDA
# 1. Crea tres variables: nombre, carrera y universidad.
# 2. Muestra un mensaje con f-string como:
#    Hola, soy Juan, estudio Ingeniería Industrial en la USIL.
