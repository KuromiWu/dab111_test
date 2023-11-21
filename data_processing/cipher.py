

import string

letters = string.ascii_lowercase

def caesar_cipher (plain_text, shift):
    #plain_text=plain_text.lowercase
    cipher_text =''
    for ch in plain_text.lower():      # change to lowercase
        if ch.isspace():
            cipher_text +=ch
        else:
         cipher_idx = (letters.find(ch) + shift) % 26
         cipher_chr =  letters [ cipher_idx]
         cipher_text += cipher_chr
    return cipher_text 

def double_caesar(plain_text, shift_1, shift_2):
    idx =0
    cipher_text=''
    for ch in plain_text:
        if ch.isspace():
            cipher_text += ch
            continue
        if idx % 2 ==0:
            cipher_text+= caesar_cipher(ch, shift_1)
        else:
            cipher_text+= caesar_cipher(ch, shift_2)
        idx +=1
    return cipher_text   

def main():
    text =input ('Input your secret message')
    shift_1 = int (input('Enter first shift:'))
    shift_2 = int (input('Enter Second shift:'))
    cipher_text=double_caesar(text,shift_1, shift_2)
    print(cipher_text)
    
if __name__ =='__main__':
    main()