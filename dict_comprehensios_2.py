def dict_comprehensions():
    dict_comp = {
        "numbers":[1, 2, 3, 4, 5.5],
        "letters":["a", "b", "c", "d", "f"]            
        }
    for key, value in dict_comp.items():
        print(key, value)
    

if __name__ == '__main__':
    dict_comprehensions()
