def start():
    filename = input("Enter the file name here -->  ")
    noOfWords = 0
    a = open(filename)
    b = a.read()
    print(b)

    for line in b:
        words = line.split("#")
        noOfWords = noOfWords+len(words)
    
    print(noOfWords)

start()