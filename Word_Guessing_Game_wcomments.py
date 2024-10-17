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


    

def set_difficulty(education_level):
    # Set the number of turns (difficulty) based on education level.
    if education_level.lower() == 'elementary':
        return 15  # Easier level: 15 turns.
    elif education_level.lower() == 'high school':
        return 12  # Moderate level: 12 turns.
    elif education_level.lower() == 'college':
        return 8  # Harder level: 8 turns.
    else:
        return 10  # Default turns if education level is unspecified or invalid.

def play_game(name, education_level, used_words):
    # Get the word list for the given education level.
    words = choose_word_list(education_level)
    
    # Filter out words that have already been used.
    available_words = [word for word in words if word not in used_words]
    
    # If no words are left to play, notify the player and end the game.
    if not available_words:
        print(f"{name}, you've played all the words for your education level!")
        return False  # Game over.
    
    # Randomly choose a word from the remaining (unused) words.
    word = random.choice(available_words)
    
    # Add the chosen word to the set of used words to avoid repeating it.
    used_words.add(word)
    
    # Set the number of turns based on the player's education level.
    turns = set_difficulty(education_level)

    print("Guess the characters")  # Prompt to start guessing.
    guesses = ''  # Store the guessed characters.

    # Game loop that continues until the player wins or runs out of turns.
    while turns > 0:
        failed = 0  # Counter for unguessed characters.

        # Display the word, replacing unguessed letters with underscores.
        for char in word:
            if char in guesses:
                print(char, end=" ")  # Print the correctly guessed character.
            else:
                print("_", end=" ")  # Print an underscore for unguessed letters.
                failed += 1  # Increment the fail counter for each missing letter.

        # If there are no missing letters, the player wins.
        if failed == 0:
            print(f"\nYou Win, {name}!")  # Congratulate the player.
            print("The word is:", word)  # Reveal the full word.
            break  # Exit the loop as the player has won.

        print()  # New line for clarity.
        guess = input("Guess a word: ").lower()  # Prompt the player to guess a character.
        guesses += guess  # Add the guessed character to the list of guesses.

        # If the guess is incorrect, reduce the number of remaining turns.
        if guess not in word:
            turns -= 1  # Decrease turns by one.
            print("Wrong")  # Notify the player of a wrong guess.
            print(f"You have {turns} more guesses")  # Show how many guesses are left.

            # If no turns are left, the player loses.
            if turns == 0:
                print(f"You Lose, {name}.\n The word was: {word}")  # Reveal the word after a loss.
    
    # After the game ends, ask the player if they want to play again.
    play_again = input("Do you want to play again? (yes/no): ").lower()
    
    # Return True if the player wants to play again, otherwise False.
    return play_again == 'yes'

def main():
    display_title()  # Display the game title and visuals.
    
    # Prompt the player for their name and education level.
    name = input("What is your name? ")
    education_level = input("What is the highest level of school you attended? (Elementary, High School, College): ")
    
    print("Good Luck!", name)  # Wish the player good luck.
    
    used_words = set()  # Initialize a set to track words that have been used.

    # Game loop that continues while the player wants to play.
    while play_game(name, education_level, used_words):
        print("\nStarting a new game...\n")  # Start a new round.

    print("Thanks for playing!")  # Thank the player after the game ends.

# Start the game if the script is executed directly.
if __name__ == "__main__":
    main()

