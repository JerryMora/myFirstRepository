logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

print(logo)

alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
            't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
            't', 'u', 'v', 'w', 'x', 'y', 'z']





def caesar(text, shift, direccion):
    newText = ""
    shift = shift % 26
    if direccion == "decod":
        shift *= -1
    for letra in text:
        if letra in alfabeto:
            position = alfabeto.index(letra)
            newPosition = position + shift
            new_letter = alfabeto[newPosition]
            newText += new_letter
        else:
            newText += letra
    if direccion == "cod":
        print(f"El texto encriptado es: {newText}")
    elif direccion == "decod":
        print(f"El texto desencriptado es: {newText}")

answerBool

while answerBool != False:

    codOrDecod = input("Ingresa ""cod"" para codificar o ""decod"" para decodificar:\n")

    texto = input("Escribe tu mensaje:\n").lower()

    cifrado = int(input("Escribe el numero de cifrado: "))

    caesar(text = texto, shift = cifrado,direccion = codOrDecod)

    answer = input("Desea continuar (c) o salir(s)?\n")
    if answer == "c":
        answerBool == True
    else:
        answerBool == False
