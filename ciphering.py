
import string
#Lese inn filen 

#Velg alfabet

#modulo 26(alfabetlengden)
#alfabetet må være indeksert 

alphabet = string.ascii_lowercase
#print(alphabet.index("g"))

text = "abba"
key =1
def encrypting(key, text):
    encrypted_text = ""
    for letter in text:
        encrypted_letter_index = (alphabet.index(letter) + key) %26 #henter ut indeksen til bokstaven, legger til nøkkelen og moduler med 26
        encrypted_text += alphabet[encrypted_letter_index]    
    print(encrypted_text)
     
encrypting(key, text)
    
    
def decrytping(key, text):
    decrypted_text =""
    #for loop gjennom bokstavene 
    
    
    return decrypted_text 