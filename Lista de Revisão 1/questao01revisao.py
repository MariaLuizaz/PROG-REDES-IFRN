import sys
from tabulate import tabulate
from termcolor import colored  

def validando_ip(ip):
    octetos = ip.split('.')  
    
    if len(octetos) != 4:
        return False  
    
    for octeto in octetos:
        if not octeto.isdigit():
            return False
        num = int(octeto)
        if num < 0 or num > 255:
            return False
    
    return True 


while True:
    strendIP = input("Informe um endereço IP (formato xxx.xxx.xxx.xxx): ")
    
    if validando_ip(strendIP):
        print("IP VÁLIDO!")
        break  
    else:
        print("IP INVÁLIDO! Por favor insira um IP no formato correto.")

def validando_CIDR(CIDR):
    if CIDR.isdigit():
        cidr_int = int(CIDR)

        if 0 <= cidr_int <= 32:
            return True
        else:
            print("ERRO: Insira o endereço no formato CIDR.")
            return False
    else:
        print("ERRO: O valor informado não é um número válido.")
        return False

while True:
   CIDR1 = input("Insira a máscara CIDR inicial: ")
   if validando_CIDR(CIDR1):
        print('Máscara CIDR VÁLIDA!')
        break
   else:
        print('Máscara CIDR INVÁLIDA! Por favor insira o endereço no formato correto!')

while True:
    CIDR2 = input("Insira a máscara CIDR final:")
    if validando_CIDR(CIDR2):
        print('Máscara CIDR VÁLIDA!')
        break
    else:
        print('Máscara CIDR INVÁLIDA! Por favor insira o número no formato correto!')


def convertendoIP(IP):
    octetosconvert = IP.split('.')
    formatbin = []
    for octetosconvert in octetosconvert:
        formatbin.append(bin(int(octetosconvert))[2:].zfill(8))
    return '.'.join(formatbin)

try:
    ipbin = convertendoIP(strendIP)
except ValueError as e:
    sys.exit(e)
except:
    sys.exit(f'\nERRO: {sys.exc_info()[1]}')

def decimal(mask):
    if not (0 <= mask <= 32):
        raise ValueError(f"ERRO! O valor CIDR é inválido")
    
    maskbin ='1' * mask + '0' * (32 - mask)
    maskdec = [str(int(maskbin[i:i+8], 2)) for i in range(0, 32, 8)]
    maskbinformat = '.'.join([maskbin[i:i+8] for i in range(0, 32, 8) ])
    return '.'.join(maskdec), maskbinformat

try:
    tuplaMask1 = decimal(int(CIDR1))  
    tuplaMask2 = decimal(int(CIDR2))  
except ValueError as e:
    sys.exit(e)
except Exception as e:
    sys.exit(f"ERRO! {str(e)}")

def endereçoBITaBIT(ipbin, maskbin):
    ip_octet = ipbin.split('.')
    mask_octet = maskbin.split('.')

    redeIPbin = []
    for i in range(4):
        redeIPbin.append(format(int(ip_octet[i], 2) & int(mask_octet[i], 2), '08b'))
    return '.'.join(redeIPbin)

strIPrede1 = endereçoBITaBIT(ipbin, tuplaMask1[1])
strIPrede2 = endereçoBITaBIT(ipbin, tuplaMask2[1])

def IPbinario(binstr):
    binoctet = binstr.split('.')
    ip = [] 
    for binoctet in binoctet:
        ip.append(str(int(binoctet, 2)))
    return '.'.join(ip)

host1bin1 = strIPrede1[:-1] + '1'
tuplahost1_1 = IPbinario(host1bin1)

broadcastbin1 = strIPrede1[:-8] + '11111111'
tuplabroadcast1 = IPbinario(broadcastbin1)

host2bin1 = tuplabroadcast1[0][:-1] + '0'
tuplahost2_1 = IPbinario(host2bin1)

hostsvalidos1 = (2 ** (32 - int(CIDR1))) - 2

host1bin2 = strIPrede2[:-1] + '1'
tuplahost1_2 = IPbinario(host1bin2)

broadcastbin2 = strIPrede2[:-8] + '11111111'
tuplabroadcast2 = IPbinario(broadcastbin2)

host2bin2 = tuplabroadcast2[0][:-1] + '0'
tuplahost2_2 = IPbinario(host2bin2)

hostsvalidos2 = (2 ** (32 - int(CIDR2))) - 2

tabela = [
    [colored('Endereço IP', 'yellow'), strendIP, strendIP],
    [colored('Máscara Decimal', 'yellow'), tuplaMask1[0], tuplaMask2[0]],
    [colored('Máscara Binária', 'yellow'), tuplaMask1[1], tuplaMask2[1]],
    [colored('Endereço de Rede', 'yellow'), strIPrede1, strIPrede2],
    [colored('Primeiro Host', 'yellow'), tuplahost1_1, tuplahost1_2],
    [colored('Broadcast', 'yellow'), tuplabroadcast1, tuplabroadcast2],
    [colored('Último Host', 'yellow'), tuplahost2_1, tuplahost2_2],
    [colored('Hosts Válidos', 'yellow'), hostsvalidos1, hostsvalidos2]
]

print("\nResultados:")
print(tabulate(tabela, headers=["Descrição", f"Para máscara /{CIDR1}", f"Para máscara /{CIDR2}"], tablefmt="fancy_grid"))
