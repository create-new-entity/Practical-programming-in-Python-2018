
rateUtoE = None
rateEtoU = None

while True:
    command = input("Give a command: ")
    command = command.split(" ")
    try:
        if (len(command) == 3) and (command[0] == "USD") and (command[2] == "EUR"):
            rateUtoE = float(command[1])
        elif (len(command) == 3) and (command[0] == "EUR") and (command[2] == "USD"):
            rateEtoU = float(command[1])
        elif (len(command) == 2) and (command[1] == "USD"):
            usd = float(command[0])
            if (rateUtoE == None):
                print("No USD-EUR rate defined yet!")
            else:
                print("{:.2f} USD = {:.2f} EUR".format(usd, usd*rateUtoE))
        elif (len(command) == 2) and (command[1] == "EUR"):
            eur = float(command[0])
            if (rateEtoU == None):
                print("No EUR-USD rate defined yet!")
            else:
                print("{:.2f} EUR = {:.2f} USD".format(eur, eur*rateEtoU))
        elif (len(command) == 1) and (command[0] == "quit"):
            break
        else:
            print("Illegal command!")
    except ValueError:
        print("Illegal command!")