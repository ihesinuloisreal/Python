alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',]




def ceasar(text, shift, direction):
    res = True
    while res == True :
        final_text=""
        if direction == "decode":
            shift *= -1 
        for i in text:
            if i in alphabet:
                position = alphabet.index(i)
                new_position = position + shift
                new = (int(new_position))
                final_text += alphabet[new]
            else:
                final_text += i
        print(final_text)
        result = input("Do you want to continue? yes or no").lower()
        if result == "no":
            res = False
            print("Good bye")

from art import art

print(art)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

shift %= 26


ceasar(text, shift, direction)