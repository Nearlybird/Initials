#get full name
def get_initials(fullname):
    first = fullname[0:1]
    initials = first.upper()
    for index in range(len(fullname)):
        if fullname[index] == " ":
            initials += fullname[index+1].upper()
    return initials

def main():
    name = input("What your full name is? ")
    print(get_initials(name))

if __name__ == '__main__':
    main()

#select only the first letters of all words
    #Identify each word
    #Take the first letter of each word
#capitalize them letters
