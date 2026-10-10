import string
#Lese inn filen 

alphabet = string.ascii_lowercase


def encrypting(key, text):
    cipher_text = ""
    for letter in text:
        index = (alphabet.index(letter) + key) %26 
        cipher_text += alphabet[index]    
    print(f"Encrypted text: {cipher_text}")    
    
def decrytping(key, text):
    plain_text=""
    for letter in text:
        index = (alphabet.index(letter) - key) %26 
        plain_text += alphabet[index]  
    print(f"Decrypted text: {plain_text}") 
    
def hacker(): #TODO
    hackermode = True
    return hackermode

def inputValidation():
    if(method == "e"):
        encrypting(key, text)
    elif(method == "d"):
        decrytping(key, text)
    else: 
        print(f"Invalidinput. You wrote {method} and it needs to be either 'd' or 'e'")
        inputValidation()
#TODO i prioritert rekekfølge 
#TODO: Legg til fillesning
#TODO: Hvordan håndtere spacing? 
#TODO: Legg til valudering og testing 
#TODO: Legg til hacker modus -> hvor lang tid det trar for en hacker å løse 
print("What do you want to do today?: cipher file_to_read key method")
information = input()
cipher, text, key, method =information.split() #TODO legge til andre krypteringsmåter TODO input validation sikkerlig 
key = int(key)
inputValidation()

#c lawlyplujlgpzgæolgælhjolygvmghssgæopunzuvgvulgpzgzvgiyhålgæohægolgpzguvægkpzæøyilkgibgzvtlæopungøulawljælkpgohkgyhæolygilgmpyzægpughgåpsshnlgæohugzljvukghægyvtltlugmyllsbgilsplålgæohægopjogæolbgklzpylpgjhtlgpgzhgpgjvuxølylk 7 d
#TODO hvorfor funger det ikke å lime inn? 
#NB feil i løsningsforslaget 
#c experience 7 e
#Encrypted text: lewlyplujl, ikke lawlyplujl. 