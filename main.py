# Password manager

print("Wellcome to Password manager")

def manual():

    print("""
        Enter 'q' to quit 
        Enter 'h' for help
        Enter 'n' for new entry    
    """)

manual()
while True:

    inp = input("-> ")

    if inp.lower() == 'q':
        break
    elif inp.lower() == 'h':
        manual()
    elif inp.lower == 'n':
        pass
    else:
        print("Please enter correct input or Enter 'h' for help")


