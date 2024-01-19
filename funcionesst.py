######################################################################
#Elaborado por: Jose Fabio Navarro Naranjo y Emmanuel Naranjo Blanco #
#Fecha de Creación: 21/03/2019 5:45pm                                #
#Fecha de última Modificación: 25/03/2019 6:18pm                     #
#Versión: 3.7.2                                                      #
######################################################################

#importación de librerías
import sys
sys.setrecursionlimit(5000)

def calcularNumSuerteAux(pfrase): #1
    #Funcion: validar datos para contar los numeros de una frase.
    #Entrada: pfrase(str)
    #Salida: numero de la surte (str)
    if pfrase.startswith(" ")==False:
        if pfrase.endswith(" ")==False:
            return calcularNumSuerte(pfrase)
        return "No debe dejar espacios al final de la oración."
    return 'No debe dejar espacios al inicio de la oración.'

def calcularNumSuerte(pfrase):
    """
    Funcion: contar los numeros de una frase.
    Entrada: pfrase(str)
    Salida: numero de la suerte (str)
    """
    i=0
    suma=0
    while i<=len(pfrase)-1:
        if pfrase[i].isdigit():
            suma+=int(pfrase[i])
        i+=1
    return suma

def contarVoConAux(ppal):#2
    #Funcion: validar datos para indicar la cantidad de vocales y consonantes
    #Entrada: ppal(str)
    #Salida: cantidad de vocales y consonantes (str)
    if ppal.isalpha():
        return contarVoCon(ppal)
    return "Debe ingresar solo una palabra, no puede contener números ni espacios."

def contarVoCon(ppal):
    """
    Funcion: indicar la cantidad de vocales y consonantes
    Entrada: ppal(str)
    Salida: cantidad de vocales y consonantes (str)
    """
    a=0;e=0;i=0;o=0;u=0
    con=0
    contador=len(ppal)-1
    while 0<=contador:
        if ppal[contador]=='a':
            a+=1
        elif ppal[contador]=='e':
            e+=1
        elif ppal[contador]=='i':
            i+=1
        elif ppal[contador]=='o':
            o+=1
        elif ppal[contador]=='u':
            u+=1
        else:
            con+=1
        contador-=1
    print('\nCantidad de a: ',a,'\nCantidad de e: ',e,' \nCantidad de i: ',i,'\nCantidad de o: ',o, '\nCantidad de u: ',u,'\nCantidad de consonantes: ',con)
    return ''

def saberPalinAux(ppalabra):#3
    #Funcion: Validar los datos para determinar si una palabra es palindroma.
    #Entrada: ppalabra(str)
    #Salida: indica si la palabra es palindroma (str)
    if ppalabra.isalpha():
        return saberPalin(ppalabra)
    return 'Debe ingresar solo una palabra y esta no puede tener números ni espacios.'

def saberPalin(ppalabra):
    """
    Funcion: determinar si una palabra es palindroma.
    Entrada: ppalabra(str)
    Salida: indica si la palabra es palindroma (str)
    """
    espejo=convertirEspejo(ppalabra)
    if espejo==ppalabra:
        return 'Su palabra si es palindroma'
    else:
        return 'Su palabra no es palindroma'


def comerVocalesAux(pfrase): #4
    #Funcionamiento: Validar los datos para eliminar las vocales de una frase.
    #Entradas: pfrase(str)
    #Salidas: frase sin vocales (str)
    if pfrase.startswith(" ")==False:
        if pfrase.endswith(" ")==False:
            return comerVocales(pfrase)
        return "No debe dejar espacios al final de la oración."
    return 'No debe dejar espacios al inicio de la oración.'

def comerVocales(pfrase):
    """
    Funcion: Eliminar las vocales de una frase.
    Entrada: pfrase(str)
    Salida: frase sin vocales (strs)
    """
    vocales = ['a','A','e','E','i','I','o','O','u','U']
    resultado=''
    for letra in pfrase:
        if letra not in vocales:
            resultado += letra
    return resultado

def convertirEspejoAux(ppal):#5
    #Funcionamiento: Validar los datos para convertir el texto en espejo.
    #Entradas: palabra(str)
    #Salidas: texto en espejo(str)
    if ppal.isalpha():
            return convertirEspejo(ppal)
    return 'Debe ingresar solo una palabra, y no puede contener números.'

def convertirEspejo(ppal):
    """
    Funcion: invertir los caracteres de una palabra.
    Entrada: palabra(str)
    Salida: palabra en espejo(str)
    """
    x=len(ppal)-1
    alreves=""
    while 0<=x:
        alreves=alreves+(ppal[x])
        x-=1
    return alreves
   
def analizarTextoAux(porac):#6
    #Funcionamiento: Validar los datos para contar las palabras y los caracteres.
    #Entradas: oracion(str)
    #Salidas: número de palabras y caracteres (str)
    if porac[0]!=" ":
        if porac[len(porac)-1]!=" ":
            return analizarTexto(porac)
        return "No debe dejar espacios al final de la oración."
    return 'No debe dejar espacios al inicio de la oración.'

def analizarTexto(porac):
    """
    Funcion: invertir los caracteres de una palabra.
    Entrada: oracion(str)
    Salida: número de palabras y caracteres (str)
    """
    nc=0
    x=len(porac)-1
    pal=1
    while x>=0:
        if porac[x]==" ":
            pal+=1
        nc+=1
        x-=1
    return "La oración tiene "+str(nc)+" caracteres y "+str(pal)+" palabras."

def convertirBinaDeciAux(pbina):#7
    #Funcionamiento: Validar los datos convertir el valor de binario a decimal
    #Entradas: numero binario(int)  ##??? int o str??
    #Salidas: valor decimal de la entrada binaria (int)
    if pbina.isdigit():
        if pbina.count("1")+pbina.count("0")==(len(pbina)):
            if len(pbina)==8:
                return convertirBinaDeci(pbina)
            return "La cifra debe tener 8 dígitos"
        return "El número ingresado debe ser binario (solo 0 y 1)."
    return 'La cadena ingresada no debe contener letras.'

def convertirBinaDeci(pbina):
    """    
    Funcionamiento: Validar los datos convertir el valor de binario a decimal
    Entradas: numero binario(str)
    Salidas: valor decimal de la entrada binaria (int)
    """
    pbina2=convertirEspejo(pbina)
    decimal=0
    n=len(pbina)-1
    while n>=0:
        if pbina2[n]=="1":
            decimal+=(2**(n))
        n-=1
    return "El número decimal correspondiente a "+str(pbina)+" es "+str(decimal)
