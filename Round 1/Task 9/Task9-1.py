a = int(input())
b = int(input())
k = int(input())


def get_prime_numbers(a, b):
    i = a
    prime_numbers = []
    while i <= b:
        j = 2
        prime = True
        while j < i:
            if i % j == 0:
                prime = False
                break
            j += 1
        if prime and i!=1 and i!=0:
            prime_numbers.append(i)
        i += 1
    return prime_numbers
    
    
prime_numbers = get_prime_numbers(a,b)

i = 0
output = ""
first = True
while i < len(prime_numbers) and a <= prime_numbers[i] <= b:
    if first:
        first = False
    else:
        output += " "
    output += str(prime_numbers[i])
    i += k
print(output)