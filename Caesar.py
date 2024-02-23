#building a caesar-cipher encryption program using string manipulation
def Caesar(text,shift):
    alphabet='abcdefghijklmnopqrstuvwxyz'
    encrypt_txt=''

    for char in text.lower():
        if char == ' ':
            encrypt_txt+=char
        else:
            index=alphabet.find(char)
            n_index=(index+shift)%len(alphabet)
            encrypt_txt+=alphabet[n_index]
        print('Plain-Text : ',text)
        print('encrypted-text : ',encrypt_txt)

text=input("Enter your Plain-text : ")
shift=int(input("Enter you shift-value : "))
Caesar(text,shift)
