import string
alphabet = string.ascii_lowercase

def shifting(key, text): 
    input_text = text
    output_text =""
    for letter in input_text:
        if letter in alphabet: 
            index = (alphabet.index(letter) + key) %26 
            output_text += alphabet[index]  
        else: 
            output_text += letter  
    print(output_text)
    
def encrypting(key, text): 
    shifting(key, text)
    
def decrypting(key, text): 
    shifting((-key), text) 
      
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
        continue
    if method not in ("e", "d"):
        print(f"Invalidinput. You wrote {method} and it needs to be either 'd' or 'e'")
        continue
    try: 
        with open(filename, encoding="utf8") as f: 
            text = f.read().lower()
    except FileNotFoundError: 
        print(f"Could not find the file '{filename}'. Remember to add the filetype at the end, feks 'txt'")
        continue
    break
    
if(method == "e"):
    encrypting(key, text)
else:
    decrypting(key, text)

        








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