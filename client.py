import pyDes
import binascii
import colorama      # библиотека для цветного текста
import sys
import socket

class DES:
    # pyDes.des（key，[mode]，[IV]，[pad]，[padmode]）
    # Байты, тип шифрования и дополнительные параметры ключа шифрования используются для установки символов заполнения и установки режима заполнения
    def des_encrypt(self, key, plaintext):
        iv = secret_key = key
        k = pyDes.des(secret_key, pyDes.CBC, iv, pad=None, padmode = pyDes.PAD_PKCS5)
        data = k.encrypt(plaintext, padmode=pyDes.PAD_PKCS5)
        return(binascii.b2a_hex(data))      # возвращаются байты

    def des_decrypt(self, key, ciphertext):
        iv = secret_key = key
        k = pyDes.des(secret_key, pyDes.CBC, iv, pad=None, padmode = pyDes.PAD_PKCS5)
        data = k.decrypt(binascii.a2b_hex(ciphertext), padmode=pyDes.PAD_PKCS5)
        return(data)      # возвращаются байты

sock = socket.socket()
sock.connect(('localhost', 12397))

file = open("key_s.txt")        # файл с ключом
key_s = file.readline()         # чтение из файла строки с ключом
file.close()

def colored_input(text: str, color):                  # функция для цветного текста
    inp = input(text + color)
    print(colorama.Fore.RESET, end="", flush=True)
    sys.excepthook = sys.__excepthook__
    return inp
colorama.init(autoreset=True)                         # автообновление цвета

msg = colored_input(' -> ', colorama.Fore.GREEN)

des = DES()

while True:
    if msg != 'exit':
        data = des.des_encrypt(key_s, msg.strip())
        sock.send(data)    # отправка зашифрованного сообщения на сервер

        print('Получено от сервера: ' + colorama.Fore.GREEN + str(data.decode()) + '\n')
        msg = colored_input(' -> ', colorama.Fore.GREEN)
    else:
        break

sock.close()