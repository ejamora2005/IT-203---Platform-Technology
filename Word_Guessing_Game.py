import random

def display_title():
    print("""              
            __        _______ _     ____ ___  __  __ _____ 
            \ \      / / ____| |   / ___/ _ \|  \/  | ____|
             \ \ /\ / /|  _| | |  | |  | | | | |\/| |  _|  
              \ V  V / | |___| |__| |__| |_| | |  | | |___ 
               \_/\_/  |_____|_____\____\___/|_|  |_|_____|
                             _____ ___                                      
                            |_   _/ _ \                                     
                              | || | | |                                    
                              | || |_| |                                    
                              |_|_\___/
__        __ __  ___   ____     ______   _ _____ ____ ___  ___ _   _  ____      
\ \      / / _ \|  _ \|  _ \   / ___| | | | ____/ ___/ ___|_ _| \ | |/ ___| 
 \ \ /\ / / | | | |_) | | | | | |  _| | | |  _| \___ \___ \| ||  \| | |  _  
  \ V  V /| |_| |  _ <| |_| | | |_| | |_| | |___ ___) |__) | || |\  | |_| | 
   \_/\_/  \___/|_| \_\____/   \____|\___/|_____|____/____/___|_| \_|\____| 
                        ____    _    __  __ _____
                       / ___|  / \  |  \/  | ____|                          
                      | |  _  / _ \ | |\/| |  _|                             
                      | |_| |/ ___ \| |  | | |___                            
                       \____/_/   \_\_|  |_|_____|                         
                       """)

def word_list(education_level):
    elementary_words = ['rain', 'ball', 'cat', 'dog', 'book', 'sun', 'tree', 'fish', 'hat', 'star']
    high_school_words = ['rainbow', 'computer', 'science', 'player', 'board', 'planet', 'gravity', 'equation', 'cell', 'internet']
    college_words = ['programming', 'mathematics', 'condition', 'reverse', 'geeks', 'algorithm', 'database', 'architecture', 'recursion', 'syntax']
    
    if education_level.lower() == 'elementary':
        return elementary_words
    elif education_level.lower() == 'high school':
        return high_school_words
    elif education_level.lower() == 'college':
        return college_words
    else:
        return high_school_words  

def difficulty(education_level):
    if education_level.lower() == 'elementary':
        return 15 
    elif education_level.lower() == 'high school':
        return 12  
    elif education_level.lower() == 'college':
        return 8   
    else:
        return 10 

def play_game(name, education_level, used_words):
    words = word_list(education_level)
    available_words = [word for word in words if word not in used_words]
    
    if not available_words:
        print(f"{name}, you've played all the words for your education level!")
        return False
    
    word = random.choice(available_words)
    used_words.add(word)
    turns = difficulty(education_level)

    print("Guess the word:")
    guesses = set() 
    
    while turns > 0:
        failed = 0

        for char in word:
            if char in guesses:
                print(char, end=" ")
            else:
                print("_", end=" ")
                failed += 1

        if failed == 0:
            print(f"\nYou Win, {name}!")
            print("The word is:", word)
            break

        print()
        guess = input("Guess a character: ").lower()

    
        if guess in guesses:
            print(f"You've already used letter '{guess}'. Try again.")
        else:
            guesses.add(guess)
            if guess not in word:
                turns -= 1
                print("Wrong")
                print(f"You have {turns} more guesses")

                if turns == 0:
                    print(f"You Lose, {name}.\n The word was: {word}")
    
    play_again = input("Do you want to play again? (yes/no): ").lower()
    return play_again == 'yes'

def main():
    display_title()
    
    name = input("What is your name? ")
    education_level = input("What is the highest level of school you attended? (Elementary, High School, College): ")
    
    print("Good Luck!", name)
    used_words = set()

    while play_game(name, education_level, used_words):
        print("\nStarting a new game...\n")

    print("Thanks for playing!")

if __name__ == "__main__":
    main()
