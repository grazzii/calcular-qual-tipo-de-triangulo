# Solicita os lados do triângulo
a = float(input("Lado a = "))  # Lado a
b = float(input("Lado b = "))  # Lado b
c = float(input("Lado c = "))  # Lado c
 
# Verifica se os lados formam um triângulo
if (a < b + c and b < a + c and c < a + b):
    # Verifica o tipo de triângulo
    if (a == b and b == c):
        print("Triângulo Equilátero")
    elif (a == b or a == c or b == c):
        print("Triângulo Isósceles")
    else:
        print("Triângulo Escaleno")
else:
    print("Os lados não formam um triângulo!")
