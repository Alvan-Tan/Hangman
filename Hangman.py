import random

def hang_stages(stage):
    if stage == 0:
        print("---------------")
        print("|")
        print("|")
        print("|")
        print("|")
    elif stage == 1:
        print("---------------")
        print("|       |")
        print("|")
        print("|")
        print("|")
    elif stage == 2:
        print("---------------")
        print("|       |")
        print("|       O")
        print("|")
        print("|")
    elif stage == 3:
        print("---------------")
        print("|       |")
        print("|       O")
        print("|       |")
        print("|")
    elif stage == 4:
        print("---------------")
        print("|       |")
        print("|       O")
        print("|      /|")
        print("|")
    elif stage == 5:
        print("---------------")
        print("|       |")
        print("|       O")
        print("|      /|\\")
        print("|")
    elif stage == 6:
        print("---------------")
        print("|       |")
        print("|       O")
        print("|      /|\\")
        print("|      /")
    else:
        print("---------------")
        print("|       |")
        print("|       O")
        print("|      /|\\")
        print("|      / \\")

word_list = ["function", "algorithm", "artificial", "security", "teamwork", "google", "facebook", "decimal"]

def get_answer():
    return random.choice(word_list)

def main():
    guessed_letters = []
    guessed_words = []
    print("Hello player, welcome to the hangman game")
    answer = get_answer()
    stage = 0
    hang_stages(stage)
    print("Guessed letters", guessed_letters)
    print("Guessed words", guessed_words)
    progress = "_ "*len(answer)
    print("Guess the word:",progress)
    while stage <7:
        guess = input("Please guess a letter or a word").lower()
        if guess in guessed_letters or guess in guessed_words:
            print("You have already made this guess before! Try again.")
        else:
            if len(guess) == 1:
                guessed_letters.append(guess)
                if guess in answer:
                    for i in range(len(answer)):
                        if answer[i] == guess:
                            progress = progress.split(" ")
                            progress[i] = guess
                            progress = " ".join(progress)
                    if "_" not in progress:
                        print(f"Congrats you win! the word is {answer}")
                        break
                    else:
                        hang_stages(stage)
                        print("Guessed letters", guessed_letters)
                        print("Guessed words", guessed_words)
                        print("Guess the word:",progress)
                else:
                    print("You have made the wrong guess :(")
                    stage += 1
                    hang_stages(stage)
                    print("Guessed letters", guessed_letters)
                    print("Guessed words", guessed_words)
                    print("Guess the word:", progress)
            else:
                guessed_words.append(guess)
                guess = guess.split()
                guess = " ".join(guess)
                if guess == answer:
                    print(f"Congrats you win! the word is {answer}")
                    break
                else:
                    print("You have made the wrong guess :(")
                    stage += 1
                    hang_stages(stage)
                    print("Guessed letters", guessed_letters)
                    print("Guessed words", guessed_words)
                    print("Guess the word:", progress)
    if stage<7:
        pass
    else:
        print(f"Oh no, you lost! The answer is {answer}")

main()





