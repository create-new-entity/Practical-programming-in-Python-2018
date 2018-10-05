class QuitCommandError(Exception):
    pass
   

def readPressureValue(inputMessage):
    while True:
        try:
            userInput = input(inputMessage)
            pressure = int(userInput)
            if pressure <= 0:
                raise ValueError
            break
        except ValueError:
            if userInput == "quit":
                raise QuitCommandError
            else:
                print("Enter a positive integer!")
    return pressure
        
    

while True:
    try:
        systolic = readPressureValue("Enter systolic pressure (or \"quit\" to stop): ")
        diastolic = readPressureValue("Enter diastolic pressure (or \"quit\" to stop): ")
        if systolic < 90 or diastolic < 60:
            print("Low")
        elif systolic < 120 and diastolic < 80:
            print("Normal")
        elif (120 <= systolic <= 129) and diastolic < 80:
            print("Elevated")
        elif(systolic > 180) or (diastolic > 120):
            print("Hypertensive crisis (consult your doctor immediately)")
        elif(systolic >= 140) or (diastolic >= 90):
            print("High (hypertension) stage 2")
        elif (130 <= systolic <= 139) or (80 <= diastolic <= 89):
            print("High (hypertension) stage 1")
    except QuitCommandError:
        print("Quit-command received. Stopping the program.")
        break