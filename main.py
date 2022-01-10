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
manager = Manager()
gen = Generator()
# print(f"\n\n {manager} \n\n")

# Main Loop
while True:
    inp = input("-> ")

    if inp.lower() == 'q':
        manager.close_db()
        break
    elif inp.lower() == 'h':
        manual()
    elif inp.lower() == 'n':
        manager.new_entry()
    elif inp.lower() == 'd':
        pass
    elif inp.lower() == 'g':
        password = gen.generate_multiple()
        print(f"Random a password is : \t {password}")


    else:
        print("Please enter correct input or Enter 'h' for help")


