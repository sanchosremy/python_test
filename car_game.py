"""Car game
"""
COMMAND = ""
STARTED = False
while COMMAND.lower() != "quit":
    COMMAND = input("> ")
    if COMMAND.lower() == "start":
        if STARTED:
            print("Car is already started!")
        else:
            STARTED = True
            print("Car started...")
    elif COMMAND.lower() == "stop":
        if not STARTED:
            print("Car is already stopped!")
        else:
            STARTED = False
            print("Car stopped.")
    elif COMMAND.lower() == "help":
        print(
            """
start - to start the car
stop - to stop the car
quit - to quit
        """
        )
    elif COMMAND == "quit":
        break
    else:
        print("Sorry i don't understand that!")
