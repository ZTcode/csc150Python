# Acronym.py
#   A program that gives the acronym of a phrase given by the user

def main():

    phrase = input("Enter a pharse: ")

    words = phrase.split()      #splits phrase in words as a list of strings
    acronym = "" # empty string 
    for i in words:          #we access word one by one
                            # us accumulation to add each character one by one
        acronym = acronym + i[0]        #this is the first letter of the word


    print("The acronym is", acronym.upper())

    

main()


    

    
    
