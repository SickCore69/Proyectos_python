def list_comprehensions(): 
    #square = []
    #for i in range(1,101):
    #    if i % 3 == 0 and i % 5 == 0: 
    #        square.append(i**2)
    #print(square)
    square = [i**2 for i in range(1, 101) if i % 3 == 0 and i % 5 == 0]
    print(square)

if __name__ == '__main__':
    list_comprehensions()

