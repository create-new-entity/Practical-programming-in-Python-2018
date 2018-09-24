import sys

encryptD = {}
decryptD = {}


def setDictionaries(cipherAlphabet):
    i = 'a'
    j = 0
    while True:
        encryptD[i] = cipherAlphabet[j]
        decryptD[cipherAlphabet[j]] = i
        if i == 'z':
            break
        i = chr(ord(i)+1)
        j += 1
        
setDictionaries(sys.argv[1])


def enOrdeCrypt(dict, inputStr):
    outputStr = ""
    for c in inputStr:
        if 'a' <= c <= 'z':
            outputStr += dict[c]
        else:
            outputStr += c
    return outputStr


while True:
    command = input("Give a command: ")
    if command.find("encrypt ") != -1:
        command = command.partition("encrypt ")
        print(enOrdeCrypt(encryptD, command[2]))
    elif command.find("decrypt ") != -1:
        command = command.partition("decrypt ")
        print(enOrdeCrypt(decryptD, command[2]))
    elif command == "quit":
       break
    else:
        print("Illegal command!")