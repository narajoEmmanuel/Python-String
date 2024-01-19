######################################################################
#Elaborado por: Jose Fabio Navarro Naranjo y Emmanuel Naranjo Blanco #
#Fecha de Creación: 21/03/2019 5:45pm                                #
#Fecha de última Modificación: 25/03/2019 6:18pm                     #
#Versión: 3.7.2                                                      #
######################################################################

#importanción de librerías
from funcionesst import*
""""funcionesst" es el archivo que contiene las funciones principales
a ser llamadas desde este archivo"""

#Definición de funciones
#Permiten el ingreso y salida de datos
def opcionSuerte():#1
    """
    Funcionamiento: Responsable de permitir la entrada y salidad de datos 
    Entradas: NA
    Salidas: indica el numero de la suerte
    """
    print("\n------------------------\n")
    print("Numero de la suerte\n")
    frase=input("Ingrese una frase: ")
    print('Su numero de la suerte es: ',calcularNumSuerteAux(frase))
    
def opcionVoCon():#2
    """
    Funcionamiento: Responsable de permitir la entrada y salidad de datos 
    Entradas: NA
    Salidas: indica la cantidad de vocales y consonantes
    """
    print("\n------------------------\n")
    print("Cantidad de vocales y consonantes\n")
    pal=input("Ingrese una palabra: ")
    print(contarVoConAux(pal))
    
def opcionPalindroma(): #3
    """
    Funcionamiento: Responsable de permitir la entrada y salidad de datos 
    Entradas: NA
    Salidas: indica si la palabra es palindroma
    """
    print("\n------------------------\n")
    print("Palabras Palíndromas\n")
    palabra=input("Ingrese una palabra: ")
    print(saberPalinAux(palabra))
    
def opcionComerVocales():#4
    """
    Funcionamiento: Responsable de permitir la entrada y salidad de datos 
    Entradas: NA
    Salidas: texto sin vocales
    """
    print("\n------------------------\n")
    print("Reconocer las vocales\n")
    frase=input("Ingrese una frase: ")
    print('Su frase sin vocales es: ',comerVocalesAux(frase))

def opcionCadenaEspejo():#5
    """
    Funcionamiento: Responsable de permitir la entrada y salidad de datos 
    Entradas: NA
    Salidas: texto en espejo
    """
    print ("\n------------------------\n")
    print("Texto en espejo\n")
    pal=str(input("Ingrese una palabra únicamente: "))
    print(convertirEspejoAux(pal))

def opcionAnalizaTexto():#6
    """
    Funcionamiento: Responsable de permitir la entrada y salidad de datos 
    Entradas: NA
    Salidas: Cantidad de caracteres y de palabras.
    """
    print ("\n------------------------\n")
    print("Analizador de texto\n")
    orac=str(input("Ingrese una oración: "))
    print(analizarTextoAux(orac))

def opcionConvertidor():#7
    """
    Funcionamiento: Responsable de permitir la entrada y salidad de datos 
    Entradas: NA
    Salidas: valor decimal de la entrada binaria
    """
    print ("\n------------------------\n")
    print("Covertidor de binario a decimal\n")
    bina=str(input("Ingrese un número binario (ej:10000101): "))
    print(convertirBinaDeciAux(bina))
     

###############################################################################

def menu():
    """
    Funcionamiento: De manera repetitiva, muestra el menú al usuario. 
    Entradas: NA
    Salidas: Resultado según lo solicitado
    """
    print("\n**************************\n")
    print("Laboratorio de String")
    print("\n**************************\n")
    print("1. Numero de la suerte")
    print("2. Contar vocales y consonantes")
    print("3. Palabras palindromas")
    print("4. Come Vocales")
    print("5. Texto en espejo")
    print("6. Analizador de texto")
    print("7. Covertidor de binario a decimal")
    print("0. Terminar")
    opcion =int(input ("Escoja una opción: "))
    if opcion >=0 and opcion <=7:   
        if opcion==1:
            opcionSuerte()
        elif opcion==2 :
            opcionVoCon()
        elif opcion==3:
            opcionPalindroma()
        elif opcion==4:
            opcionComerVocales()
        elif opcion==5:
            opcionCadenaEspejo()
        elif opcion==6:   
            opcionAnalizaTexto()
        elif opcion==7:
            opcionConvertidor()
        elif opcion==0:
            return
    else:
        print ("Opción inválida")

    menu()

#Programa Principal
menu()
