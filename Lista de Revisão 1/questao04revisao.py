import os

def criptografia(contando, senha):
    senhalen = len(senha)
    result = []

    for i, byte in enumerate(contando):
        senhachar = senha[i % senhalen]
        xor_byte = byte ^ ord(senhachar)  

    return bytes(result)

def arqs():
    arqorigem = input("Insira o arquivo de origem: ")
    palavrapasse = input("Insira a palavra-passe: ")
    arqdestino = input("Insira o arquivo de destino: ")

    if not os.path.exists(arqorigem):
        print("ERRO: O arquivo de origem não existe.")
        return

    if os.path.exists(arqdestino):
        print("ERRO: O arquivo não será sobrescrito.")
        return

    try:
        with open(arqorigem, 'rb') as f:
            conteudo = f.read()

        conteudo_encriptado = criptografia(conteudo, palavrapasse)

        with open(arqdestino, 'wb') as f:
            f.write(conteudo_encriptado)

        print(f"Arquivo processado e salvo: '{arqdestino}'.")

    except Exception as e:
        print(f"ERRO: {e}")

if __name__ == "__main__":
    arqs()
