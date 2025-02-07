# Funciones para las operaciones matemáticas
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: No se puede dividir por cero"

# Función principal del calculador
def calculadora():
    print("Bienvenido al calculador en Python")
    
    while True:
        print("\nOpciones:")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")
        
        # Pedir al usuario que elija una operación
        operacion = input("Elige una opción (1/2/3/4/5): ")
        
        if operacion == '5':
            print("¡Hasta luego!")
            break
        
        # Pedir números para realizar la operación
        try:
            num1 = float(input("Introduce el primer número: "))
            num2 = float(input("Introduce el segundo número: "))
        except ValueError:
            print("Por favor, ingresa un número válido.")
            continue
        
        # Realizar la operación seleccionada
        if operacion == '1':
            print(f"{num1} + {num2} = {sumar(num1, num2)}")
        elif operacion == '2':
            print(f"{num1} - {num2} = {restar(num1, num2)}")
        elif operacion == '3':
            print(f"{num1} * {num2} = {multiplicar(num1, num2)}")
        elif operacion == '4':
            print(f"{num1} / {num2} = {dividir(num1, num2)}")
        else:
            print("Opción no válida. Por favor, elige una opción entre 1 y 5.")

# Ejecutar la calculadora
if __name__ == "__main__":
    calculadora()
#Espero que te guste mi proyecto
