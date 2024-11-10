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

    # Specify custom delays (in seconds) for each line
    delays = [3.2, 0.5, 0.5, 1.5, 1.5]

    # Loop through each line of lyrics and corresponding delay
    for line, delay in zip(lyrics, delays):
        # Print each character in the line with a short delay
        for char in line:
            print(char, end='', flush=True)
            sleep(0.05)  # Delay between each character
        print()  # Move to the next line after the line is complete
        sleep(delay)  # Use custom delay for each line

# Call the function to print the lyrics
print_lyrics()
