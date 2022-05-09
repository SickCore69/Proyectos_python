# Dictionart comprehensios that save whos keys be the firts 1000 natural numbers with your squeares raise at how value

def dict_comprehensions():
    dict_comp = {i:i**2 for i in range(1,1001)}
    print(dict_comp)

if __name__ == '__main__':
    dict_comprehensions()
