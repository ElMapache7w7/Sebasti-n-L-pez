#Escriba un programa para mostrar el patrón como un triángulo rectángulo con un número. El patrón como:
#1
#12
#123
#1234
#12345
altura = int(input("Ingrese la latura del triangulo: "))
i = 1

for i in range(1, altura + 1):
    
    for j in range(1, i + 1):
        print(j, end='')
    print()