# convert2.py
#   A program to convert Celsius to Fahreheit 5 times 

def main():
    print("Converting from celcius to fahrenheit")
    for i in range(5):
        celsius = eval(input("What is the Celsius Temperature? "))
        fahrenheit = 9/5 * celsius + 32
        print("The temperature is" , fahrenheit, "degrees fahrenheit.")

main()
