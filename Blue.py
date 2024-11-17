from time import sleep
import time

def print_lyrics():
    # Blue - Yung Kai
    lyrics = [
        "You're all that I want - this life🎶",
        "I'll imagine we fell in love.",
        "I'll nap under moonlight skies with you,",
        "I think I'll picture us, you with the waves. 🎶",
        "The ocean's colors on your face."
    ]

    #custom delays 
    delays = [3.2, 0.5, 0.5, 1.5, 1.5]

    for line, delay in zip(lyrics, delays):
        for char in line:
            print(char, end='', flush=True)
            sleep(0.05) 
        print()  
        sleep(delay) 

print_lyrics()