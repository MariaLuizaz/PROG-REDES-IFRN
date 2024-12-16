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