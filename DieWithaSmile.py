





from time import sleep

def print_lyrics():
    # Die With A Smile -- Bruno Mars
    
    lyrics = [
        "Nobody's promised tomorrow",                                  #0
        "So I'ma love you every night like it's the last night",       #1
        "Like it's the last night",                                    #2
        "If the world was ending, I'd wanna be next to you...🎶",      #3
        "If the party was over and our time on Earth was through...🎶",#4
        "I'd wanna hold you just for a while and die with a smile.🎶", #5
        "If the world was ending, I'd wanna be next to you.🎶"         #6
    ]
    # Custom delays 
    delays = [3.0, 1.8, 0.4, 5.8, 5.2, 7.2, 6.2]  #0,  #1,  #2,  #3,  #4,  #5,  #6
    for line, delay in zip(lyrics, delays):
        for char in line:
            print(char, end='', flush=True)
            sleep(0.05) 
        print()  
        sleep(delay) 

print_lyrics()
