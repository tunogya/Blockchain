from hashlib import sha256

x = 5
y = 0
while sha256(str(x * y).encode()).hexdigest()[:4] != "0000":
    y += 1
    print(y, sha256(str(x * y).encode()).hexdigest()[:4])
print(y)
