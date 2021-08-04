"""Спортсмен поставил перед собой задачу пробежать в общей сложности Х километров. 
В первый день спортсмен пробежал Y километров, а затем он каждый день увеличивал пробег на 10% от предыдущего значения. 
Определите номер дня в который спортсмен достигнет своей цели. 
Оформите решение в виде программы, которая на вход принимает числа X и Y и выводит номер найденного дня.""" 
 
 
# Input the values 
print("Your goal in kilometers:") 
x = int(input()) 
print("First day running result: ") 
y = float(input()) 
day = int() 
 
# Cycle to find the day number 
while x != y and y < x: 
    y = y + (y * 0.1) 
    day += 1 
 
# Print the result 
print("Your goal will be achieved in " + str(day))
