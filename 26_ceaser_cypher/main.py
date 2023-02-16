alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

direction = input("Type 'encoded' to  encrypt, type 'decode' to decrypt ")
text = input("Type your message:\n").lower()
shift = int(input("Type your shift number:\n"))

# defining the function of encryption and decrryption 

def encrypt(text_input,shift_number):
    cipher_text = ""
    for i in text_input:
        position = alphabet.index(i)
        new_position = position +shift_number
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f" The encoded text is:- {cipher_text}")


def decrypt(cypher_text,shift_amount):
    decrypt_text = ""
    for i in cypher_text:
        position = alphabet.index(i)
        new_position = position -shift_amount
        decrypt_text += alphabet[new_position]
    print(f"The decoded text is {decrypt_text}")
    
if direction == "encode":
    encrypt(text_input=text,shift_number=shift)
else:
    decrypt(cypher_text=text,shift_amount=shift)