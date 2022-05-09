# Uso de lambda para saber si una palabra es palindromo o no 
#def palindrome(string):
#    if string == string[::-1]:
#        print("Es un palindromo", string)
#        return(string)
#    else:
#        print("La palabra no es un palidromo", string)
#        return(string)

#if __name__ == '__main__':
#    palindrome("oso")

palindrome = lambda string: string == string[::-1]
print(palindrome("ana"))
