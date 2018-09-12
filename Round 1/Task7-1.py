r = int(input())
c = int(input())
h = int(input())
w = int(input())



ch = "#"

i = 0
while i<r:
    if ch == "#":
        ch = " "
    else:
        ch = "#"
    j = 0
    while j<h:
        k = 0
        output = ""
        ch2 = ch
        while k<c:
            l = 0
            while l<w:
                output += ch2
                l += 1
            if ch2 == "#":
                ch2 = " "
            else:
                ch2 = "#"
            k += 1
        print(output)
        j += 1
    i += 1