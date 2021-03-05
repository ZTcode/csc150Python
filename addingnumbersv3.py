
def main():
    total = 0

    while True: 
        response = input("Enter a number: ")
        if len(response) > 0: #not a blank line
            val = eval(response)
            total += val
        else:
            break 

    print("The total is", total)

main()

    
    
