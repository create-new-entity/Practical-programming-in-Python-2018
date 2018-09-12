while True:
    n = input()
    if n == "":
        break
    n = int(n)
    sym = input()
    mid = int(n/2)
    sindex1 = sindex2 = mid
    midCrossed = False
    
    if n == 1:
        print(sym)
    else:
        i = 0
        while i < n:
            output = ""
            j = 0
            while j < n:
                if j == sindex1:
                    output += sym
                elif j == sindex2 and not sindex1 == sindex2:
                    output += sym
                else:
                    output += " "
                j += 1
            print(output)
            if midCrossed:
                sindex1 += 1
                sindex2 -= 1
            else:
                sindex1 -= 1
                sindex2 += 1
            i += 1
            if i > mid and midCrossed == False:
                midCrossed = True
                sindex1 += 2
                sindex2 -= 2
    print() 