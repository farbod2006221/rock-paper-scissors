import random

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    print("Enter your choice: rock, paper, or scissors")
    
    # Possible choices
    choices = ['rock', 'paper', 'scissors']
    
    while True:
        # Get user input
        user_choice = input("Your choice: ").lower()
        
        # Validate user input
        if user_choice not in choices:
            print("Invalid choice. Please try again.")
            continue
            
        # Computer makes a random choice
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")
        
        # Determine the winner
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissors' and computer_choice == 'paper'):
            print("You win!")
        else:
            print("Computer wins!")
        
        # Ask to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

# Start the game
play_game()