import time


class Rng():
    def __init__(self, m, a, b, x):
        self.m = m
        self.a = a
        self.b = b
        self.x = x

    def gen(self, n):
        liste = []
        for i in range(n):
            timestamp = int(time.time() % 15)
            self.x = (self.a * self.x + self.b) * timestamp
            self.x = self.x % n
            
        return self.x


rng1 = Rng(7,5,8,13)

print(rng1.gen(10))