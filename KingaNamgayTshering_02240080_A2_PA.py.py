import random

class GameSuite:
    def __init__(self):
        self.scores = {
            'guess_number': 0,
            'rps': 0,
            'trivia': 0,
            'binder': 0
        }

    def menu(self):
        while True:
            print("Main Menu")
            print("1. Guess the Number Game")
            print("2. Rock Paper Scissors Game")
            print("3. Trivia Pursuit Quiz Game")
            print("4. Pokémon Card Binder Manager")
            print("5. View Overall Score")
            print("6. Exit")
            choice = input("Choose an option from (1-6): ")

            if choice == '1':
                self.guess_number_game()
            elif choice == '2':
                self.rock_paper_scissors_game()
            elif choice == '3':
                self.trivia_game()
            elif choice == '4':
                self.binder_menu()
            elif choice == '5':
                self.show_overall_score()
            elif choice == '6':
                print("Exiting the program. thanks for playing")
                break
            else:
                print("Invalid option. Please try again la.")

    def guess_number_game(self):
        target = random.randint(1, 100)
        guesses = 0
        while True:
            try:
                guess = int(input("Guess a number between 1 and 100: "))
                guesses += 1
                if guess < 1 or guess > 100:
                    print("Invalid guess. Try within 1 to 100.")
                elif guess < target:
                    print("Too low.")
                elif guess > target:
                    print("Too high.")
                else:
                    print(f"You got it right! It took you {guesses} guesses.")
                    self.scores['guess_number'] += max(0, 10 - guesses)
                    break
            except ValueError:
                print("Please enter a valid number.")

    def rock_paper_scissors_game(self):
        choices = ['rock', 'paper', 'scissors']
        wins = 0
        try:
            rounds = int(input("How many rounds are you up to the challenge? "))
            for _ in range(rounds):
                user = input("Choose rock, paper or scissors: ").lower()
                if user not in choices:
                    print("Invalid choice. Please choose the options ")
                    continue
                computer = random.choice(choices)
                print(f"Computer chose {computer}.")
                if user == computer:
                    print("Draw.")
                elif (user == 'rock' and computer == 'scissors') or \
                     (user == 'scissors' and computer == 'paper') or \
                     (user == 'paper' and computer == 'rock'):
                    print("You won against the opp")
                    wins += 1
                else:
                    print("You lost against the opp")
            print(f"Total wins: {wins}")
            self.scores['rps'] += wins
        except ValueError:
            print("Please enter a valid number of rounds.")

    def trivia_game(self):
        questions = {
            'GK': [
                ("What is the national dish of Bhutan?", ['Momo', 'Ema Datsi', 'Chowmin', 'Udon'], 'Ema Datsi')
            ],
            'History': [
                ("When was CST established?", ['2001', '2002', '2003', '2004'], '2001')
            ]
        }
        score = 0
        for category, qs in questions.items():
            print(f"Category: {category}")
            for q, options, answer in qs:
                print(q)
                for i, opt in enumerate(options):
                    print(f"{i+1}. {opt}")
                try:
                    choice = int(input("Choose 1-4: "))
                    if options[choice-1] == answer:
                        print("You got it correct! Congrats")
                        score += 1
                    else:
                        print(f"Sorry,your answer was wrong. The correct answer was {answer}.")
                except:
                    print("Invalid input.")
        print(f"Trivia Score: {score}")
        self.scores['trivia'] += score
   
    def show_overall_score(self):
        print("Overall Scores:")
        for game, score in self.scores.items():
            print(f"{game.capitalize()}: {score}")

    def binder_menu(self):
        from KingaNamgayTshering_02240080_A2_PB import PokemonBinder
        binder_app = PokemonBinder()
        binder_app.menu()
    


if __name__ == "__main__":
   Game = GameSuite()
   Game.menu() 
   
