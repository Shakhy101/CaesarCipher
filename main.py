from art import logo
from alpha import alphabet

def caesar(start_text, shift_amount, cipher_direction): 
    end_text = ""
    over_index = len(alphabet) #potrebuji zjistit index nasledujici po poslednim abych mohl pouzit modulo pro pripadne zacykleni posunu
    if cipher_direction == "decode":
            shift_amount *= -1 #posouvam se zpet

    for letter in start_text:
        if letter not in alphabet: #Osetreni neznamych znaku
            end_text += letter
        else:    
            position = alphabet.index(letter) #nova metoda (urci index prvku v listu list.index(prvek) )
            position_shifted = position + shift_amount
            if position_shifted < 0: #pokud dostanu zaporne cislo, musim se presunout na konec listu
                position_shifted = len(alphabet) + position_shifted #delka listu + zaporny position_shifted mi da spravne pismeno
            else: 
                position_shifted = position_shifted % over_index 
            end_text += alphabet[position_shifted]
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