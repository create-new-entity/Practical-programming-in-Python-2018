
rateUtoE = None
rateEtoU = None

while True:
    command = input("Give a command: ")
    command = command.split(" ")
    try:
        if (len(command) == 3) and (command[0].lower() == "USD".lower()) and (command[2].lower() == "EUR".lower()):
            rateUtoE = float(command[1])
        elif (len(command) == 3) and (command[0].lower() == "EUR".lower()) and (command[2].lower() == "USD".lower()):
            rateEtoU = float(command[1])
        elif (len(command) == 2) and (command[1].lower() == "USD".lower()):
            usd = float(command[0])
            if (rateUtoE == None):
                print("No USD-EUR rate defined yet!")
            else:
                print("{:.6f} USD = {:.6f} EUR".format(usd, usd*rateUtoE))
        elif (len(command) == 2) and (command[1].lower() == "EUR".lower()):
            eur = float(command[0])
            if (rateEtoU == None):
                print("No EUR-USD rate defined yet!")
            else:
                print("{:.6f} EUR = {:.6f} USD".format(eur, eur*rateEtoU))
        elif (len(command) == 1) and (command[0].lower() == "quit"):
            break
        else:
            print("Illegal command!")
    except ValueError:
        print("Illegal command!")