# Програмування. Частина 1, Лабораторна робота №7.2
print('Лабораторна робота №7.2, Коломоєць Ольга')
n=int(input("Введіть значення n "))
def prime_factors(n):
    factors = []  
    divisor = 2  

    while n > 1:
        while n % divisor == 0:  
            factors.append(divisor) 
            n //= divisor  
        divisor += 1 
    return factors

result = prime_factors(n)
print(" ".join(map(str, result)))