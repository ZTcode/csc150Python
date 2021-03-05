# File: chaos.py
# A simple program illustraing chaotic behavior
def main():
    print("This program illustrates a chaotic function")
    x = eval(input("enter a number between 0 and 1: "))
    n = eval(input("How many numbers should i print?: "))
    for i in range(n):
        #x = 3.9 * x * (1-x)
        x = 3.9 * (x - x * x)
        print(x)

main()
