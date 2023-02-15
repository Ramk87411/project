alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

direction = input("Type 'encoded' to  encrypt, type 'decode' to decrypt ")
text = input("Type your message:\n").lower()
shift = int(input("Type your shift number:\n"))

# defining the function of encryption and decrryption

def ceaser(start_text,shift_amount,cipher_direction):
    end_text = ""
    if direction == "decode":
        shift_amount *= -1
    for letter in start_text:
        position = alphabet.index(letter)
        new_position = position +shift_amount
        end_text += alphabet[new_position]
    print(f"your {direction}d result is {end_text}")
    
ceaser(start_text=text,shift_amount=shift,cipher_direction=direction)
###########################

