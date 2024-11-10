from time import sleep
import time

def print_lyrics():
    # Lyrics or phrases to print out, line by line
    lyrics = [
        "🎶 Code all day, code all night,",
        "Syntax errors giving me a fright.",
        "If the code runs, I'll feel alright,",
        "Python's here to make it tight. 🎶",
        "Loading libraries one by one,",
        "Import time, now let's have some fun.",
        "Sleep a second, take a pause,",
        "Debugging code is my cause."
    ]

    # Specify custom delays (in seconds) for each line
    delays = [1.5, 2, 2.5, 1.5, 2, 1, 3, 2]

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
