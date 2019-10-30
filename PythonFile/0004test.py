import hashlib
import random


# m = random.getrandbits(256)
# print(m)
# n = hashlib.sha256(str(random.getrandbits(256)).encode('utf-8')).hexdigest()
# print(n)

m = hashlib.sha256()
m.update(b"Nobody inspects")
# m.update(b" the spammish repetition")
# x = m.hexdigest()
x = str(m.digest())
print(x)