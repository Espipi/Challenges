def madlib():
    """ HoneyCode Team try to create a madlib game. 
    Here the function provided for this expectation"""
    
    #packages we need
    import os
    import re
    import random
    random.seed()
    
    #local machine path
    #Replace here the url path of your directory template
    path=r"D:\Python_Project\Nanodegree\templates"
    #for ec2 environment path
    #path="/home/ec2-user/environment/templates"
   
    os.chdir(path) # os.chidr() to go to my directory
    file = random.choice(os.listdir()) # choising randomly file with random command 
    #Check random file which the code choose for the game
    print(file)
    
    ##Opening and reading
    
    f=open(file, encoding="utf8")
    sentence = f.read()
    print(type(sentence))
    
    f.close()
    #Check on back the sentence
    #print(sentence)
    
    ##Store words in variable by compiling it with regular expression module
    
    regex = re.compile(r'{adjective}|{adverb}|{a place}|{verb}|{body_part}|{noun}|{verb in ing}|{animal}|{plural noun}|{foreign country}|{number}|{past tense verb}|{adjective ending in -est}|{type of liquid}')
    
    #More funny
    name_of_player = input("Please provide fantasy game's name: ")
    emoji_code = "\U0001F600"
    print(f"Hello {name_of_player}{emoji_code}, welcome to madlib's game!!!")
    
    ##conditions
    
    while True:
        match_word = regex.search(sentence)
        #print(match_word)
        if match_word == None:
            
            break # Stop my function when there is no match words
            
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
        
        sentence = sentence.replace(match_word.group(), word.lower(), 1)
    print(f"**********{name_of_player} {emoji_code}, here is your story on madlib game************************")

    print(sentence)
    
    print("***********************************************************")
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
        print("Please enter a correct input (y/n)!!")  # Print a statement to the user
        restart()  # Repeat the Function


# Run the game
if __name__ == '__main__':
    story = madlib()
    print(story)
