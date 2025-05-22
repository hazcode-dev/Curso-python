# ==========================================
# TEMA 6: COMENTARIOS Y ESTILO DE CÓDIGO (PEP 8)
# ==========================================

# Los comentarios sirven para explicar el código.
# No se ejecutan y comienzan con el símbolo #

# Esto es un comentario de una línea
print("Hola")  # También se puede comentar al final de una línea

# ==========================================
# 🔹 Comentarios multilínea (uso común, aunque no oficial)
# ==========================================
# Puedes escribir varios comentarios seguidos:
# Esta función muestra un mensaje
# con el nombre del usuario
# y su edad actual.

# También puedes usar comillas triples para documentar funciones o clases
# (docstrings):


def saludar(nombre):
    """
    Esta función saluda al usuario por su nombre.
    """
    print(f"Hola, {nombre}")


# ==========================================
# 🔹 ¿Qué es PEP 8?
# ==========================================
# PEP 8 es la guía oficial de estilo de Python.
# Ayuda a que tu código sea limpio, legible y profesional.

# ✅ Reglas más importantes:

# 1. Nombres de variables: minúsculas + guión bajo
edad_usuario = 25

# 2. Indentación: 4 espacios por nivel
if edad_usuario >= 18:
    print("Eres mayor de edad")

# 3. Longitud de línea: máximo 79 caracteres por línea

# 4. Líneas en blanco:
#   - 2 líneas en blanco entre funciones
#   - 1 línea entre métodos en una clase

# 5. Espacios:
# ❌ NO
# suma= a+ b
# ✅ SÍ
# suma = a + b

# ==========================================
# 🔹 Herramientas útiles en VS Code
# ==========================================
# Puedes instalar extensiones como:
# - Python (Microsoft)
# - Pylance
# - Black Formatter (autoformatea el código)
# - flake8 o pylint (detecta errores de estilo)

# Atajo útil:
# SHIFT + ALT + F → Formatear archivo automáticamente

# ==========================================
# 🧪 PRUEBA RÁPIDA
# 1. Escribe una pequeña función que reciba nombre y edad, y devuelva un
# saludo.
# 2. Aplica buenas prácticas PEP8:
#    - Indentación correcta
#    - Comentarios descriptivos
#    - Buenos nombres de variables
