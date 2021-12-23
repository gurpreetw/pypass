# Password Generator
import string
from random import choice, randint

class Generator : 
    def __init__(self, num):
        # List of all letters numbers and symbols .
        self.letters = [
            string.ascii_uppercase, 
            string.ascii_lowercase, 
            string.digits, 
            string.punctuation
        ]
        self.num = int(num)

    #Generating the password    
    def generate(self):
        self.word = ""
        for i in range (self.num):
            self.word = self.word + choice(self.letters[randint(0,3)])    
        return self.word


