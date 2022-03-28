hash_table = [[], ] * 10


def check_prime(n):
    if n == 1 or n == 0:
        return 0

    for i in range(2, n//2):
        if n % i == 0:
            return 0

    return 1


def get_prime(n):
    if n % 2 == 0:
        n = n + 1

    while not check_prime(n):
        n += 2

    return n


def hash_function(key):
    capacity = get_prime(10)
    return key % capacity


def insert(key, data):
    index = hash_function(key)
    hash_table[index] = [key, data]


def delete(key):
    index = hash_function(key)
    hash_table[index] = 0


insert(123, "antelope")
insert(432, "coyote")
insert(213, "dolphin")
insert(654, "hawk")

print(hash_table)

delete(123)

print(hash_table)
