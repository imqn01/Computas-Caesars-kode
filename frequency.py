from collections import Counter
import re
import string
from time import perf_counter


alphabet = string.ascii_uppercase

with open("shh.txt", encoding="utf-8") as f:
    letters = re.sub(r"[^A-Z]", "", f.read().upper())

trigrams = [letters[i:i + 3] for i in range(len(letters) - 2)] 

for trigram, count in Counter(trigrams).most_common(3):
    start = perf_counter()
    key = (alphabet.index(trigram[0]) - alphabet.index("T")) % 26 # shift that would turn T into this trigram's first letter
    shifted_the = "".join(alphabet[(alphabet.index(c) + key) % 26] for c in "THE") # does the same shift also turn H and E into the other two letters?

    if shifted_the == trigram:
        print(f"{trigram} ({count}x) is THE shifted by {key}")
        elapsed = perf_counter() - start  
        print(f"To find the key to turn one of the top three trigrams to 'THE' took {elapsed:.6f} seconds")
    else:
        print(f"{trigram} ({count}x) is not THE")