from commands import commands

# Import modules so they register commands
import weapons
import monsters

def main():

    print("Welcome to the Adventure Game!")
    print("Commands: search, fight, quit")

    while True:

        cmd = input("> ")

        if cmd == "quit":
            break

        if cmd in commands:
            commands[cmd]()
        else:
            print("Unknown command")

if __name__ == "__main__":
    main()