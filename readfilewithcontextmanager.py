with open('test.txt') as file :
    print(file.readline())
    print(file.readline())
    print(file.readline())
    print(file.closed)
    file.close()
    print(file.closed)