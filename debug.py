import multiprocessing

class One():
    def test(self):
        for i in range(10):
            print('test is nums %d' % i)

    def in_test(self):
        multiprocessing.Process(target=self.test).start()

if __name__ == '__main__':
    One().in_test()
