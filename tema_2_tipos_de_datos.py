# ==========================================
# TEMA 2: TIPOS DE DATOS EN PYTHON
# ==========================================

# En Python, existen varios tipos de datos básicos o "primitivos"
# que se usan para almacenar información fundamental.

# 🔹 1. Enteros (int)
# Son números enteros positivos o negativos, sin decimales.

numero_entero = 10
print("Número entero:", numero_entero)

# 🔹 2. Flotantes (float)
# Son números con decimales.

numero_decimal = 3.1416
print("Número flotante:", numero_decimal)

# 🔹 3. Cadenas (str)
# Texto encerrado entre comillas simples o dobles.

nombre = "Juan"
mensaje = "Bienvenido"
print("Nombre:", nombre)
print("Mensaje:", mensaje)

# 🔹 4. Booleanos (bool)
# Solo tienen dos valores: True (verdadero) o False (falso)

es_activo = True
esta_inscrito = False
print("¿Está activo?", es_activo)
print("¿Está inscrito?", esta_inscrito)

# ==========================================
# 📌 Verificando el tipo de dato con type()
# ==========================================

print("Tipo de 'nombre':", type(nombre))
print("Tipo de 'numero_entero':", type(numero_entero))
print("Tipo de 'numero_decimal':", type(numero_decimal))
print("Tipo de 'es_activo':", type(es_activo))

# ==========================================
# ⚠️ Nombres de variables: buenas prácticas
# ==========================================
# - Usar nombres descriptivos: edad_alumno, promedio_final
# - Evitar usar palabras reservadas (if, for, print, etc.)
# - Usar minúsculas y guiones bajos: mi_variable

edad_alumno = 21  # ✅ correcto
# edad alumno = 21  ❌ incorrecto (espacio no permitido)

# ==========================================
# 🧪 PRUEBA RÁPIDA
# Crea 4 variables: tu edad, tu altura, tu nombre y si estás activo.
# Muestra cada una con su tipo correspondiente.
