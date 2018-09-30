def isInt(word):
    try:
        x = int(word)
        return True
    except:
        return False
        
        
def isFloat(word):
    try:
        x = float(word)
        return True
    except:
        return False 



def isBool(word):
    if word == "True" or word == "true" or word == "False" or word == "false":
        return True
    else:
        return False

def tOrf(word):
    if word == "True" or word == "true":
        return True
    return False
        
       

def wordTypes(fileName):
    wordTypesDic = {}
    typeLists = [[], [], [], []]
    with open(fileName) as inFile:
        for line in inFile.readlines():
            line = line.strip("\n").split()
            for word in line:
                if isInt(word):
                    typeLists[0].append(int(word))
                elif isFloat(word):
                    typeLists[1].append(float(word))
                elif isBool(word):
                    typeLists[2].append(tOrf(word))
                else:
                    typeLists[3].append(word)
                
    wordTypesDic[int] = typeLists[0]
    wordTypesDic[float] = typeLists[1]
    wordTypesDic[bool] = typeLists[2]
    wordTypesDic[str] = typeLists[3]
    
    wordTypesDic[int].sort()
    wordTypesDic[float].sort()
    wordTypesDic[bool].sort()
    wordTypesDic[str].sort()
    
    return wordTypesDic
    