class h:
    def test(self):
        a = 4
        for i in range(5):
            yield i * a



y = h().test()

for i in y:
    print(i)

a = b = c = 5


print(b)