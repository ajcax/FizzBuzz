lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
resultado = []
for i in lista:
    if i % 3 == 0 and i % 5 == 0:
        resultado.append("FizzBuzz")
    elif i % 3 == 0:
        resultado.append("Fizz")
    elif i % 5 == 0:
        resultado.append("Buzz")
    else:
        resultado.append(i)
print(resultado)
def proceso(number):
    if number % 3 == 0 and number % 5 == 0:    
        return 'FizzBuzz'
    elif number % 5 == 0:
        return 'Buzz'
    elif number % 3 == 0:
        return 'Fizz'
    else:
        return number