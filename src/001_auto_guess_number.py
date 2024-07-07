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
        self.counter = 0
        self.guess = 0
        self.maximum = 50
        self.number = 0
        self.running = True
        self.threshold = 1000000

    def __verify(self) -> int:
        if self.number == self.guess:
            return 0
        elif self.number < self.guess:
            return -1
        elif self.number > self.guess:
            return 1

    def launch(self) -> None:
        print("\n\033[93mAUTOMATIC GUESS NUMBER\033[0m\n")
        self.number = randrange(1, self.threshold)
        while self.running:
            self.counter += 1
            self.guess = randrange(1, self.threshold)
            print(f"{self.counter:02d}/{self.maximum}")
            print(f"{self.guess:07d} == {self.number:07d}")
            if self.counter >= self.maximum:
                print("\033[91mCOUNTER EXCEEDED\033[0m\n")
                self.running = False
                break
            elif self.__verify() == 0:
                print("\033[92mSUCCESS\033[0m\n")
                self.running = False
            else:
                print("\033[91mFAILURE\033[0m\n")


if __name__ == "__main__":
    AutoGuessNumber().launch()
