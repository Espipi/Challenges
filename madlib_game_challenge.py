def madlib():
    #packages we need
    import os
    import re
    import random
    random.seed()
    path="/home/ec2-user/environment/templates"
    #local machine path
    #path=r"D:\Python_Project\Nanodegree\templates"
    os.chdir(path)
    file = random.choice(os.listdir())
    #Check random on the code
    print(file)
    
    ##Opening and reading
    
    f=open(file, encoding="utf8")
    sentence = f.read()
    print(type(sentence))
    
    f.close()
    
    print(sentence)
    
    ##Search
    
    regex = re.compile(r'{adjective}|{adverb}|{a place}|{verb}|{body_part}|{noun}|{verb in ing}|{animal}|{plural noun}|{foreign country}|{number}|{past tense verb}|{adjective ending in -est}|{type of liquid}')
    
    #More funny
    name_of_player = input("Please provide fantasy game's name: ")
    emoji_code = "\U0001F600"
    print(f"Hello {name_of_player}{emoji_code}, welcome to madlib's game!!!")
    
    ##conditions
    
    while True:
        match_word = regex.search(sentence)
        print(match_word)
        given_word = []
        if match_word == None:
            
            break
            
        elif match_word.group() == '{adjective}':
            print(f"Please {name_of_player}, enter an adjective:")
        elif match_word.group() == '{verb}':
            print(f"Please {name_of_player}, enter a verb:")
        elif match_word.group() == '{noun}':
            print(f"Please {name_of_player}, enter a noun:")
        elif match_word.group() == '{adverb}':
            print(f"Please {name_of_player}, enter a adverb:")
        elif match_word.group() == '{plural noun}':
            print(f"Please {name_of_player}, enter a plural noun:")
        elif match_word.group() == '{number}':
            print(f"Please {name_of_player}, enter a number:")
        elif match_word.group() == '{past tense verb}':
            print(f"Please {name_of_player}, enter a past tense verb:")
        elif match_word.group() == '{adjective ending in -est}':
            print(f"Please {name_of_player}, enter a adjective ending in -est:")
        elif match_word.group() == '{body_part}':
            print(f"Please {name_of_player}, enter a body part:")
        elif match_word.group() == '{verb in ing}':
            print(f"Please {name_of_player}, enter a verb ending in -ing:")
        elif match_word.group() == '{animal}':
            print(f"Please {name_of_player}, enter an animal:")
        elif match_word.group() == '{foreign country}':
            print(f"Please {name_of_player}, enter a foreign country:")
        elif match_word.group() == '{type of liquid}':
            print(f"Please {name_of_player}, enter a type of liquid:")
        elif match_word.group() == '{a place}':
            print(f"Please {name_of_player}, enter a place:")
        word = input()

        #function to store words provided and print out it
        
        #####
        
        sentence = sentence.replace(match_word.group(), word.lower(), 1)
    print("**********Here The Story************************")

    print(sentence)
    
        # Restart Function
    restart()

# Restart Function
def restart():
    replay = str(input("would you like to replay the game? (y/n): ").lower())  # Getting user input
    if replay == "y":  # Check if the input is equal to "y"
        madlib()  # If it is than run main() again
    elif replay == "n":  # Else if the input is "n"
        print("Goodbye!!!")
    else:  # Else if the input is not y or n then
        print("Please enter a correct input!!")  # Print a statement to the user
        restart()  # Repeat the Function


# Run the game
if __name__ == '__main__':
    story = madlib()
    print(story)