from random import randint
from time import perf_counter

my_numbers = []
random_numbers = []
counter = 0
tries = 0

while True:
    num = int(input('Adj meg egy számot 1 és 90 között: '))
    if 0 < num < 91 and num not in my_numbers:
        my_numbers.append(num)
        counter += 1
    else:
        print('HIBA!')
    if counter == 5:
        break

start = perf_counter()

while True:
    tries += 1
    for x in range(5):
        random_numbers.append(randint(1, 90))
    check =  all(item in random_numbers for item in my_numbers)
    if check == True:
        end = perf_counter()
        break
    else:
        random_numbers.clear()

print(random_numbers)
print('Sorsolások száma:', tries)
print(f'Sorsolás alatt eltelt idő: {round(end-start, 2)} mp')