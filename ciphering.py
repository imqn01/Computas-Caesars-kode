import string
import sys
from time import sleep
from collections import Counter
import re
from time import perf_counter
import random, string, shutil


alphabet = string.ascii_lowercase
#CAEASAR
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

#HACKERMODE
def frequency(filename):
    start = perf_counter()
    with open(filename, encoding="utf-8") as f:
        text = f.read().lower()
    letters = re.sub(r"[^a-z]", "", text) #alt som ikke er a til z erstates med ingenting. Fjerner mellomrom, punktum og tall. 
    trigrams = [letters[i:i + 3] for i in range(len(letters) - 2)] #Deler alle bokstaver inn i trigrams. Isa, sab. Stopper to tall før slutten så det ikke blir index out of bounce. 

    for trigram, count in Counter(trigrams).most_common(3): #teller hvor ofte et trigram kommer og gir et par med topp tre og deres frekvens
        for key in range(26): #tester ut alle nøkler i most common trigrams og ser om noen av de blir THE. 
            if decrypting(key, trigram) == "the":
                print(f"\n{trigram} ({count}x) is 'the' shifted by {key}")
                with open("FrequencyHack.txt", "w", encoding="utf-8") as output: 
                    output.write(f"Key {key}: \n")
                    output.write(decrypting(key, text))
                    elapsed = perf_counter() - start 
                print(f"The decrpyted text was written into FrequencyHack.txt. Decrypting time = {elapsed:.6f}")
                return key
    print("Could not find 'the' among the top three trigrams.")
                
      
def hacker(filename): 
    try: 
        with open(filename, encoding="utf-8") as f: 
            text = f.read().lower()
    except FileNotFoundError:
            print(f"Could not find the file '{filename}'. Remember to add the filetype at the end, feks 'txt'")
            return 
    with open("bruteForce.txt", "w", encoding="utf-8") as output: 
        start = perf_counter()
        for key in range(len(alphabet)):
            output.write(f"Key {key}: \n")
            output.write(decrypting(key, text))
            output.write("\n\n")    
        elapsed = perf_counter() - start   
    print(f"\nAll 26 possible decryptions were written to bruteForce.txt")
    print(f"Brute force of all 26 keys took {elapsed:.6f} seconds")
    find_key = input("Do you want to automatically find the secret key (y/n)?")
    if find_key == "y": 
        frequency(filename)
    else: 
        pass
    
#HACKERMODE DESIGN
GREEN = "\033[92m" #'\033[95m' #"\033[92m" lilla eller grønn?
RESET = "\033[0m"

def typewriter(text, delay=0.03, color=GREEN):
    for char in text:
        sys.stdout.write(color + char + RESET) #printer en bokstav i grønn og resets fargen. 
        sys.stdout.flush() #får terminalen til å vise bokstaven akkurat nå
        sleep(delay) #venter, får det til å se ut som typing 
    print()

def matrix_rain(duration=2.0, delay=0.05): #TODO veldig usikker
    width = shutil.get_terminal_size().columns #bredden til terminalen 
    end = perf_counter() + duration #hvor lang tid animasjonen skal bruke
    while perf_counter() < end:
        line = "".join(
            random.choice(string.ascii_letters + string.digits) if random.random() < 0.15 else " "
            for _ in range(width)
        )
        print(GREEN + line + RESET)
        sleep(delay)
    
#USER INTERACTION 
while True: 
    print("What do you want to do today?: cipher file_to_read key method")
    information = input()
    if information == "hackermode": 
        matrix_rain()
        typewriter("ACCESS GRANTED. Initiating hacker mode")
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
        print("\nEncrypted message: \n" + encrypting(key, text))
    else:
        print("\nDecrypted message: \n" +decrypting(key, text))
    break