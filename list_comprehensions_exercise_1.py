# Just save numbers that be multiple of 4, 6 and 9 in a list and one print in a range 1-9999.

def list_9999():
    multiple = [i for i in range(1,9999) if  i % 4 ==0 and i % 6 == 0 and i % 9 == 0]
    print(multiple)

if __name__ == '__main__': 
    list_9999()
