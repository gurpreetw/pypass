# Password Generator
import string
from random import choice, randint

class Generator : 
    def __init__(self):
        # List of all letters numbers and symbols .
        self.letters = [
            string.ascii_uppercase, 
            string.ascii_lowercase, 
            string.digits, 
            string.punctuation
        ]
        self.word = ""

    # For Generator    
    def generate_multiple(self):
        inp = ""
        while True:
            inp = input("(Length) -> ")     

            for i in range (int(inp)):
                self.word = self.word + choice(self.letters[randint(0,3)])

            print(f"Random a password is : \t {self.word}\n")
            print("Press 'enter' key to continue or Enter 'a' to generate password again")
            inp = str(input("(Again)-> "))
            if not inp:
                break

    #For Manager
    def generate_one(self):
        inp = input("(Length) -> ")
        for i in range (int(inp)):
            self.word = self.word + choice(self.letters[randint(0,3)])

        return(self.word)
        



