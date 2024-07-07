from random import randrange


# Find a secret integer between 1 and 1000000 in less than 50 guesses.
# Write a function that solves the game without user input.
# Returns the solution by using the function verify() with the following specification:
# Returns:
#      0 if the guess is the solution, your program won
#      -1 if the solution is smaller than the guess parameter
#      1  if the solution is bigger than the guess parameter
# You are not allowed to call verify() more that 50 times or you lose.
class AutoGuessNumber:
    def __init__(self) -> None:
        self.attempts = 0
        self.maximum = 50
        self.number1 = 0
        self.number2 = 0
        self.running = True
        self.threshold = 1000000

    def __verify(self) -> int:
        if self.number1 == self.number2:
            return 0
        elif self.number1 < self.number2:
            return -1
        elif self.number1 > self.number2:
            return 1

    def launch(self) -> None:
        print("\n\033[93mAUTOMATIC GUESS NUMBER\033[0m\n")
        while self.running:
            self.attempts += 1
            self.number1 = randrange(1, self.threshold)
            self.number2 = randrange(1, self.threshold)
            print(f"ATTEMPT {self.attempts}/{self.maximum}")
            print(f"COMPUTE {self.number1} WITH {self.number2}")
            if self.attempts >= self.maximum:
                print("\033[91mALLOVER, MAX ATTEMPTS EXCEEDED\033[0m\n")
                self.running = False
                break
            elif self.__verify() == 0:
                print("\033[92mCORRECT, YOU WIN\033[0m\n")
                self.running = False
            else:
                print("\033[91mINVALID, YOU LOSE\033[0m\n")


if __name__ == "__main__":
    AutoGuessNumber().launch()
