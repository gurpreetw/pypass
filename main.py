# Password manager
from  generator import Generator
print("Wellcome to Password manager")

def manual():

    print("""
        Enter 'q' to quit 
        Enter 'h' for help
        Enter 'n' for new entry    
        Enter 'g' to generate password
    """)

manual()
# Main Loop
while True:
    inp = input("-> ")

    if inp.lower() == 'q':
        break
    elif inp.lower() == 'h':
        manual()
    elif inp.lower() == 'n':
        pass
    elif inp.lower() == 'g':
        # for testing only, i might sift this code block to genetor.py later!
        print("Enter length password of password you want :")
        while inp != "\n":
            inp = input("(Length) -> ")
            password = Generator(num=inp).generate()
            print(f"Random a password is : \t {password}")

            print("Press 'enter' to continue and Press 'a' to generate password again")    
    else:
        print("Please enter correct input or Enter 'h' for help")


