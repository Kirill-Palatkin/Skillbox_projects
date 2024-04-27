class LRUCache:

    cache_list = dict()
    key_list = []

    def __init__(self, capacity):
        self.capacity = capacity

    @property
    def cache(self):
        return self.cache_list[self.key_list[0]]

    @cache.setter
    def cache(self, new_elem):
        self.key_list.append(new_elem[0])

        if len(self.key_list) > self.capacity:
            self.key_list.pop(0)

        self.cache_list[new_elem[0]] = new_elem[1]

    def get(self, key):
        self.key_list.pop(0)
        self.key_list.append(key)

        if key in self.key_list:
            return self.cache_list[key]

    def print_cache(self):
        print('\nLRUCache:')
        for key in self.key_list:
            if key in self.cache_list:
                print(f'{key}: {self.cache_list[key]}')
        print()


# Создаем экземпляр класса LRU Cache с capacity = 3
cache = LRUCache(3)

# Добавляем элементы в кэш
cache.cache = ("key1", "value1")
cache.cache = ("key2", "value2")
cache.cache = ("key3", "value3")

# # Выводим текущий кэш
cache.print_cache()  # key1 : value1, key2 : value2, key3 : value3

# Получаем значение по ключу
print(cache.get("key2"))  # value2

# Добавляем новый элемент, превышающий лимит capacity
cache.cache = ("key4", "value4")

# Выводим обновленный кэш
cache.print_cache()  # key2 : value2, key3 : value3, key4 : value4
