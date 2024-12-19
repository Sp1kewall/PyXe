import sys

def command(argument: str = None):
    print("Hello world!")
    if argument != None:
        print(f"Your argument is {argument}")

if __name__ == "__main__":
    command(sys.argv[1:])