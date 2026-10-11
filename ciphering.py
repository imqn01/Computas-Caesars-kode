import string
alphabet = string.ascii_lowercase

def encrypting(key, text):
    cipher_text = ""
    for letter in text:
        if letter in alphabet: 
            index = (alphabet.index(letter) + key) %26 
            cipher_text += alphabet[index]  
        else: 
            cipher_text += letter  
    print(f"Encrypted text: {cipher_text}")    
    
def decrytping(key, text):
    plain_text=""
    for letter in text:
        if letter in alphabet: 
            index = (alphabet.index(letter) - key) %26 
            plain_text += alphabet[index]  
        else: 
            plain_text += letter
    print(f"Decrypted text: {plain_text}") 
    
def hacker(): #TODO
    hackermode = True
    return hackermode

while True: 
    print("What do you want to do today?: cipher file_to_read key method")
    information = input()
    try: 
        cipher, filename, key, method =information.split() #TODO legge til andre krypteringsmåter TODO input validation sikkerlig 
        key = int(key)
    except ValueError:
        print("Enter four values. The key must be a number: cipher file_to_read key method") 
    if method not in ("e", "d"):
        print(f"Invalidinput. You wrote {method} and it needs to be either 'd' or 'e'")
        continue
    try: 
        with open(filename, encoding="utf8") as f: 
            text = f.read()
    except FileNotFoundError: 
        print(f"Could not find the file '{filename}'")
        continue
    break
    
if(method == "e"):
    encrypting(key, text)
else:
    decrytping(key, text)

        








#TODO i prioritert rekekfølge 
#TODO: Legg til fillesning
#TODO: Hvordan håndtere spacing? 
#TODO: Legg til valudering og testing 
#TODO: Legg til hacker modus -> hvor lang tid det trar for en hacker å løse 



# def filereading(filename): 
#     f = open(f"{filename}")
#     print(f.read())

#c lawlyplujlgpzgæolgælhjolygvmghssgæopunzuvgvulgpzgzvgiyhålgæohægolgpzguvægkpzæøyilkgibgzvtlæopungøulawljælkpgohkgyhæolygilgmpyzægpughgåpsshnlgæohugzljvukghægyvtltlugmyllsbgilsplålgæohægopjogæolbgklzpylpgjhtlgpgzhgpgjvuxølylk 7 d
#TODO hvorfor funger det ikke å lime inn? 
#NB feil i løsningsforslaget 
#c experience 7 e
#Encrypted text: lewlyplujl, ikke lawlyplujl. 