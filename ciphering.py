import string
from time import perf_counter
import sys
from time import sleep
from collections import Counter
import re
import string
from time import perf_counter

alphabet = string.ascii_lowercase

#Selve Caesar logikken
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

#Hacker mode

def frequency(filename): 
    with open(filename, encoding="utf-8") as f:
        letters = re.sub(r"[^a-z]", "", f.read().lower())

    trigrams = [letters[i:i + 3] for i in range(len(letters) - 2)] 

    for trigram, count in Counter(trigrams).most_common(3):
        start = perf_counter()
        key = (alphabet.index(trigram[0]) - alphabet.index("t")) % 26 # shift that would turn T into this trigram's first letter
        shifted_the = "".join(alphabet[(alphabet.index(c) + key) % 26] for c in "the") # does the same shift also turn H and E into the other two letters?

        if shifted_the == trigram:
            elapsed = perf_counter() - start 
            print(f"{trigram} ({count}x) is THE shifted by {key}")
            print(f"To find the key to turn one of the top three trigrams to 'THE' took {elapsed:.6f} seconds")
        else:
            print(f"{trigram} ({count}x) is not THE")
      
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
    find_key = input("Do you want to automatically find the secret key (y/n)?")
    if find_key == "y": 
        frequency(filename)
    else: 
        pass
        
    
#TODO hacker mode extended frequency 

#Hackermode UI 
GREEN = "\033[92m"
RESET = "\033[0m"

def typewriter(text, delay=0.03, color=GREEN):
    for char in text:
        sys.stdout.write(color + char + RESET)
        sys.stdout.flush()
        sleep(delay)
    print()

def progress_bar(label, steps=30, delay=0.05):
    for i in range(steps + 1):
        bar = "█" * i + "-" * (steps - i)
        print(f"\r{GREEN}{label} [{bar}] {i * 100 // steps}%{RESET}", end="", flush=True)
        sleep(delay)
    print()
    
import random, string, shutil

def matrix_rain(duration=2.0, delay=0.05):
    width = shutil.get_terminal_size().columns
    end = perf_counter() + duration
    while perf_counter() < end:
        line = "".join(
            random.choice(string.ascii_letters + string.digits) if random.random() < 0.15 else " "
            for _ in range(width)
        )
        print(GREEN + line + RESET)
        sleep(delay)
    
#Interaksjonen 
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
        print(encrypting(key, text))
    else:
        print(decrypting(key, text))
    break
