import time
from tabulate import tabulate  

def hash(data):
    hash_valor = 0
    for byte in data:
        hash_valor = (hash_valor ^ byte) * 31  
    return hash_valor & ((1 << 256) - 1)  

def findNonce(dataToHash, bitsToBeZero):
    nonce = 0
    quantdBits0 = 2 ** (256 - bitsToBeZero)
    tempo = time.time()

    while True:
        data_with_nonce = dataToHash + nonce.to_bytes((nonce.bit_length() + 7) // 8, 'big')
        hash_result = hash(data_with_nonce)
        if hash_result < quantdBits0:
            break
        nonce += 1
    
    tempo_gasto = time.time() - tempo

    return nonce, tempo_gasto


def arqs():
    teste = [
        ("Esse eh facil", 8),
        ("Esse eh facil", 10),
        ("Esse eh facil", 15),
        ("Texto maior muda o tempo?", 8),
        ("Texto maior muda o tempo?", 10),
        ("Texto maior muda o tempo?", 15),
        ("Eh possivel calcular esse?", 18),
        ("Eh possivel calcular esse?", 19),
        ("Eh possivel calcular esse?", 20)
    ]
    
    resultados = []
    
    for text, bits in teste:
        data_bytes = text.encode('utf-8') 
        nonce,tempo_gasto = findNonce(data_bytes, bits) 
        
        resultados.append([text, bits, nonce, f"{tempo_gasto:.6f}"])  
    
    print(tabulate(resultados, headers=["Texto a Validar", "Bits em Zero", "Nonce", "Tempo (em s)"], tablefmt="fancy_grid"))
    
    with open("resultados.txt", "w") as file:
        file.write(tabulate(resultados, headers=["Texto a Validar", "Bits em Zero", "Nonce", "Tempo (em s)"], tablefmt="fancy_grid"))
    
    print("Tabela no arquivo: 'resultados.txt'.")

if __name__ == "__main__":
    arqs()
