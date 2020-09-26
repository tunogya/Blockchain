from hashlib import sha256

x = 83687839376
y = 0


while sha256(str(x * y).encode()).hexdigest()[:8] != "00000000":
    y += 1
    print(y, sha256(str(x * y).encode()).hexdigest()[:8])
print(y)
