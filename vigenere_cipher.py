def vigenere_cipher(message,key,direction = 1):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''
    key_index = 0
    for char in message:
        if not char.isalpha():
            final_message += char
        else:
            key_char = key[key_index%len(key)]
            key_index += 1

            offset = (alphabet.index(key_char))
            index = alphabet.find(char)
            new_index = (index+offset*direction)%len(alphabet)
            final_message += alphabet[new_index]
        
    return final_message
    
def encrypt(message,key):
    return vigenere_cipher(message,key)
def decrypt(message,key):
    return vigenere_cipher(message,key,-1)

message = input("Enter the message you want to encrypt/decrypt: ")
key = input("Enter the key: ")
choice = input("Press (E) if you want to Encrypt or (D) if you want to decrypt: ")
if choice.upper() == "E":
    result = encrypt(message,key)
    print(f"Encrypted message: {result}")
elif choice.upper() == 'D':
    result = decrypt(message,key)
    print(f"Decrypted message: {result}")
else:
    print("Please enter valid choice!")