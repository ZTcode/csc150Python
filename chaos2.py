
def main():
        print("this program illustrates a chaotic function")
        n = eval(input("how many numbers should i print? "))
        x = eval (input("enter a number between 0 and 1: "))
        for i in range(n):
                x = 2.0 * x * (1 - x)
