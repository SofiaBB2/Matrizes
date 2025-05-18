import numpy as np

def criptografar(alfabeto, chave):
    msg = input("Informe sua mensagem: ").upper()
    letras = list(msg)

    codigo = []

    for letra in letras:
        for i in range (len(alfabeto[0])):
            if letra == alfabeto[0][i]:
                codigo.append(alfabeto[1][i])
                break

    if len(codigo) % 2 != 0:
        codigo.append(0)  

    codigo = np.reshape(codigo, (2, -1))
    print(codigo)

    cript = np.dot(chave, codigo)
    cript = cript.flatten()
    cript = ', '.join(map(str, cript))

    return cript

def descriptografar(alfabeto, chave):
    cript = input("Digite a mensagem criptografada (números separados por vírgula): ")
    numeros = list(map(int, cript.split(', ')))

    cript = np.reshape(numeros, (2, -1))

    chaveInv = np.linalg.inv(chave)

    codigo = np.dot(chaveInv, cript)
    codigo = np.round(codigo).astype(int)
    codigo = codigo.flatten()

    descript = []

    for n in codigo:
        for i in range (len(alfabeto[0])):
            if n == alfabeto[1][i]:
                descript.append(alfabeto[0][i])
                break
    
    descript = ''.join(descript)

    return descript
     


chave = [[2, 12], [15, 8]]

alfabeto = [["A", "À", "Á", "Ã", "Â", "B", "C", "D", "E", "É", "Ê", "È", "F", "G", "H", "I", "Í", "Î", "J", "K", "L", "M", "N", "O", "Ó", "Ô", "Õ", "P", "Q", "R", "S", "T", "U", "Ú", "Û", "V", "W", "X", "Y", "Z", "Ç", " ", "?", ",", "!"], 
            [472, 473, 474, 475, 476, 58, 314, 392, 216, 217, 218, 219, 164, 493, 384, 135, 136, 137, 105, 433, 344, 268, 244, 26, 27, 28, 29, 365, 484, 330, 211, 125, 292, 293, 294, 478, 174, 389, 306, 34, 499, 12, 5, 18, 2]]

op = 1
while(op != 0):    
    print("------------------MENU------------------")
    print("0 - sair;")
    print("1 - criptografe uma mensagem;")
    print("2 - descriptografe uma mensagem.")
    op = int(input("Informe a opção escolhida: "))

    if(op == 0):
        print("Fim!")
        break
    elif(op == 1):
        cript = criptografar(alfabeto, chave)
        print(cript)
    elif(op == 2):
        descript = descriptografar(alfabeto, chave)
        print(descript)
    else:
        print("3RR01(ERRO!)")
