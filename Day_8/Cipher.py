alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',]

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
def encrypt(text, shift):
    texts = [*text]
    encode=[]
    for i in texts:
        print(f"{i} {alphabet.index(i)+1}")
        position = f"{alphabet.index(i) + shift}"
        new = (int(position))
        encode.append((alphabet[new]))
    print(encode)



encrypt(text, shift) 