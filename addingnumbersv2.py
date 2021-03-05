
def main():
    total = 0

    response = "unknown"
    while len(response) > 0: 
        response = input("Enter a number: ")
        if len(response) > 0: #not a blank line
            val = eval(response)
            total += val
        

    print("The total is", total)

main()

    
    
