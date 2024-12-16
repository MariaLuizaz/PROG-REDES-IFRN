import random
import os

arquivo = r"C:\Users\maria\OneDrive\Documentos\wordslista.txt"

if not os.path.exists(arquivo):
    print(f"Erro: O arquivo {arquivo} não foi encontrado.")
    exit()  

def palavras_arq(arquivo):
    palavras = []
    with open(arquivo, 'r', encoding='utf-8') as file:
        for linha in file:
            palavra = linha.strip()  
            if 5 <= len(palavra) <= 8:  
                palavras.append(palavra)  
    return palavras

def sorteio(palavras):
    palavra_sorteada = random.choice(palavras)  
    print(f" VAMOS COMEÇAR!:D A palavra sorteada tem {len(palavra_sorteada)} letras.")
    return palavra_sorteada


def retorno(tentativa, palavra_sorteada):
    
    VERDE = '\033[32m'  
    AMARELO = '\033[33m'  
    CINZA = '\033[37m'  
    RESET = '\033[39m'  

    resultado = []

    for i, letra in enumerate(tentativa):
        if letra == palavra_sorteada[i]:
            resultado.append(VERDE + letra + RESET)  
        elif letra in palavra_sorteada:
            resultado.append(AMARELO + letra + RESET) 
        else:
            resultado.append(CINZA + letra + RESET) 
    return ''.join(resultado)

def jogar():
    palavras = palavras_arq(arquivo)  
    palavra_sorteada = sorteio(palavras)  
    tentativas = 6  
    print("Adivinhe a palavra!")
    while tentativas > 0:
        tentativa = input(f"\nFaltam {tentativas} tentativas. Insira uma palavra com {len(palavra_sorteada)} letras: ").strip().lower()

        if len(tentativa) != len(palavra_sorteada):
            print(f"A palavra deve ter {len(palavra_sorteada)} letras.")
            continue

        print(retorno(tentativa, palavra_sorteada))

        if tentativa == palavra_sorteada:
            print(f"PARABÉNS!!! Você adivinhou a palavra '{palavra_sorteada}' em {7 - tentativas} tentativas!")
            break

        tentativas -= 1

    if tentativas == 0 and tentativa != palavra_sorteada:
        print(f"\nGAME OVER! :( A palavra era '{palavra_sorteada}'.")


jogar()

