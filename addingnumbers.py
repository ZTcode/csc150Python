
def main():
    total = 0

    response = "unknown"
    while response[0] != 'n':
        val = eval(input("Enter a number: "))
        total += val 
        response = input("Do you have more data? (y/n): ")

    print("The total is", total)

main()

    
    
