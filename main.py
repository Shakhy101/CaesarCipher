from art import logo
from alpha import alphabet

def caesar(start_text, shift_amount, cipher_direction): 
    end_text = ""
    if cipher_direction == "decode":
            shift_amount = -shift_amount #posouvam se zpet 

    for letter in start_text:
        if letter not in alphabet: #Osetreni neznamych znaku
            end_text += letter
        position = alphabet.index(letter) #nova metoda (urci index prvku v listu list.index(prvek) )
        new_position = (position + shift_amount) % len(alphabet)#nemusim resit preteceni listu zespodu, protoze zaporny index jde zezadu, a jinak vse resi mod :)
        end_text += alphabet[new_position]
    print(f"The {cipher_direction}d text is: {end_text}")

print(logo)
run_again = True
while run_again:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    again = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if again == "no":
        run_again = False

print("Good bye.")