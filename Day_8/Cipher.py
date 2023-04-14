alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',]


def encrypt(text, shift):
    encode=""
    for i in text:
        position = f"{alphabet.index(i) + shift}"
        new = (int(position))
        encode += alphabet[new]
    print(encode)

    

def decrypt(text, shift):
    decode=""
    for j in text:
        position = f"{alphabet.index(j) - shift}"
        new = (int(position))
        decode+=alphabet[new]
    print(decode)

res = "yes"

while res == "yes" :
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if direction == "encode" :
        encrypt(text=text, shift=shift)
    elif direction == "decode" :
        decrypt(text=text, shift=shift)
    else:
        print("invalide input")

    res = input("Would you want to continue: yes or no!").lower()