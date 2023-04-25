number = int(input('Enter the number: '))
binary = ''
while(number > 1 or number == 1 ):
    quotient = number // 2
    remainder = number % 2
    binary = str(remainder) + binary
    # print(2,'  ',number,'      ', remainder)
    number = quotient
print(binary)