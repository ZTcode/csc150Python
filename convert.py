# convert.py
#   A program to convert Celsius to Fahreheit

def main():
    print("Converting from celcius to fahrenheit")
    celsius = eval(input("What is the Celsius Temperature? "))
    fahrenheit = 9/5 * celsius + 32
    

    if fahrenheit > 90:
        print("It's hot as hell out!")

    if fahrenheit < 30:
        print("It cold as shit nigga, bundle up!")
    
    print("The temperature is", fahrenheit, "degrees fahrenheit.")    
    

main()


