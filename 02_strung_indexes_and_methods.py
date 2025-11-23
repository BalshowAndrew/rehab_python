s = "hello python"

print(f"s = {s}")
print(f"s[0] = {s[0]}")
print(f"s[1] = {s[1]}")
print(f"s[-1] = {s[-1]}")

# иднекс последнего знака
print(f"last index = {len(s) -1}")
print(f"s[{len(s) - 1}] = {s[len(s) - 1]}")

# обработка исключения: индекс стороки вышел за пределы диапазона
try:
    print(s[12])
except IndexError:
    print("string index out of range")
    print()

# срезы
str = "the Phython is the best"
print(f"str = {str}")

print(f"str[:3] = {str[:3]}")
print(f"str[:-4] = {str[:-4]}")
print(f"str[-4:] = {str[-4:]}")
print(f"str[-4:-2] = {str[-4:-2]}")
print(f"str[-4:2] = {str[-4:2]}")
print(f"len(str) = {len(str)}")
print(f"str[-8:19] = {str[-8:19]}")

# шаги в срезах
print(f"str[:: 2] = {str[:: 2]}")
print(f"str[:: -2] = {str[:: -2]}")

# string methods
print(str.capitalize())
print(str.lower())
print(str.upper())
print(str)
print(str.count('th'))
print(str.count('t'))
print(str.count("t", 4))
print(str.count("t", 4, -2))
print(str.find("the"))
print(str.find("the", 4))
print(str.rfind("the"))
print(str.index('the'))
print(str.rindex('the'))
print(str.find('rule'))

try:
    print(str.index('rule'))
except ValueError:     
    print('Substring not found!')

print(str.replace('the', 'THE'))
print(str.replace('the', 'THE', 1))

print(str.isalpha())
str_mod = str.replace('e', '5')
print(str_mod.isalpha())
str_mod = str.replace(' ', 'w')
print(str_mod.isalpha())

str_new = 'abcd'
print(str_new.rjust(5, 'A'))
print(str_new.ljust(7, 'D'))

print(str.strip(' '))

print(str.split(' '))
print(str.split('t'))
split_str = str.split('t')
print('t'.join(split_str))

print(str.startswith('the'))
