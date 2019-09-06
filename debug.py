import time

q = time.time()
time.sleep(2)
s = time.time()

h = s-q
print(type(h))