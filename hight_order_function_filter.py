# Filtra los numeros pares en un rango de 1-10 y los imprime

#numbers_list = [1,2,3,4,5,6,7,8,9,10]
#odd = [i for i in numbers_list if i % 2 == 0]
#print(odd)
my_list = [1,2,3,4,5,6,7,8,9,10]
multiple = list(filter(lambda x: x%2==0, my_list))
print(multiple)
