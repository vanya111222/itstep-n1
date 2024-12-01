'''class PowersOfTwo:
    def __init__(self):
        self.exponent = 0

    def __iter__(self):
        return self

    def __next__(self):
        result = 2 ** self.exponent
        self.exponent += 1
        return result



powers_of_two = PowersOfTwo()


for _ in range(10):
    print(next(powers_of_two))'''

'''def powers_of_three():
    exponent = 0
    while True:
        yield 3 ** exponent
        exponent += 1


gen = powers_of_three()


for _ in range(10):
    print(next(gen))'''