import math

def sum(complex_1, complex_2):
    add = (complex_1[0] + complex_2[0], complex_1[1] + complex_2[1])
    answer(add)
def subtraction(complex_1, complex_2):
    subtract = (complex_1[0] - complex_2[0], complex_1[1] - complex_2[1])  
    answer(subtract)
def product (complex_1, complex_2):
    prod = (complex_1[0]* complex_2[0] - complex_1[1]*complex_2[1], complex_1[1]*complex_2[0] + complex_1[0]* complex_2[1] )
    answer(prod)
def division(complex_1, complex_2):
    dividir = complex_2[0]**2 + complex_2[1]**2
    split = [(complex_1[0]*complex_2[0]+complex_1[1]*complex_2[1])/dividir, (complex_2[0]*complex_1[1]-complex_1[0]*complex_2[1])/dividir]
    answer(split)
def conjugate(complex_1):
    conjuga = [complex_1[0], -complex_1[1]]
    answer(conjuga)
def fase(complex_1):
    coord_x = complex_1[0]
    coord_y = complex_1[1]
    if (coord_x < 0 and coord_y < 0) or (coord_x < 0 and coord_y >= 0):
        return math.pi + (math.atan(complex_1[1]/complex_1[0]))
    elif coord_x >= 0 and coord_y < 0:
        return 2* math.pi + (math.atan(complex_1[1]/complex_1[0]))
    else:
        return math.atan(complex_1[1]/complex_1[0])
def module(complex_1):
    mod = math.sqrt((complex_1[0]**2 + (complex_1[1]**2)))
    return mod
def cartesianTopolar(complex_1):
    angle = fase[complex_1]   
    polar = (module(complex_1, angle))
    answer(polar) 
def answer (result):
    if result[1] > 0:
        print(str(result[0]) + "+" + str(result[1])+ "i")
    else:
        print(str(result[0]) + str(result[1])+ "i")
   

def main():
    complex_1 = [15,4]
    complex_2 = [25,2]

   
    print("Ingresar 1 para suma, 2 para resta, 3 para producto")
    print("4 para division, 5 para conjugado, 6 para modulo, 7 para fase, 8 para cartesiano")
    elegir = input ("Ingrese un numero para seleccionar la funcion: ")
   
    if elegir == "1":
        sum(complex_1, complex_2)
    elif elegir == "2":
        subtraction(complex_1, complex_2)
    elif elegir == "3":
        product(complex_1, complex_2)
    elif elegir == "4":
        division(complex_1, complex_2)
    elif elegir == "5":
        conjugate(complex_1)
    elif elegir == "6":
        fase(complex_1)
    elif elegir == "7":
        module(complex_1)
    elif elegir == "8":
        cartesianTopolar(complex_1)
    else:
        print("Por el momento no tenemos otra función")
main()   

