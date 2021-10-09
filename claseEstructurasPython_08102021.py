# Programación en python
#Utilización de estructuras de control
'''
# ------------ UTILIZANDO EL IF -----------------

En python, la sentencia if, a primera vista, suele parecerse a la que se utiliza en 
el lenguaje de java, pero en su implementación suele tener varios cambios.
La condición a evaluar no se encierra dentro de paréntesis, el 'else if' cambia a
ser un 'elif', mientras que el else sigue manteniéndose igual. El bloque de código 
no está encerrado en {} (corchetes), sino que solamente dicho cuerpo de código se 
encontrará dentro con la identación del mismo, es decir, con un sangrado mayor.



#EJEMPLOS:
#Ejemplo simple
print('----------  EJEMPLO SIMPLE IF -------------')

x = 27
if x < 20:
    print(x, 'es menor que 20')
else:
    print(x, 'es mayor que 20')

print('----------- EJEMPLO SIMPLE FOR ------------')

# ------------ UTILIZANDO EL FOR -----------------

En python, el for posee una estructura muy diferente, la cual es:
for 'variable' in range(desde, hasta, paso)
En esta parte, "desde" es el número inicial, "hasta" es hasta donde se quiere llegar este número NO
SE INCLUYE, "paso" es el paso que utilizará la estructura.


#EJEMPLO SIMPLE:
for i in range(0, 11, 2):
    print(i)

#ejemplo lista:
lista = ['Andrea', 'Carlos', 'RACSO', 'Jose']

for a in lista:
    print(a)
print('----------- EJEMPLO SIMPLE WHILE  ------------')

#------------ UTILIZANDO EL WHILE -----------------

Aqui en python NO EXISTE el do while, solamente el while. Su estructura es muy simple y muy parecida a la de Java

num = 0
while num < 6:
    print(num)
    num=num+1

'''

#-------------------------------------------------------
#funcion para menú:
def Menu():
    print('------------------ MENÚ ------------------')
    print('1. Sumas')
    print('2. Tablas de multiplicación')
    print('3. Ejemplo de while')
    print('4. Salir')
    print('------------------------------------------')

#main:
if __name__ == '__main__':
    while True:
        Menu()
        op = input('Ingrese una opción del menú: ')

        if op == '1':
            x = int(input('Ingrese un número: '))
            y = int(input('Ingrese otro número: '))
            z=x+y
            print('La sumatoria de los números es : ', z)

        elif op == '2':
            numero = int(input('¿De cuál número desea que se su tabla de multiplicación? '))
            inicio = 1
            hasta = 10

            for u in range(inicio, hasta +1):
                print(numero, ' x ', u, ' = ', numero*u)
        
        elif op == '3':
            lineas = []
            print('Escriba unas líneas: ')

            while True:
                ingreso = input()
                if ingreso:
                    lineas.append(ingreso)
                else:
                    break

            for texto in lineas:
                print(texto)
        
        elif op == '4':
            break