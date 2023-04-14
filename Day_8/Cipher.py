alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',]

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
def encrypt(text, shift):
    
    # texts = [*text]
    encode=""
    for i in text:
        print(f"{i} {alphabet.index(i)+1}")
        position = f"{alphabet.index(i) + shift}"
        new = (int(position))
        encode += alphabet[new]
    print(encode)

    

# def decrypt():
#     text = input("Type your message:\n").lower()
#     shift = int(input("Type the shift number:\n"))
#     texts = [*text]
#     decode=[]
#     for j in encode:
#         position = f"{alphabet.index(j) - shift}"
#         new = (int(position))
#         decode.append((alphabet[new]))
#     print(decode)


encrypt(text=text, shift=shift) 