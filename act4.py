# --- 1. BUCLE 'while' (para validar la entrada) ---
# Usamos un bucle 'while True' para seguir preguntando
# hasta que el usuario ingrese un número válido.

print("--- Validación con 'while' ---")
numero_limite = 0

while True:
    try:
        # Intentamos convertir la entrada del usuario a un número entero
        entrada = input("Por favor, ingresa un número entero positivo (ej. 10): ")
        numero_limite = int(entrada)

        # --- ESTRUCTURA DE CONTROL 'if' (dentro del 'while') ---
        # Verificamos si el número es positivo
        if numero_limite > 0:
            # Si es positivo, rompemos (salimos) el bucle 'while'
            print(f"¡Número válido! Has ingresado: {numero_limite}\n")
            break 
        else:
            # Si es 0 o negativo, lo informamos y el bucle continúa
            print("Error: El número debe ser mayor que 0. Intenta de nuevo.")
            
    except ValueError:
        # Si 'int(entrada)' falla (ej. si escribe "hola"),
        # se ejecuta este bloque y el bucle continúa
        print("Error: Eso no es un número entero. Intenta de nuevo.")

# --- 2. BUCLE 'for' (para iterar) ---
# Ahora que tenemos un 'numero_limite' válido, usamos 'for'
# para recorrer todos los números desde 1 hasta ese límite.

print(f"--- Procesando números del 1 al {numero_limite} con 'for' y 'if' ---")

# 'range(1, numero_limite + 1)' crea una secuencia
# que empieza en 1 y termina en 'numero_limite'
for numero in range(1, numero_limite + 1):

    # --- 3. ESTRUCTURAS DE CONTROL 'if/elif/else' (dentro del 'for') ---
    # Usamos 'if/elif/else' para clasificar cada 'numero'
    
    # Verificamos si es múltiplo de 2 Y de 3 (ej. 6, 12)
    if (numero % 2 == 0) and (numero % 3 == 0):
        print(f"Número {numero}: Es múltiplo de 2 y 3.")
    
    # Si no, verificamos si es solo múltiplo de 2 (ej. 2, 4, 8)
    elif numero % 2 == 0:
        print(f"Número {numero}: Es par (múltiplo de 2).")
        
    # Si no, verificamos si es solo múltiplo de 3 (ej. 3, 9, 15)
    elif numero % 3 == 0:
        print(f"Número {numero}: Es múltiplo de 3.")
        
    # Si no cumple ninguna de las anteriores (ej. 1, 5, 7)
    else:
        print(f"Número {numero}: Es impar y no es múltiplo de 3.")

print("\n--- ¡Programa finalizado! ---")