import pyfiglet
import random
  
# result = pyfiglet.figlet_format("EnD", font="slant")
# print(result)

result = pyfiglet.figlet_format("EnD", font = "slant" )
print(result)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',' ','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',' ']

def encrypt(text, shifts):
  cipher_text=""
  for letter in text:
    position=alphabet.index(letter)
    new_position=position+shifts
    cipher_text+=alphabet[new_position]
  print(cipher_text)
  cont=input("do you wish to continue \n  Write yes to continue and no to finish").lower()
  if cont =="yes":
      repeat()

def decrypt(text,shifts):
    original_texts=""
    for letter in text:
        position=alphabet.index(letter)
        new_position=position-shifts
        original_texts+=alphabet[new_position]
    print(original_texts)
    cont=input("do you wish to continue \n  Write yes to continue and no to finish \n").lower()
    if cont =="yes":
      repeat()

def repeat():
    direction=input("what you want to do? \n Type encrypt for the encryption and Type decrypt for decryption \n").lower()
    if direction=="encrypt":
            text = input("Type your message:\n").lower()
            shift = int(input("Type any number key:\n"))
            encrypt(text, shift)
    elif direction=="decrypt":
            text = input("Type your message:\n").lower()
            shift = int(input("Type any number key:\n"))
            decrypt(text, shift)
    else:
            print("invalid command")

repeat()










    
    








