import string
from time import perf_counter

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
    return(output_text)
    
def encrypting(key, text): 
    return shifting(key, text)
    
def decrypting(key, text): 
    return shifting((-key), text) 
      
def hacker(filename): 
    try: 
        with open(filename, encoding="utf-8") as f: 
            text = f.read().lower()
    except FileNotFoundError:
            print(f"Could not find the file '{filename}'. Remember to add the filetype at the end, feks 'txt'")
            return 
    with open("hackerFile.txt", "w", encoding="utf-8") as output: 
        start = perf_counter()
        for key in range(len(alphabet)):
            output.write(f"Key {key}: \n")
            output.write(decrypting(key, text))
            output.write("\n\n")    
            elapsed = perf_counter() - start   
    print("All 26 possible decryptions were written to hackerFile.txt")
    print(f"Brute force of all 26 keys took {elapsed:.6f} seconds")

while True: 
    print("What do you want to do today?: cipher file_to_read key method")
    information = input()
    if information == "hackermode": 
        print("Which file do you want to hack?")
        file_to_hack = input()
        hacker(file_to_hack)
        break
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
    if(method == "e"):
        print(encrypting(key, text))
    else:
        print(decrypting(key, text))
    break
