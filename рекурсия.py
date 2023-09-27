# Это класс, представляющий элементы, которые могут быть коробками или ключами.
class Item:
    def __init__(self, is_box=False):
        self.is_box = is_box

    def is_a_box(self):
        return self.is_box

    def is_a_key(self):
        return not self.is_box


# Функция для рекурсивного поиска ключа во вложенных коробках.
def look_for_key(box):
    for item in box:
        if item.is_a_box():
            # Если элемент является коробкой, вызываем функцию look_for_key рекурсивно.
            look_for_key(item)
        elif item.is_a_key():
            # Если элемент является ключом, выводим сообщение.
            print("Нашёл ключ")

#Создаем коробку верхнего уровня.
top_level_box = [Item(is_box=True), Item(is_box=True), Item(is_box=False)]

#Помещаем вложенные коробки и ключи внутрь верхней коробки.
top_level_box[0] = [Item(is_box=False), Item(is_box=False)]
top_level_box[1] = [Item(is_box=True), Item(is_box=False)]

#Начинаем поиск с верхней коробки.
look_for_key(top_level_box)



# стек
class Stack:
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        if len(self.stack) == 0:
            return None
        removed = self.stack.pop()
        return removed


# рекурсия
def factorial(n):
    # Базовый случай: если n равно 0 или 1, возвращаем 1.
    if n == 0 or n == 1:
        return 1
    # Рекурсивный случай: вызываем функцию для (n-1) и умножаем на n.
    else:
        return n * factorial(n - 1)


result = factorial(5)  # Вычислит факториал 5, что равно 5 * 4 * 3 * 2 * 1 = 120
print(result)
