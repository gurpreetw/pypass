# Password manager
from generator import Generator
from manager import Manager

print("Wellcome to Password manager")

def manual():

    print("""
        Enter 'q' to quit 
        Enter 'h' for help
        Enter 'g' to generate password
        Enter 'n' for new entry
        Enter 'd' to delete
    """)

manual()
# Main Loop
manager = Manager()
print(f"\n\n {manager} \n\n")

while True:
    inp = input("-> ")

    if inp.lower() == 'q':
        manager.close_db()
        break
    elif inp.lower() == 'h':
        manual()
    elif inp.lower() == 'n':
        pass
    elif inp.lower() == 'd':
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


