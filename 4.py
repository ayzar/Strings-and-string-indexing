# 4.Задача «Четные и нечетные».
# Описание: используя срезы, вывести все чётные и нечётные символы заданной строки.
# Пример: дана строка «нейропрограммирование». 
# Требуется вывести «нйорграмрвне  ерпормиоаи».'''
string = "нейропрограммирование"
print(string[::2],' ',string[1::2])
