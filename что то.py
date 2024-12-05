print("Задача №1")
s = input("Введите строку:")
count = 0
vowels = set("aeiou")
for letter in s:
    if letter in vowels:
        count += 1
print("Количество гласных равно:")
print(count)


print("Задача №2")
file = open('input', 'r')
s = file.readlines()
s.reverse()
print(''.join(s))
print("задача №3")
