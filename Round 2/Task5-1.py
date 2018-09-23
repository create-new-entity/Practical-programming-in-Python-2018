
def checkTickets(winningTicket, tickets):
    print("Correct numbers: " + " ".join(str(digit) for digit in winningTicket))
    for ticket in tickets:
        matchedDigits = []
        for digit in ticket:
            if digit in winningTicket:
                matchedDigits.append(digit)
        if len(matchedDigits) > 0:
            print("Ticket: " + " ".join(str(digit) for digit in ticket) + " (" + str(len(matchedDigits)) + " correct: " + " ".join(str(digit) for digit in matchedDigits) + ")")
        else:
            print("Ticket: " + " ".join(str(digit) for digit in ticket) + " (0 correct)")
            