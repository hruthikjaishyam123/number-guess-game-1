import random 
import time

def intro():
    print("May I ask you for your name?")
    name = input() 
    print(name + ", we are going to play a game. I am thinking of a number between 1 and 200")
    time.sleep(.5)
    print("Go ahead. Guess!")

def pick(number):
    guessesTaken = 0
    while guessesTaken < 6: 
        time.sleep(.25)
        enter = input("Guess: ") 
        try: 
            guess = int(enter)  

            if 1 <= guess <= 200: 
                guessesTaken += 1 
                if guessesTaken < 6:
                    if guess < number:
                        print("The guess of the number that you have entered is too low")
                    elif guess > number:
                        print("The guess of the number that you have entered is too high")
                    if guess != number:
                        time.sleep(.5)
                        print("Try Again!")
                if guess == number:
                    break 
            else: 
                print("Silly Goose! That number isn't in the range!")
                time.sleep(.25)
                print("Please enter a number between 1 and 200")

        except ValueError: 
            print("I don't think that " + enter + " is a number. Sorry")

    if guess == number:
        guessesTaken = str(guessesTaken)
        print('Good job, ' + name + '! You guessed my number in ' + guessesTaken + ' guesses!')

    if guess != number:
        print('Nope. The number I was thinking of was ' + str(number))

def main():
    play_again = "yes"
    while play_again.lower() in ["yes", "y"]:
        number = random.randint(1, 200)  
        intro()
        pick(number)
        print("Do you want to play again? (yes/no)")
        play_again = input()
        if play_again.lower() not in ["yes", "y"]:
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
