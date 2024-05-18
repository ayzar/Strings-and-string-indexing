# 3. Задача «Равные части».
# Описание: разделить заданную строку пополам на две части и поменять их местами.
# Пример: дана строка «кенгуру». Требуется получить «урукенг».
string = "кенгуру"
string_length = len(string)
index = string_length // 2
print(string[string_length-index:] + string[:string_length-index])