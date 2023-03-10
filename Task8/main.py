# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# Пример:
# 3 2 4 -> yes
# 3 2 1 -> no

chocolate_length = int(input("Укажите размеры шоколадки в дольках. Длина: "))
chocolate_width = int(input("Ширина: "))

piece = int(input("Укажите размер кусочка, который нужно отломить: "))

result = "answer"
if (piece < (chocolate_length * chocolate_width)) and ((piece % chocolate_length == 0) or (piece % chocolate_width == 0)): 
    result = "yes"
else: result = "no"

print(chocolate_length, chocolate_width, piece, " -> ", result)