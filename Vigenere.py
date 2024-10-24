text= 'Hello Zaira'
custom_key = 'python'

def Vigenere(message, key, direction = 1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message= ''

    for char in message.lower():
       # Agregar espaciado en el mensaje
        if not char.isalpha():
            final_message += char
        else:
            # Encontrar la llave correcta para codificar / decodificar
            key_char= key[key_index %len(key)]
            key_index +=1

            # Definir el desplazamiento y el encriptador / dencriptado
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset * direction) % len(alphabet)
            final_message += alphabet[new_index]
    return final_message
def encryp(message, key):
    return Vigenere(message, key)
def decrypt(message, key):
    return Vigenere(message, key, -1)

print (f'''\n Texto Sin Encriptar : {text}
       \n Texto Encriptado : {encryp(text, custom_key)}
       \n Llave Encriptadora: {custom_key}
       \n Funcion Desencriptadora : {decrypt(encryp(text, custom_key), custom_key)}''')
