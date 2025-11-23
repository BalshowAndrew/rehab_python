"""Module describe the work with variables."""
import sys

a = []
aa = ['a', 'b']
x = y = z = [1, 2, 3]
b = 1.001
c = cc = ccc = 'coolboy'
cc = None

# Поличаем количество ссылок на объект
print(sys.getrefcount([]))
print(sys.getrefcount(['a', 'b']))
print(sys.getrefcount([1, 2, 3]))
print(sys.getrefcount(x))
y = None
print(sys.getrefcount(x))
print(sys.getrefcount(1.001))
print(sys.getrefcount('coolboy'))
